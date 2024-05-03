from antlr4 import *
from dist.CPP14Parser import CPP14Parser
from dist.CPP14ParserVisitor import CPP14ParserVisitor
from Utils import *
import re
import inspect
import csv
import os

def logToCsv(current_function_name, ctx_text, rust_code):
    if os.environ.get('DEBUG') == "1":
        log_entry = [current_function_name, ctx_text, rust_code]
            # Open the CSV file and write the log entry as a row
        with open("log.csv", "a", encoding=None, newline='') as file:
            writer = csv.writer(file)
            writer.writerow(log_entry)

def convert_c_array_signature_to_rust(c_code):
    # Regular expression to find array declarations in C
    array_pattern = r'(\w+\s*\w*)\s+(\w+)\[([\d\[\]]*)\]'

    # Find all matches
    matches = re.findall(array_pattern, c_code)

    # Convert each match to Rust's format
    rust_arrays = []
    for match in matches:
        # Splitting dimensions and creating the Rust array format
        dimensions = match[2].split('][')
        base_type = match[0].strip()  # Base type, stripping any extra whitespace
        rust_type = base_type

        # Handle unspecified first dimension
        if dimensions[0] == '':
            rust_type = f'[{rust_type}]'
            dimensions = dimensions[1:]

        # Process remaining dimensions
        for dim in reversed(dimensions):
            if dim:  # Skip empty dimensions
                rust_type = f'[{rust_type}; {dim}]'

        rust_arrays.append((match[1], base_type, rust_type))  # Store variable name, base type, and new type
    return rust_arrays


class CPPtoRustConverter(CPP14ParserVisitor):
    def __init__(self):
        # output
        self.rustCode = '''#![allow(warnings, unused)]
        use std::ops::{Add,AddAssign,BitAnd,BitAndAssign,BitOr,BitOrAssign};
        use std::ops::{BitXor,BitXorAssign,Div,DivAssign,Index,Mul,MulAssign};
        use std::ops::{Neg,Not,Rem,RemAssign,Shl,ShlAssign,Shr,ShrAssign,Sub,SubAssign};
        #[path = "../libs/Vector.rs"]
        pub mod Vector;
        use Vector::{vector, ListInit};

        #[path = "../libs/Stack.rs"]
        pub mod Stack;
        use Stack::stack;

        #[path = "../libs/Map.rs"]
        pub mod Map;
        use Map::map;
        #[path = "../libs/Unordered_map.rs"]
        pub mod Unordered_map;
        use Unordered_map::unordered_map;

        #[path = "../libs/Deque.rs"]
        pub mod Deque;
        use Deque::{deque};

        #[path = "../libs/Set.rs"]
        pub mod Set;
        use Set::{set};

        #[path = "../libs/UnorderedSet.rs"]
        pub mod UnorderedSet;
        use UnorderedSet::{unordered_set};

        #[path = "../libs/String.rs"]
        pub mod String;
        use String::string;
        '''
        
        # handling data type conversion
        self.isSimpleDecl = False
        self.arraySizeDecl = ["",""]
        self.Std = None

        # Handling operator keyword conversion
        self.opKeywordConversionMap = {
            "and": "&&",
            "or": "||",
            "xor": "^",
        }
        # Handling known Function types
        self.currentFunction = ""

        # Handling switch case breaks and braces
        self.isSwitchStatementCaseBeingEvaluated = False
        self.switchEval = False

        # Handling Classes
        self.currentClassName = ""
        self.idFromPrimaryExpression = False
        self.isFunctionDefinitionInsideClass = False
        self.isClassFunctionParameters = False
        self.functionDeclName = ""
        self.isThisAConstructorCall = False
        self.isFnPublic = False
        self.attributesInClasses = {}
        self.currentFunctionParameters = set()
        self.selfPresent = False
        self.inFunctionDeclaration = False
        self.fnRtnReference = False
        self.implPresent = False

        # assumes we are not using unary - or unary +. Detecting those operators
        # requires analysing function parameters
        # mp[0] = function name, mp[1] = trait name , mp[2] = type <> = ? should be added
        self.opConversionMap = {
            "+": ["add", "Add", "Output"],
            "+=": ["add_assign", "AddAssign", ""],
            "&": ["bitand","BitAnd", "Output"],
            "&=": ["bitand_assign","BitAndAssign", ""],
            "|": ["bitor","BitOr", "Output"],
            "|=": ["bitor_assign","BitOrAssign", ""],
            "^": ["bitxor","BitXor","Output"],
            "^=": ["bitxor_assign","BitXorAssign",""],
            "/": ["div","Div","Output"],
            "/=": ["div_assign","DivAssign",""],
            "[]": ["index","Index","Output"],
            "*": ["mul","Mul","Output"],
            "*=": ["mul_assign","MulAssign",""],
            "!": ["not","Not","Output"],
            "%": ["rem","Rem","Output"],
            "%=": ["rem_assign","RemAssign",""],
            "<<": ["shl","Shl","Output"],
            "<<=": ["shl_assign","ShlAssign",""],
            ">>": ["shr","Shr","Output"],
            ">>=": ["shr_assign","ShrAssign",""],
            "-": ["sub","Sub", "Output"],
            "-=": ["sub_assign","SubAssign",""],
            "=": ["assign","",""],
        }
        self.unOpMap = {
            "-": ["neg","Neg","Output"], # Unary -
        }
        self.isNeg = False

        # Handling declaration of objects belongs to classes in declared in the file
        self.classSet = set()

        # Handling templates 
        self.currentTemplateParameters = ""
        self.isThisATemplateDeclaration = False

        #Handling namespaces
        # self.isThisANameSpaceDeclaration = False
        self.namespaceDepth = 0 # This keeps the present depth in a nested namespace.

        #Handling Type Convertions
        self.conversion_map = {
            "char": "char",
            "unsignedchar": "u8",
            "signedchar": "i8",
            "shortint": "i16",
            "unsignedshortint": "u16",
            "signedint": "i32",
            "int": "i32",
            "unsignedint": "u32",
            "signedlongint": "i64",  # Data model dependent
            "longint": "i64",  # Data model dependent
            "unsignedlongint": "u64",  # Data model dependent
            "signedlonglongint": "i64",
            "longlongint": "i64",
            "longlong": "i64",
            "unsignedlonglongint": "u64",
            "size_t": "usize",
            "float": "f32",
            "double": "f64",
            "longdouble": "f64",  # Note: f128 was removed in Rust
            "bool": "bool",
        }

        # Handling Implicit conversion
        self.leftHandSideDataType = None
        self.isSimpleAssignment = False
        self.hasBracket = False


        # Handling Pointers in function parameters
        self.unsafeEnabled = True
        self.declIsPointer = False
        self.usesLibC = False
        self.inFunctionParameters = False
        self.arraySignature = ""

        #Handling Pointer
        self.isPointerDeclaration = False

        #Handling STLs
        self.stlDataTypeMap = dict()

        #Handling Vectors
        self.isVectorDeclaration = False

        #Handling Stacks
        self.isStackDeclaration = False

        #Handling orderedmap
        self.isMapDeclaration = False

        #Handling unorderedmap
        self.isUnMapDeclaration = False
         
        #Handling Queues
        self.isDequeDeclaration = False

        #Handling Sets
        self.isSetDeclaration = False

        #Handling Unordered Sets
        self.isUnorderedSetDeclaration = False

        #Handling Strings
        self.isStringDeclaration = False

    def convert(self, tree):
        self.visit(tree)
        return self.rustCode

    # Visit a parse tree produced by CPP14Parser#literal.
    def visitLiteral(self, ctx: CPP14Parser.LiteralContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)

        if ctx.PointerLiteral() is not None:
            self.rustCode += "// Safe rust code does not support Null Pointers, please refer to the documentation to handle this case.\n"

        elif ctx.UserDefinedLiteral() is not None:
            self.rustCode += (
                "// User Defined Literals are currently not supported, please refer to the documentation to handle this case of "
                + ctx.getText()
                + "\n"
            )

        else:
            LiteralText = ctx.getText() + " "

            if ctx.StringLiteral() is not None and self.currentFunction == "printf":
                LiteralText = printfReplacer(LiteralText)
            
            if ctx.StringLiteral() is not None and self.currentFunction != "printf" and self.currentFunction != "cout":
                self.rustCode+=" string::from( "


            self.rustCode += LiteralText

            if ctx.StringLiteral() is not None and self.currentFunction != "printf" and self.currentFunction != "cout":
                self.rustCode+=" ) "

            if self.currentFunction == "printf":
                self.currentFunction = ""

    # Expression Chain

    # Visit a parse tree produced by CPP14Parser#literal.
    def visitExpression(self, ctx: CPP14Parser.ExpressionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)

        expressionVisitor(self, ctx)

    def visitLogicalOrExpression(self, ctx: CPP14Parser.LogicalOrExpressionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        expressionVisitor(self, ctx)

    def visitLogicalAndExpression(self, ctx: CPP14Parser.LogicalAndExpressionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        expressionVisitor(self, ctx)

    def visitInclusiveOrExpression(self, ctx: CPP14Parser.InclusiveOrExpressionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        expressionVisitor(self, ctx)

    def visitExclusiveOrExpression(self, ctx: CPP14Parser.ExclusiveOrExpressionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        expressionVisitor(self, ctx)

    def visitAndExpression(self, ctx: CPP14Parser.AndExpressionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        expressionVisitor(self, ctx)

    def visitEqualityExpression(self, ctx: CPP14Parser.EqualityExpressionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        expressionVisitor(self, ctx)

    def visitRelationalExpression(self, ctx: CPP14Parser.RelationalExpressionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        expressionVisitor(self, ctx)

    def visitShiftExpression(self, ctx: CPP14Parser.ShiftExpressionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.visit(ctx.getChild(0))
        childCount = ctx.getChildCount()
        if childCount > 1:

            if self.currentFunction == "cout" and ctx.getChild(1).Greater() is not None:
                # assuming that the things will be either a string literal or some other thing
                texts = []
                for i in range(1, childCount, 2):
                    printingText = ctx.getChild(i+1).getText()
                    if ('" ' not in printingText
                            and self.selfPresent is True
                            and printingText in self.attributesInClasses.setdefault(self.currentClassName, set())
                            and printingText not in self.currentFunctionParameters
                        ):
                        printingText = "self." + printingText
                    texts.append(printingText)
                finalString = coutHandler(texts)
                self.rustCode += finalString
                self.currentFunction = ""
            else:
                for i in range(1, childCount, 2):
                    self.visit(ctx.getChild(i))
                    self.visit(ctx.getChild(i + 1))

    def visitShiftOperator(self, ctx: CPP14Parser.ShiftOperatorContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += " " + ctx.getText() + " "

    def visitAdditiveExpression(self, ctx: CPP14Parser.AdditiveExpressionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        expressionVisitor(self, ctx)

    def visitMultiplicativeExpression(
        self, ctx: CPP14Parser.MultiplicativeExpressionContext
    ):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        expressionVisitor(self, ctx)

    def visitPointerMemberExpression(
        self, ctx: CPP14Parser.PointerMemberExpressionContext
    ):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.visit(ctx.getChild(0))
        childCount = ctx.getChildCount()
        if childCount > 1:
            self.rustCode += "// Safe Rust Code does not recommend raw pointers, thus references and addressing are not possible directly, refer to Rust documentation for more information\n"
            for i in range(1, childCount, 2):
                self.visit(ctx.getChild(i))
                self.visit(ctx.getChild(i + 1))

    def visitCastExpression(self, ctx: CPP14Parser.CastExpressionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.unaryExpression() is not None:
            self.visit(ctx.unaryExpression())
        else:
            self.visit(ctx.castExpression())
            self.rustCode += " as "
            self.visit(ctx.theTypeId())

    # visiting children
    def visitTheTypeId(self, ctx: CPP14Parser.TheTypeIdContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        # self.rustCode += ctx.theTypeId().getText()
        if ctx.getText() in self.conversion_map:
            self.rustCode += self.conversion_map[ctx.getText()]
        else:
            self.rustCode += ctx.getText()
        return super().visitTheTypeId(ctx)

    # visiting children
    def visitTypeSpecifierSeq(self, ctx: CPP14Parser.TypeSpecifierSeqContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        # return super().visitTypeSpecifierSeq(ctx)

    # visiting children

    def visitAbstractDeclarator(self, ctx: CPP14Parser.AbstractDeclaratorContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        return super().visitAbstractDeclarator(ctx)

    def visitTypeSpecifier(self, ctx: CPP14Parser.TypeSpecifierContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        return super().visitTypeSpecifier(ctx)

    def visitTrailingTypeSpecifierSeq(self, ctx: CPP14Parser.TrailingTypeSpecifierSeqContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        signedNess = True
        lengthSpecifier = None
        dataType = None
        isAuto = False
        self.Std = None
        for i in ctx.trailingTypeSpecifier():
            if i.getText() == "auto":
                dataType = "auto"
                isAuto = True
            elif i.getText() == "unsigned":
                signedNess = False
            elif i.getText() in ["int","float", "double"]:
                dataType = i.getText()
            elif i.getText() in ["short", "long", "longlong"]:
                dataType = "int"
                if i.getText() == "short":
                    lengthSpecifier = "16"
                elif i.getText() in ["long", "longlong"]:
                    lengthSpecifier = "64"
            elif i.getText() in ["int8_t", "int16_t", "int32_t", "int64_t", "uint8_t", "uint16_t", "uint32_t", "uint64_t", "size_t", "bool", "char"]:
               dataType=i.getText()
               self.Std = i.getText()
        
        if isAuto or dataType is None:
            self.rustCode += " "
            return super().visitTrailingTypeSpecifierSeq(ctx)
        # self.rustCode += ": "
        rustDataType = ""
        if self.Std is not None:
            stdConvert = {
                "int8_t": "i8",
                "int16_t": "i16",
                "int32_t": "i32",
                "int64_t": "i64",
                "uint8_t": "u8",
                "uint16_t": "u16",
                "uint32_t": "u32",
                "uint64_t": "u64",
                "size_t": "usize",
                "bool": "bool",
                "char": "char"
            }
            # self.rustCode += stdConvert[Std]
            rustDataType += stdConvert[self.Std]
        else:
            if signedNess is False:
                # self.rustCode += "u"
                rustDataType += "u"
            else:
                if dataType in ["int"]:
                    # self.rustCode += "i"
                    rustDataType += "i"
                elif dataType != "":
                    # self.rustCode += "f"
                    rustDataType += "f"
            if lengthSpecifier is not None:
                # self.rustCode += lengthSpecifier
                rustDataType += lengthSpecifier
            else:
                if dataType == "int":
                    # self.rustCode += "32"
                    rustDataType += "32"
                elif dataType == "float":
                    # self.rustCode += "32"
                    rustDataType += "32"
                elif dataType == "double":
                    # self.rustCode += "64"
                    rustDataType += "64"

        self.rustCode += rustDataType
        return super().visitTrailingTypeSpecifierSeq(ctx)

    def visitTrailingTypeSpecifier(self, ctx: CPP14Parser.TrailingTypeSpecifierContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        return super().visitTrailingTypeSpecifier(ctx)


    def visitSimpleTypeSpecifier(self, ctx: CPP14Parser.SimpleTypeSpecifierContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.visitChildren(ctx) # vedanta
        # return

    def visitElaboratedTypeSpecifier(self, ctx: CPP14Parser.ElaboratedTypeSpecifierContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        

       # Don't know what this means yet.

        if ctx.Enum() is not None:
            self.rustCode += " enum "
            # Unlike C++, Rust always has scoped Enums
            # don't know how to handle this case so just visiting the child
            if ctx.nestedNameSpecifier() is not None:
                self.visit(ctx.nestedNameSpecifier())
            self.rustCode += " " + ctx.Identifier().getText() + " "
        else:
            self.visit(ctx.classKey())

            if ctx.Identifier() is not None:
                self.visitChildren(ctx)
                self.rustCode += " " + ctx.Identifier().getText() + " "

            else:
                self.rustCode += "// Yet to support Templates, please refer to the documentation" + " "
                self.visitChildren(ctx)

    def visitClassKey(self, ctx: CPP14Parser.ClassKeyContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        # there are no classes in Rust only Structs
        self.rustCode += " struct "

    def visitTypeNameSpecifier(self, ctx: CPP14Parser.TypeNameSpecifierContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += "// Yet to support Templates, please refer to the documentation" + " "
        self.visitChildren(ctx)

    def visitCvQualifier(self, ctx: CPP14Parser.CvQualifierContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        # initial assumption
        return super().visitCvQualifier(ctx)

        if ctx.Const() is not None:
            self.rustCode += " *const "
        else:
            self.rustCode += " *mut "

    def visitClassSpecifier(self, ctx: CPP14Parser.ClassSpecifierContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        nonAttributes = []
        self.currentClassName = ctx.classHead().classHeadName().className().getText()
        self.rustCode += "#[derive(Default)]\n"
        self.rustCode += "pub "
        wasThisATemplatedClass = self.isThisATemplateDeclaration
        self.visit(ctx.classHead())
        self.rustCode += " {\n"
        if ctx.memberSpecification() is not None:
            childCount = ctx.memberSpecification().getChildCount()
            for i in range(childCount):
                child = ctx.memberSpecification().getChild(i)
                specificationType = type(child)
                if specificationType == CPP14Parser.MemberdeclarationContext:
                    # means member
                    isFunctionDeclaration = memberDeclarationIsFuntion(child)
                    if child.Semi() is not None and not isFunctionDeclaration:
                        self.visit(child)
                    elif not isFunctionDeclaration:
                        nonAttributes.append(child)
        self.rustCode += " }\n"

        if len(nonAttributes) > 0:
            className = ctx.classHead().classHeadName().className()
            self.classSet.add(className.getText())
            self.isThisATemplateDeclaration = wasThisATemplatedClass
            self.rustCode += "impl "
            if self.isThisATemplateDeclaration:
                self.rustCode += self.currentTemplateParameters
            self.visit(className)
            self.rustCode += " {\n"
            self.implPresent = True
            for i in nonAttributes:
                if i.functionDefinition() is not None:
                    functionName = getFunctionName(self,i.functionDefinition())
                    if self.currentClassName != functionName:
                        self.attributesInClasses.setdefault(self.currentClassName, set())
                        self.attributesInClasses[self.currentClassName].add(functionName)

            for i in nonAttributes:
                if i.functionDefinition() is not None:
                    self.isFnPublic = True
                    self.isFunctionDefinitionInsideClass = True
                    self.isClassFunctionParameters = True
                    self.currentClassName = className.getText()
                self.visit(i)
                self.isFunctionDefinitionInsideClass = False
                self.isFnPublic = False
                self.currentFunctionParameters.clear()
            self.rustCode += " }\n"
            self.implPresent = False

        self.currentClassName = ""

    def visitClassHead(self, ctx: CPP14Parser.ClassHeadContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.Union() is not None:
            self.rustCode += "// Currently ignoring unions in the transpilation\n"
        self.visitChildren(ctx)

    def visitAttributeSpecifierSeq(self, ctx: CPP14Parser.AttributeSpecifierSeqContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        return super().visitAttributeSpecifierSeq(ctx)

    def visitAttributeSpecifier(self, ctx: CPP14Parser.AttributeSpecifierContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += "// Currently ignoring attribute specifiers in the transpilation\n"
        self.visitChildren(ctx)

    def visitAlignmentspecifier(self, ctx: CPP14Parser.AlignmentspecifierContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += "// Currently ignoring alignment specifiers in the transpilation\n"
        self.visitChildren(ctx)

    def visitMemberSpecification(self, ctx: CPP14Parser.MemberSpecificationContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        # currently assuming all the methods to be public thus access specifiers have no meaning
        self.rustCode += "// Currently all methods and variables are assumed to be public\n"
        self.visitChildren(ctx)

    def visitMemberdeclaration(self, ctx: CPP14Parser.MemberdeclarationContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.Semi() is not None:
            if pointerHandling(ctx):
                # this is has a pointer declarator then need to something else

                # if ctx.memberDeclaratorList() -> memberDeclarator(0) -> declarator() -> pointerDeclarator -> pointerOperator(0) is not None

                cntx = ctx.memberDeclaratorList().memberDeclarator(
                    0).declarator().pointerDeclarator()

                self.visit(ctx.noPointerDeclarator())

                if ctx.attributeSpecifierSeq() is not None or ctx.declSpecifierSeq() is not None:
                    self.rustCode += ":"

                self.visit(cntx.pointerOperator(0))

                if ctx.attributeSpecifierSeq() is not None:
                    self.visit(ctx.attributeSpecifierSeq())

                if ctx.declSpecifierSeq() is not None:
                    self.visit(ctx.declSpecifierSeq())

                self.rustCode += ",\n"

            else:
                if ctx.memberDeclaratorList() is not None:
                    # self.visit(ctx.memberDeclaratorList())
                    childCount = ctx.memberDeclaratorList().getChildCount()
                    for i in range(0, childCount, 2):
                        self.visit(ctx.memberDeclaratorList().getChild(i))

                        if ctx.attributeSpecifierSeq() is not None or ctx.declSpecifierSeq() is not None:
                            self.rustCode += ":"

                        if ctx.attributeSpecifierSeq() is not None:
                            self.visit(ctx.attributeSpecifierSeq())

                        if ctx.declSpecifierSeq() is not None:
                            self.visit(ctx.declSpecifierSeq())

                        self.rustCode += ",\n"
        else:
            self.visitChildren(ctx)

    def visitMemberDeclaratorList(self, ctx: CPP14Parser.MemberDeclaratorListContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        expressionVisitor(self, ctx)

    def visitMemberDeclarator(self, ctx: CPP14Parser.MemberDeclaratorContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        # dont know about the second rule let's skip it for now
        if ctx.Colon() is not None:
            self.rustCode += "// Member Declarator needs more attention\n"
            if ctx.Identifier() is not None:
                self.rustCode += " " + ctx.Identifier().getText()
            if ctx.attributeSpecifierSeq() is not None:
                self.visit(ctx.attributeSpecifierSeq())
            self.rustCode += ":"
            self.visit(ctx.constantExpression())
        else:
            self.attributesInClasses.setdefault(self.currentClassName, set())
            self.attributesInClasses[self.currentClassName].add(ctx.declarator().getText())
            self.visitChildren(ctx)

    def visitDeclarator(self, ctx: CPP14Parser.DeclaratorContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        return super().visitDeclarator(ctx)

    def visitPointerDeclarator(self, ctx: CPP14Parser):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.arraySizeDecl = ["",""]
        if len(ctx.pointerOperator()) > 0:
            # todo!: add unsafe keyword to relevant functions
            #self.rustCode += "// Handling Pointers...\n"
            self.declIsPointer = True
        self.visitChildren(ctx)

    def visitPointerOperator(self, ctx: CPP14Parser.PointerOperatorContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.Star() is not None:
            if ctx.nestedNameSpecifier() is not None:
                self.visit(ctx.nestedNameSpecifier())

            if not self.declIsPointer:
                self.rustCode += "*"

            if ctx.attributeSpecifierSeq() is not None:
                self.visit(ctx.attributeSpecifierSeq())

            if ctx.cvqualifierseq() is not None:
                self.visit(ctx.cvqualifierseq())

        else:
            if self.inFunctionDeclaration is False:
                self.fnRtnReference = True
                self.rustCode += " " + ctx.getChild(0).getText() + " "
            if ctx.attributeSpecifierSeq() is not None:
                self.visit(ctx.attributeSpecifierSeq())

    def visitCvqualifierseq(self, ctx: CPP14Parser.CvqualifierseqContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        return super().visitCvqualifierseq(ctx)

    def visitNestedNameSpecifier(self, ctx: CPP14Parser.NestedNameSpecifierContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += " " + ctx.getText() + " "

    def visitTheTypeName(self, ctx: CPP14Parser.TheTypeNameContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        return super().visitTheTypeName(ctx)

    def visitClassName(self, ctx: CPP14Parser.ClassNameContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.Identifier() is not None:
            if self.Std is not None:
                self.Std = None
            else:
                self.rustCode += " " + ctx.Identifier().getText() + " " # ISSUE
                if self.isThisATemplateDeclaration:
                    self.rustCode += self.currentTemplateParameters
                self.isThisATemplateDeclaration = False
        else:
            self.visitChildren(ctx)

    def visitSimpleTemplateId(self, ctx: CPP14Parser.SimpleTemplateIdContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)

        if ctx.templateName().getText() == "vector" \
                or ctx.templateName().getText() == 'stack' \
                or ctx.templateName().getText() == 'queue' \
                or ctx.templateName().getText() == 'deque':
            pass
        else:
            self.rustCode += "// Templates are yet to supported! Currently copying them as it is!\n"
            self.rustCode += " " + ctx.getText() + " "
        # self.visitChildren(ctx)

    def visitEnumName(self, ctx: CPP14Parser.EnumNameContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += " " + ctx.Identifier().getText() + " "
    
    def visitEnumSpecifier(self, ctx:CPP14Parser.EnumSpecifierContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        # self.rustCode += " " + ctx.getText() + " "
        return self.visitChildren(ctx)
    
    def visitEnumHead(self, ctx:CPP14Parser.EnumHeadContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += " " + ctx.enumkey().getText() + " " + ctx.Identifier().getText() + " "
        return self.visitChildren(ctx)
    
    def visitEnumeratorList(self, ctx:CPP14Parser.EnumeratorListContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        # self.rustCode += " {\n " + ctx.getText() + " \n} "
        self.rustCode += " {\n "
        self.visitChildren(ctx)
        self.rustCode += " } "
        return
    
    def visitEnumeratorDefinition(self, ctx:CPP14Parser.EnumeratorDefinitionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        # self.rustCode += " " + ctx.Identifier().getText() + " "
        self.rustCode += ctx.enumerator().getText() + " = " 
        self.visitChildren(ctx)
        self.rustCode += ",\n"

    def visitTypedefName(self, ctx: CPP14Parser.TypedefNameContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += " " + ctx.Identifier().getText() + " "

    def visitNamespaceName(self, ctx: CPP14Parser.NamespaceNameContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += " " + ctx.getText() + "::*"

    def visitDecltypeSpecifier(self, ctx: CPP14Parser.DecltypeSpecifierContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += " " + ctx.getText() + " "
        self.rustCode += "// DeclType are yet to supported! Currently copying them as it is!\n"

    def visitNoPointerDeclarator(self, ctx: CPP14Parser.NoPointerDeclaratorContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.declaratorid() is not None:
            self.visitChildren(ctx)

        elif ctx.pointerDeclarator() is not None:
            self.rustCode += " ( "
            self.visit(ctx.pointerDeclarator())
            self.rustCode += " ) "
        elif self.isSimpleDecl is True: # array declaration    
            self.visit(ctx.noPointerDeclarator())
            if ctx.parametersAndQualifiers() is not None:
                self.visit(ctx.parametersAndQualifiers())
                self.arraySizeDecl[1] += " ] "
            rustCodeLen = len(self.rustCode)
            temp = ""
            if ctx.constantExpression() is not None:
                self.arraySizeDecl[0] += " [ "
                self.visit(ctx.constantExpression())
                temp = ";" + self.rustCode[rustCodeLen:]
                self.rustCode = self.rustCode[:rustCodeLen]
            else :
                self.arraySizeDecl[0] = " &["
            self.arraySizeDecl[1] = temp + "]" + self.arraySizeDecl[1]
        else: 
            self.visit(ctx.noPointerDeclarator())
            if ctx.parametersAndQualifiers() is not None:
                self.visit(ctx.parametersAndQualifiers())
            else:
                if not self.inFunctionParameters :
                    self.rustCode += " [ "
                    if ctx.constantExpression() is not None:
                        self.visit(ctx.constantExpression())
                    self.rustCode += " as usize] "
                    if ctx.attributeSpecifierSeq() is not None:
                        self.visit(ctx.attributeSpecifierSeq())


    def visitDeclaratorid(self, ctx: CPP14Parser.DeclaratoridContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.Ellipsis() is not None:
            self.rustCode += " ... "
        self.visit(ctx.idExpression())
        if self.isThisATemplateDeclaration:
            self.rustCode += self.currentTemplateParameters
            self.currentTemplateParameters=""
            self.isThisATemplateDeclaration=False

    def visitIdExpression(self, ctx: CPP14Parser.IdExpressionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        return super().visitIdExpression(ctx)

    def visitUnqualifiedId(self, ctx: CPP14Parser.UnqualifiedIdContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.Identifier() is not None:
            IdentifierText = ctx.Identifier().getText()
            self.currentFunction = IdentifierText
            knownMappedFunction = knownFunctionMap.get(IdentifierText)
            
            if knownMappedFunction is not None:
                IdentifierText = knownMappedFunction
            elif IdentifierText == self.currentClassName \
                    and self.inFunctionDeclaration:
                # constructor function
                IdentifierText = f"new"

            elif (
                self.selfPresent is True
                and IdentifierText in self.attributesInClasses.setdefault(self.currentClassName,set())
                and IdentifierText not in self.currentFunctionParameters
                and self.idFromPrimaryExpression is True
            ):
                IdentifierText = "self." + IdentifierText

            elif IdentifierText==self.currentClassName:
                IdentifierText = f"{self.currentClassName}::new"

            self.rustCode += " " + IdentifierText + " "

        elif ctx.Tilde() is not None:
            self.rustCode += "// Mostly refers to the destructor function implementation... Need to look at how to implement this...\n"
            self.rustCode += " " + ctx.Tilde().getText()
            self.visit(ctx.getChild(1))

        else:
            self.visitChildren(ctx)

    def visitOperatorFunctionId(self, ctx: CPP14Parser.OperatorFunctionIdContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        text = ctx.theOperator().getText()
        if self.isNeg:
            text = self.unOpMap[text][0]
        elif text in self.opConversionMap:
            text = self.opConversionMap[text][0]

        self.rustCode += " " + text + " "


    def visitQualifiedId(self, ctx: CPP14Parser.QualifiedIdContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if self.inFunctionDeclaration is False:
            self.visit(ctx.nestedNameSpecifier())
        if ctx.Template() is not None:
            self.rustCode += " template "
        self.visit(ctx.unqualifiedId())

    def visitParametersAndQualifiers(self, ctx: CPP14Parser.ParametersAndQualifiersContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += " ( "

        if self.isClassFunctionParameters:
            opOverloading = self.functionDeclName in self.opConversionMap
            if opOverloading and \
                    self.opConversionMap[self.functionDeclName][2] != "":
                self.rustCode += "self"
                self.selfPresent = True
                if ctx.parameterDeclarationClause() is not None:
                    self.rustCode += ", "
            elif self.isThisAConstructorCall is not True:
                self.rustCode += "&mut self"
                self.selfPresent = True
                if ctx.parameterDeclarationClause() is not None:
                    self.rustCode += ", "

            self.isClassFunctionParameters = False

        if ctx.parameterDeclarationClause() is not None:
            self.visit(ctx.parameterDeclarationClause())
        self.rustCode += " ) "
        if ctx.cvqualifierseq() is not None:
            self.visit(ctx.cvqualifierseq())
        if ctx.refqualifier() is not None:
            self.visit(ctx.refqualifier())
        if ctx.exceptionSpecification() is not None:
            self.visit(ctx.exceptionSpecification())
        if ctx.attributeSpecifierSeq() is not None:
            self.visit(ctx.attributeSpecifierSeq())

    def visitParameterDeclarationClause(self, ctx: CPP14Parser.ParameterDeclarationClauseContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.visit(ctx.parameterDeclarationList())
        if ctx.Ellipsis() is not None:
            # Attributes walaa scene still not clear
            if ctx.Comma() is not None:
                self.rustCode += ", ..."
            else:
                self.rustCode += "..."

    def visitParameterDeclarationList(self, ctx: CPP14Parser.ParameterDeclarationListContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        expressionVisitor(self, ctx)

    def visitParameterDeclaration(self, ctx: CPP14Parser.ParameterDeclarationContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.attributeSpecifierSeq() is not None:
            self.visit(ctx.attributeSpecifierSeq())
        # for accommodating types:
        self.declIsPointer = False
        curRustCode = self.rustCode
        self.rustCode = ""
        self.inFunctionParameters = True
        if ctx.declarator() is not None:
            parameterName="int " + ctx.declarator().getText()
            arrayName = convert_c_array_signature_to_rust(parameterName)
            if arrayName != []:
                parameterName=arrayName[0][1]
                self.arraySignature = ctx.declarator().getText()
            self.currentFunctionParameters.add(ctx.declarator().getText())
            self.rustCode += "mut "
            self.visit(ctx.declarator())
            self.rustCode += " : "

        elif ctx.abstractDeclarator() is not None:
            self.rustCode += "mut "
            self.currentFunctionParameters.add(
                ctx.abstractDeclarator().getText())
            self.visit(ctx.abstractDeclarator())
            self.rustCode += " : "
        
        
        self.visit(ctx.declSpecifierSeq())

        if self.declIsPointer:
            self.rustCode = self.rustCode.replace('&','')
            self.rustCode = self.rustCode.replace('mut','')
            self.rustCode = self.rustCode.replace('&mut','')
            self.rustCode = self.rustCode.replace(' : ',' :&mut ')

        self.rustCode = curRustCode + self.rustCode
        self.inFunctionParameters = False
        self.declIsPointer = False

        if ctx.Assign() is not None:
            self.rustCode += " = "
            self.visit(ctx.initializerClause())

    def visitAssignmentExpression(self, ctx: CPP14Parser.AssignmentExpressionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        return super().visitAssignmentExpression(ctx)

    def visitConditionalExpression(self, ctx: CPP14Parser.ConditionalExpressionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.Question() is not None:
            self.rustCode += " if "
            self.visit(ctx.logicalOrExpression())
            self.rustCode += " { "
            self.visit(ctx.expression())
            self.rustCode += " } "
            self.rustCode += " else { "
            self.visit(ctx.assignmentExpression())
            self.rustCode += " } "
        else:
            self.visit(ctx.logicalOrExpression())

    def visitAssignmentOperator(self, ctx: CPP14Parser.AssignmentOperatorContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += " " + ctx.getText() + " "

    def visitThrowExpression(self, ctx: CPP14Parser.ThrowExpressionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        # initial assumption
        self.rustCode += "// Need to use third party crates to handle try/catch throw statements\n"
        self.rustCode += "// It is recommended to take advantage of Result enums.\n"
        self.rustCode += " throw "
        if ctx.assignmentExpression() is not None:
            self.visit(ctx.assignmentExpression())

    def visitBraceInitList(self, ctx: CPP14Parser.BracedInitListContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += " { "
        if ctx.initializerList() is not None:
            self.visit(ctx.initializerList())
            if ctx.Comma() is not None:
                self.rustCode += " , "
        self.rustCode += " } "

    def visitInitializerList(self, ctx: CPP14Parser.InitializerListContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        childCount = ctx.getChildCount()
        # if childCount > 1:
        # self.rustCode += "[ "
        for i in range(childCount):
            child = ctx.getChild(i)
            childText = child.getText()
            # if ctx.getChild(i).initializerList() is not None:
            #     self.visit(child.initializerClause())
            if childText == "," or childText == "...":
                self.rustCode += " " + childText
            else:
                if "{" in childText:
                    self.rustCode += "( "
                self.visit(child)
                if "}" in childText:
                    self.rustCode += " ) "
        # if "," in childText:
        # self.rustCode += " ] "
        # return super().visitInitializerList(ctx)

    def visitBlockDeclaration(self, ctx: CPP14Parser.BlockDeclarationContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        return super().visitBlockDeclaration(ctx)

    def simpleDeclarationUtil(self, ctx: CPP14Parser.SelectionStatementContext, initDeclarator: CPP14Parser.InitDeclaratorContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if (initDeclarator.declarator().pointerDeclarator().pointerOperator(0) is not None):
            self.isPointerDeclaration = True
        
        if ctx.declSpecifierSeq() is not None:
            self.isSimpleDecl = True
            if ctx.declSpecifierSeq().declSpecifier(0).getText() == "const":
                self.rustCode += "const"
            else:
                self.rustCode += "let mut "

            if ctx.declSpecifierSeq().getText().startswith("stack"):
                self.stlDataTypeMap[initDeclarator.declarator().getText()] = "stack"
            elif ctx.declSpecifierSeq().getText().startswith("map"):
                self.stlDataTypeMap[initDeclarator.declarator().getText()] = "map"
            elif ctx.declSpecifierSeq().getText().startswith("unordered_map"):
                self.stlDataTypeMap[initDeclarator.declarator().getText()] = "unordered_map"

            if ctx.declSpecifierSeq().getText().startswith("vector"):
                self.stlDataTypeMap[initDeclarator.declarator().getText()] = "vector"
            
            if ctx.declSpecifierSeq().getText().startswith("queue"):
                self.stlDataTypeMap[initDeclarator.declarator().getText()] = "deque"

            if ctx.declSpecifierSeq().getText().startswith("deque"):
                self.stlDataTypeMap[initDeclarator.declarator().getText()] = "deque"
            
            if ctx.declSpecifierSeq().getText().startswith("set"):
                self.stlDataTypeMap[initDeclarator.declarator().getText()] = "set"

            if ctx.declSpecifierSeq().getText().startswith("unordered_set"):
                self.stlDataTypeMap[initDeclarator.declarator().getText()] = "unordered_set"

            if ctx.declSpecifierSeq().getText().startswith("string"):
                self.stlDataTypeMap[initDeclarator.declarator().getText()] = "string"
        
        if self.stlDataTypeMap.get(initDeclarator.declarator().getText()) == "vector":
            self.isVectorDeclaration = True
        elif self.stlDataTypeMap.get(initDeclarator.declarator().getText()) == "stack":
            self.isStackDeclaration = True
        elif self.stlDataTypeMap.get(initDeclarator.declarator().getText()) == "map":
            self.isMapDeclaration = True
        elif self.stlDataTypeMap.get(initDeclarator.declarator().getText()) == "unordered_map":
            self.isUnMapDeclaration = True
        elif self.stlDataTypeMap.get(initDeclarator.declarator().getText()) == "deque" \
                or self.stlDataTypeMap.get(initDeclarator.declarator().getText()) == 'queue':
            self.isDequeDeclaration = True
        elif self.stlDataTypeMap.get(initDeclarator.declarator().getText()) == "string":
            self.isStringDeclaration = True
        elif self.stlDataTypeMap.get(initDeclarator.declarator().getText()) == "set":
            self.isSetDeclaration = True
        elif self.stlDataTypeMap.get(initDeclarator.declarator().getText()) == "unordered_set":
            self.isUnorderedSetDeclaration = True
            
        self.visit(initDeclarator.declarator())

        if ctx.declSpecifierSeq() is not None:
            if (ctx.declSpecifierSeq().getText() in self.classSet) \
                and (initDeclarator.initializer() is None \
                or initDeclarator.initializer().LeftParen()):
                self.rustCode += " = "
                self.visit(ctx.declSpecifierSeq())

                self.rustCode += "::new"
                if initDeclarator.initializer() is None:
                    self.rustCode += "()"
            elif self.isVectorDeclaration:
                if initDeclarator.initializer() is None:
                    self.rustCode += " = vector::new() "
            elif self.isStackDeclaration:
                if initDeclarator.initializer() is None:
                    self.rustCode += " = stack::new() "
            elif self.isMapDeclaration:
                if initDeclarator.initializer() is None:
                    self.rustCode += " = map::new() "
            elif self.isUnMapDeclaration:
                if initDeclarator.initializer() is None:
                    self.rustCode += " = unordered_map::new() "

            elif self.isDequeDeclaration:
                if initDeclarator.initializer() is None:
                    self.rustCode += " = deque::new() "
            elif self.isStringDeclaration:
                if initDeclarator.initializer() is None:
                    self.rustCode += " = string::new() "
            elif self.isSetDeclaration:
                if initDeclarator.initializer() is None:
                    self.rustCode += " = set::new() "
            elif self.isUnorderedSetDeclaration:
                if initDeclarator.initializer() is None:
                    self.rustCode += " = unordered_set::new() "
            else:
                if ctx.declSpecifierSeq().getText() != "auto":
                    self.rustCode += ":" # [FUTURE ISSUES 1]
                self.rustCode += self.arraySizeDecl[0] # array declarations
                self.visit(ctx.declSpecifierSeq())
                self.rustCode += self.arraySizeDecl[1] # array declarations
            # naive attempt to improve quality

        if initDeclarator.initializer() is not None:
            self.isSimpleAssignment = True
            self.visit(initDeclarator.initializer())
        
        if  self.isVectorDeclaration or \
                self.isStackDeclaration or \
                self.isDequeDeclaration or \
                self.isSetDeclaration or \
                self.isUnorderedSetDeclaration or\
                self.isStringDeclaration:
            self.rustCode += ".clone()"
        
        if "[" in ctx.getText():
            self.leftHandSideDataType = None

        if self.isSimpleAssignment and self.leftHandSideDataType is not None:
            if self.isPointerDeclaration:
                self.rustCode += "as &mut "
            else:
                self.rustCode += " as "
            self.rustCode += self.leftHandSideDataType
            self.leftHandSideDataType = None
        self.isSimpleAssignment = False
        self.isSimpleDecl = False
        self.arraySizeDecl = ["",""]
        self.rustCode += ";\n"
        self.isPointerDeclaration = False

    def visitSimpleDeclaration(self, ctx: CPP14Parser.SimpleDeclarationContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        # for attribute specifiers currently not handling
        
        if ctx.attributeSpecifierSeq() is not None:
            self.visitChildren(ctx)
            self.rustCode += ";\n"

        # for normal declaration
        elif ctx.getChildCount() != 0:

            if singleParameterFunctionHandling(ctx):
                self.visitChildren(ctx)
                self.rustCode += ";\n"

            elif ctx.initDeclaratorList() is not None:
                declaratorList = ctx.initDeclaratorList()
                initDeclarator = declaratorList.getChild(0)
                self.simpleDeclarationUtil(ctx, initDeclarator)

                childCount = declaratorList.getChildCount()
                if childCount > 1:
                    for i in range(1, childCount, 2):
                        initDeclarator = declaratorList.getChild(i+1)
                        self.simpleDeclarationUtil(ctx, initDeclarator)
                
                self.isVectorDeclaration = False
                self.isStackDeclaration = False
                self.isMapDeclaration = False
                self.isUnMapDeclaration = False
                self.isDequeDeclaration = False
                self.isSetDeclaration = False
                self.isStringDeclaration = False
                self.isUnorderedSetDeclaration = False

            elif ctx.declSpecifierSeq() is not None:
                self.visitChildren(ctx)

        else:
            self.rustCode += ";\n"

    def visitInitDeclaratorList(self, ctx: CPP14Parser.InitDeclaratorListContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        expressionVisitor(self, ctx)

    def visitInitDeclarator(self, ctx: CPP14Parser.InitDeclaratorContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        return super().visitInitDeclarator(ctx)
    
    def visitInitializer(self, ctx:CPP14Parser.InitializerContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        return self.visitChildren(ctx)

    def visitTrailingReturnType(self, ctx: CPP14Parser.TrailingReturnTypeContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.trailingTypeSpecifierSeq().getText() != "auto":
            self.rustCode += " -> "
            self.visit(ctx.trailingTypeSpecifierSeq())
        if ctx.abstractDeclarator() is not None:
            self.visit(ctx.abstractDeclarator())

    def visitAsmDefinition(self, ctx: CPP14Parser.AsmDefinitionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += "// This is ASM invocation please refer to supported rust methods for the ASM invocation. https://doc.rust-lang.org/reference/inline-assembly.html .\n"
        self.rustCode += 'unsafe { asm!( ' + \
            ctx.StringLiteral().getText() + ' ) }\n'

    def visitNamespaceAliasDefinitions(self, ctx: CPP14Parser.NamespaceAliasDefinitionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += "// Namespaces are not yet supported in this transpiler... Copying as it is\n"
        self.rustCode += ctx.getText() + "\n"

    def visitUsingDeclaration(self, ctx: CPP14Parser.UsingDeclarationContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += "// Using Declarations are not yet supported in this transpiler... Copying as it is\n"
        self.rustCode += " using "
        self.rustCode += " " + ctx.getChild(1).getText() + " "
        self.visit(ctx.unqualifiedId())
        self.rustCode += ";\n"

    def visitUsingDirective(self, ctx: CPP14Parser.UsingDirectiveContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.attributeSpecifierSeq() is not None:
            self.visit(ctx.attributeSpecifierSeq())
        self.rustCode += "use "
        if ctx.nestedNameSpecifier() is not None:
            self.visit(ctx.nestedNameSpecifier())
        self.visit(ctx.namespaceName())
        self.rustCode += ";\n"

    def visitStaticAssertDeclaration(self, ctx: CPP14Parser.StaticAssertDeclarationContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += 'assert!('
        self.visit(ctx.constantExpression())
        self.rustCode += ', ' + ctx.StringLiteral().getText() + ');\n'

    def visitAliasDeclaration(self, ctx: CPP14Parser.AliasDeclarationContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += "// Using Namespace Alias are not yet supported in this transpiler... Copying as it is\n"
        self.rustCode += ctx.getText() + "\n"

    def visitOpaqueEnumDeclaration(self, ctx: CPP14Parser.OpaqueEnumDeclarationContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.visit(ctx.enumkey())
        if ctx.attributeSpecifierSeq() is not None:
            self.visit(ctx.attributeSpecifierSeq())
        self.rustCode += " " + ctx.Identifier().getText() + " "
        if ctx.enumbase() is not None:
            self.visit(ctx.enumbase())
        self.rustCode += ";\n"

    def visitEnumKey(self, ctx: CPP14Parser.EnumkeyContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += "enum"
        if ctx.Class() is None and ctx.Struct() is None:
            self.rustCode += "// Rust does not support unscoped enum types, make sure you add a scope to your enum\n"

    def visitEnumbase(self, ctx: CPP14Parser.EnumbaseContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        None
        # self.rustCode += ":"
        # self.visit(ctx.typeSpecifierSeq())

    def visitFunctionDefinition(self, ctx: CPP14Parser.FunctionDefinitionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        usesScopeResolution: bool = False
        self.fnRtnReference = False

        self.isNeg = False
        functionName = getFunctionName(self,ctx)
        self.functionDeclName = functionName
        returnType = getFunctionReturnType(ctx)
        if functionName is None:
            functionName = ""

        oldCurrentClassName = ""
        opOverloading = functionName in self.opConversionMap
        if opOverloading:
            self.isNeg = isOpOverloadedUnary(ctx)
            if self.isNeg and functionName in self.unOpMap:
                traitName = self.unOpMap[functionName][1]
                traitType = self.unOpMap[functionName][2]
                functionName = self.unOpMap[functionName][0]
            else:
                self.isNeg = False
                traitName = self.opConversionMap[functionName][1]
                traitType = self.opConversionMap[functionName][2]
                functionName = self.opConversionMap[functionName][0]
            returnType = traitType
            if returnType == "Output":
                returnType = "Self::Output"
            elif returnType == "Target":
                returnType = "&mut Self::Target"
            
            if traitName == "":
                return

        
        scopedParent = getFunctionScopedParentName(ctx)
        if scopedParent is not None:
            # function is defined outside the class
            usesScopeResolution = True
            self.currentClassName = scopedParent.split("<")[0]
            self.isClassFunctionParameters = True
            if opOverloading:
                self.rustCode += "impl" + self.currentTemplateParameters + f" {traitName}<&{self.currentClassName}> for " + scopedParent + "{\n"
                if traitType == "Output":
                    self.rustCode += "type Output = Self;\n"
            else:
                self.rustCode += "impl" + self.currentTemplateParameters + " " + scopedParent + "{\n" 
            self.isThisATemplateDeclaration = False
        elif opOverloading:
            # operator overloading function is either defined inside a class or is a standalone overloading
            if self.implPresent:
                self.rustCode += "\n}\n"
            self.rustCode += f"impl {traitName}<&{self.currentClassName}> for {self.currentClassName}{self.currentTemplateParameters}" + "{\n"

            if traitType == "Output":
                self.rustCode += "type Output = Self;\n"

        if self.namespaceDepth > 0 or self.isFnPublic and opOverloading is False:
            self.rustCode += "pub fn "
        else:
            self.rustCode += "fn "

        if ctx.declSpecifierSeq() is None and functionName != "" and functionName == self.currentClassName:
            self.isThisAConstructorCall = True
            returnType = self.currentClassName
        elif scopedParent is not None:
            parent_name = self.currentClassName # in case of templated parents
            return_type_name = returnType.split("<")[0]
            if return_type_name is not None and return_type_name == parent_name and parent_name == functionName:
                self.isThisAConstructorCall = True


        # adds functionName to the output
        self.inFunctionDeclaration = True
        self.visit(ctx.declarator())
        self.inFunctionDeclaration = False

        self.isNeg = False
        # adds return type to the output
        if opOverloading: 
            # Add return type based on operator overloaded
            if returnType != "":
                self.rustCode += f" -> {returnType}"
        else:
            referenceSymbol = ""
            if self.fnRtnReference is True:
                referenceSymbol = "&"
            if ctx.attributeSpecifierSeq() is not None:
                self.visit(ctx.attributeSpecifierSeq())

            if ctx.declSpecifierSeq() is not None and functionName != "main" and not self.isThisAConstructorCall:
                if returnType is not None and returnType != "void":
                    self.rustCode += " -> " + referenceSymbol
                self.visit(ctx.declSpecifierSeq())

            elif self.isThisAConstructorCall:
                self.rustCode += " -> " + self.currentClassName + self.currentTemplateParameters + " "

            if ctx.virtualSpecifierSeq() is not None:
                self.visit(ctx.virtualSpecifierSeq())

        self.fnRtnReference = False

        # adds function body to the output
        self.functionDeclName = ""
        self.visit(ctx.functionBody())

        if self.isThisAConstructorCall:
            codeWithoutClosingBrace = self.rustCode[:self.rustCode.rfind("}")]
            structComment = (
                "\n/*\n"
                + "\tThis is a constructor method.\n"
                + "\tPlease appropriate members to the struct constructor as per your logic.\n"
                + "\tCurrently the constructor returns a struct with all the defaults for the data types in the struct.\n"
                + "*/\n"
            )
            structReturnCode = structComment + \
                functionName + "{..Default::default()}\n"
            self.rustCode = codeWithoutClosingBrace + structReturnCode + "}\n"
            self.isThisAConstructorCall = False

        if usesScopeResolution or opOverloading :
            self.rustCode += "}\n" 
            if self.implPresent:
                self.rustCode += f"impl {self.currentClassName}" + "{\n"
            self.isClassFunctionParameters = False

        self.selfPresent = False

    def visitDeclSpecifierSeq(self, ctx: CPP14Parser.DeclSpecifierSeqContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        # TYPES ARE HANDLED HERE
        signedNess = True
        lengthSpecifier = None
        dataType = None
        isAuto = False
        self.Std = None
        for i in ctx.declSpecifier():
            if i.getText() == "auto":
                dataType = "auto"
                isAuto = True
            elif i.getText() == "unsigned":
                signedNess = False
            elif i.getText() in ["int","float", "double"]:
                dataType = i.getText()
            elif i.getText() in ["short", "long", "longlong"]:
                dataType = "int"
                if i.getText() == "short":
                    lengthSpecifier = "16"
                elif i.getText() in ["long", "longlong"]:
                    lengthSpecifier = "64"
            elif i.getText() == "void" and self.declIsPointer:
                dataType = "void*"
            elif i.getText() in ["int8_t", "int16_t", "int32_t", "int64_t", "uint8_t", "uint16_t", "uint32_t", "uint64_t", "size_t", "bool", "char"]:
               dataType=i.getText()
               self.Std = i.getText()
        
        if isAuto or dataType is None:
            self.rustCode += " "
            return super().visitDeclSpecifierSeq(ctx)
        # self.rustCode += ": "
        rustDataType = ""
        if self.declIsPointer and self.unsafeEnabled:
            self.rustCode += "&mut "
        if self.Std is not None:
            stdConvert = {
                "int8_t": "i8",
                "int16_t": "i16",
                "int32_t": "i32",
                "int64_t": "i64",
                "uint8_t": "u8",
                "uint16_t": "u16",
                "uint32_t": "u32",
                "uint64_t": "u64",
                "size_t": "usize",
                "bool": "bool",
                "char": "char"
            }
            # self.rustCode += stdConvert[Std]
            rustDataType += stdConvert[self.Std]
        else:
            if signedNess is False:
                # self.rustCode += "u"
                rustDataType += "u"
            else:
                if dataType in ["int"]:
                    # self.rustCode += "i"
                    rustDataType += "i"
                elif dataType == "void*":
                    rustDataType += "libc::c_void"
                    self.usesLibC = True
                elif dataType != "":
                    # self.rustCode += "f"
                    rustDataType += "f"
            if lengthSpecifier is not None:
                # self.rustCode += lengthSpecifier
                rustDataType += lengthSpecifier
            else:
                if dataType == "int":
                    # self.rustCode += "32"
                    rustDataType += "32"
                elif dataType == "float":
                    # self.rustCode += "32"
                    rustDataType += "32"
                elif dataType == "double":
                    # self.rustCode += "64"
                    rustDataType += "64"

        if self.arraySignature != "" and self.inFunctionParameters is True:
            rustDataType = rustDataType + " " + self.arraySignature
            self.arraySignature = ""
            rustDataType = convert_c_array_signature_to_rust(rustDataType)[0][2]

        self.rustCode += rustDataType
        self.leftHandSideDataType = rustDataType

        # arnav
        return super().visitDeclSpecifierSeq(ctx)

    def visitDeclSpecifier(self, ctx: CPP14Parser.DeclSpecifierContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        # self.rustCode += "// Decl Specifiers need time\n"
        if ctx.Friend() is not None or ctx.Typedef() is not None or ctx.Constexpr() is not None:
            self.rustCode += " " + ctx.getText() + " "
        else:
            self.visitChildren(ctx)

    def visitStorageClassSpecifier(self, ctx: CPP14Parser.StorageClassSpecifierContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += " " + ctx.getText() + " "

    def visitFunctionSpecifier(self, ctx: CPP14Parser.FunctionSpecifierContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += " " + ctx.getText() + " "

    def visitFunctionBody(self, ctx: CPP14Parser.FunctionBodyContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.compoundStatement() is not None:
            if ctx.constructorInitializer() is not None:

                self.rustCode += "// Handling constructor initializer\n"

                self.rustCode += "{\n"

                if self.currentClassName != "":
                    self.rustCode += self.currentClassName + " "

                self.rustCode += "{\n"

                self.visit(ctx.constructorInitializer().memInitializerList())

                self.rustCode += "};\n"

                if ctx.compoundStatement().statementSeq() is not None:
                    self.visit(ctx.compoundStatement().statementSeq())

                self.rustCode += "}\n"

            else:
                self.visit(ctx.compoundStatement())

        elif ctx.functionTryBlock() is not None:
            self.visit(ctx.functionTryBlock())

        else:
            self.rustCode += "// I've no clue what control of defaults: default and delete is about...\n"
            self.rustCode += "= " + ctx.getChild(1).getText() + " ;"

    # def visitConstructorInitializer(self, ctx: CPP14Parser.ConstructorInitializerContext):

    def visitCompoundStatement(self, ctx: CPP14Parser.CompoundStatementContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += "{ \n"
        if ctx.statementSeq() is not None:
            self.visit(ctx.statementSeq())
        self.rustCode += "} \n"

    def visitStatementSeq(self, ctx: CPP14Parser.StatementSeqContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        openBrace = False
        if self.switchEval is True:
            childCount = ctx.getChildCount()
            for i in range(childCount):
                if ctx.getChild(i).labeledStatement() is not None:
                    if openBrace:
                        self.rustCode += "},\n"
                        openBrace = False

                    cntx = ctx.getChild(i).labeledStatement()

                    if cntx.Case() is not None:
                        if cntx.attributeSpecifierSeq() is not None:
                            self.visit(cntx.attributeSpecifierSeq())

                        self.visit(cntx.constantExpression())
                        self.rustCode += "=> "

                        self.rustCode += "{\n"
                        openBrace = True

                        self.isSwitchStatementCaseBeingEvaluated = True
                        self.visit(cntx.statement())

                    elif cntx.Default() is not None:
                        if cntx.attributeSpecifierSeq() is not None:
                            self.visit(cntx.attributeSpecifierSeq())

                        self.rustCode += "_=> "
                        self.rustCode += "{\n"
                        openBrace = True

                        self.isSwitchStatementCaseBeingEvaluated = True
                        self.visit(cntx.statement())

                    else:
                        self.visit(ctx.getChild(i))

                else:
                    self.visit(ctx.getChild(i))

            if openBrace:
                self.rustCode += "},\n"
                openBrace = False

        else:
            return super().visitStatementSeq(ctx)

    def visitStatement(self, ctx: CPP14Parser.StatementContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        return super().visitStatement(ctx)

    def visitLabeledStatement(self, ctx: CPP14Parser.LabeledStatementContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.attributeSpecifierSeq() is not None:
            self.visit(ctx.attributeSpecifierSeq())

        if ctx.Identifier() is not None:
            self.rustCode += "'" + ctx.Identifier().getText() + ": "

        elif ctx.Case() is not None:
            self.visit(ctx.constantExpression())
            self.rustCode += "=> "
            self.isSwitchStatementCaseBeingEvaluated = True

        elif ctx.Default is not None:
            self.rustCode += "_=> "

        self.visit(ctx.statement())

    def visitDeclarationStatement(self, ctx: CPP14Parser.DeclarationStatementContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        return super().visitDeclarationStatement(ctx)

    def visitExpressionStatement(self, ctx: CPP14Parser.ExpressionStatementContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.expression() is not None:
            self.visit(ctx.expression())
        self.rustCode += ";\n"

    def visitSelectionStatement(self, ctx: CPP14Parser.SelectionStatementContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.If() is not None:
            self.rustCode += " if "
            self.visit(ctx.condition())
            self.statementBlockVisitor(ctx.statement(0))

            if ctx.Else() is not None:
                self.rustCode += " else "
                if ctx.statement(1).compoundStatement() is None \
                    and (ctx.statement(1).selectionStatement() is None \
                    or (ctx.statement(1).selectionStatement() is not None and ctx.statement(1).selectionStatement().If() is None)):
                    self.rustCode += "{\n"
                    self.visit(ctx.statement(1))
                    self.rustCode += "}\n"
                else:
                    self.visit(ctx.statement(1))
        # Switch case
        else:
            self.rustCode += " match "
            self.visit(ctx.condition())
            self.switchEval = True
            self.statementBlockVisitor(ctx.statement(0))
            self.switchEval = False

    def visitIterationStatement(self, ctx: CPP14Parser.IterationStatementContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        # While loop
        if ctx.Do() is None and ctx.While() is not None:
            self.rustCode += " while "
            self.visit(ctx.condition())
            self.statementBlockVisitor(ctx.statement())

        # Do while loop
        elif ctx.Do() is not None:
            self.rustCode += "loop {\n"
            self.statementBlockVisitor(ctx.statement())
            if ctx.statement().compoundStatement() is None:
                self.visit(ctx.statement())
            elif ctx.statement().compoundStatement().statementSeq() is not None:
                self.visit(
                    ctx.statement().compoundStatement().statementSeq())
            self.rustCode += "if !"
            self.visit(ctx.expression())
            self.rustCode += "{ break; }\n"
            self.rustCode += "}\n"

        # converting for loops to while loops in rust
        else:
            if ctx.forInitStatement() is not None:
                self.visit(ctx.forInitStatement())
                self.rustCode += "while "

                if ctx.condition() is not None:
                    self.visit(ctx.condition())

                if ctx.expression() is not None:
                    self.rustCode += "{\n"
                    if ctx.statement().compoundStatement() is None:
                        self.visit(ctx.statement())
                    elif ctx.statement().compoundStatement().statementSeq() is not None:
                        self.visit(
                            ctx.statement().compoundStatement().statementSeq())
                    self.visit(ctx.expression())
                    self.rustCode += ";"
                    self.rustCode += "}\n"
                else:
                    self.visit(ctx.statement())

            else:
                self.rustCode += "for "
                self.visit(ctx.forRangeDeclaration())
                self.rustCode += " in "
                self.visit(ctx.forRangeInitializer())
                self.statementBlockVisitor(ctx.statement())

    def visitForRangeDeclaration(self, ctx: CPP14Parser.ForRangeDeclarationContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        self.visit(ctx.declarator())

    def visitForRangeInitializer(self, ctx:CPP14Parser.ForRangeInitializerContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        self.visitChildren(ctx)
        self.rustCode += ".iter() "

    def visitJumpStatement(self, ctx: CPP14Parser.JumpStatementContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.Goto() is not None:
            self.rustCode += "// Goto Statements are not supported in Rust, please refer to best practices to remove goto statements from the source code\n"
            self.rustCode += "goto " + ctx.Identifier() + ";\n"

        elif ctx.Break() is not None:
            if self.isSwitchStatementCaseBeingEvaluated is False:
                self.rustCode += " break;\n "
            else:
                # do nothing
                self.isSwitchStatementCaseBeingEvaluated = False

        elif ctx.Continue() is not None:
            self.rustCode += " continue;\n "

        else:
            self.rustCode += " return "
            if ctx.getChildCount() > 1:
                self.visit(ctx.getChild(1))
            self.rustCode += ";\n"

    def visitTryBlock(self, ctx: CPP14Parser.TryBlockContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += "// There are no try-catch blocks in rust, please code tweak code as per rust standards: https://stackoverflow.com/questions/55755552/what-is-the-rust-equivalent-to-a-try-catch-statement\n"
        self.rustCode += "try "
        self.visitChildren(ctx)

    def visitHandlerSeq(self, ctx: CPP14Parser.HandlerSeqContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        return super().visitHandlerSeq(ctx)

    def visitHandler(self, ctx: CPP14Parser.HandlerContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += "catch ("
        self.visit(ctx.exceptionDeclaration())
        self.rustCode += ") \n"
        self.visit(ctx.compoundStatement())

    def visitExceptionDeclaration(self, ctx: CPP14Parser.ExceptionDeclarationContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.Ellipsis() is not None:
            self.rustCode += "..."
        else:
            self.visitChildren(ctx)

    def visitEmptyDeclaration(self, ctx: CPP14Parser.EmptyDeclarationContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += ";\n"

    def visitTemplateDeclaration(self, ctx: CPP14Parser.TemplateDeclarationContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        # self.rustCode += "// Templates are not yet fully supported for conversion\n"
        self.isThisATemplateDeclaration = True
        self.currentTemplateParameters += "< "
        self.visit(ctx.templateparameterList())
        self.currentTemplateParameters += " > "

        if ctx.declaration().functionDefinition() is not None:
            self.visit(ctx.declaration().functionDefinition())
        else: # other template types
            self.visit(ctx.declaration())

        self.isThisATemplateDeclaration = False
        self.currentTemplateParameters = ""

    def visitTemplateparameterList(self, ctx: CPP14Parser.TemplateparameterListContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        # to consider, recursive template definitions
        self.visit(ctx.getChild(0))
        childCount = ctx.getChildCount()
        if childCount > 1:
            for i in range(1, childCount, 2):
                self.currentTemplateParameters += " " + ctx.getChild(i).getText() + " "
                self.visit(ctx.getChild(i + 1))

    def visitTemplateParameter(self, ctx: CPP14Parser.TemplateParameterContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.typeParameter() is not None: 
            self.visit(ctx.typeParameter())
        else: # parameter declaration
            None
            # not handled yet
            # return super().visitTemplateParameter(ctx)

    def visitTypeParameter(self, ctx: CPP14Parser.TypeParameterContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.Typename_() is None:
            self.rustCode += "\n Generics only allow for types as parameters\n"
        self.currentTemplateParameters += ctx.Identifier().getText() 
        # return super().visitTypeParameter(ctx)

    def visitExplicitInstantiation(self, ctx: CPP14Parser.ExplicitInstantiationContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        # self.rustCode += "// Templates are not yet supported for conversion\n"
        if ctx.Extern() is not None:
            self.rustCode += "extern "

        self.rustCode += "template "
        self.visit(ctx.declaration())

    def visitExplicitSpecialization(self, ctx: CPP14Parser.ExplicitSpecializationContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        # self.rustCode += "// Templates are not yet supported for conversion\n"
        self.rustCode += "template <>"
        self.visit(ctx.declaration())

    def visitLinkageSpecification(self, ctx: CPP14Parser.LinkageSpecificationContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += "extern " + ctx.StringLiteral().getText()

        if ctx.LeftBrace() is not None:
            self.rustCode += "{ \n"
            if ctx.declarationseq() is not None:
                self.visit(ctx.declarationseq())
            self.rustCode += "} \n"

        else:
            self.visit(ctx.declaration())

    def visitNamespaceDefinition(self, ctx: CPP14Parser.NamespaceDefinitionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.rustCode += "// Variables in namespaces are partially supported....\n"
        if ctx.Inline() is not None:
            self.rustCode += "#[inline]\n"
        if self.namespaceDepth > 0:
            self.rustCode += "pub mod "
        else:
            self.rustCode += " mod "
        self.namespaceDepth += 1

        if ctx.Identifier() is not None:
            self.rustCode += " " + ctx.Identifier().getText() + " "
        elif ctx.originalNamespaceName() is not None:
            self.rustCode += " " + ctx.originalNamespaceName().getText() + " "

        self.rustCode += "{\n"
        # if ctx.namespaceBody() is not None:
        #     self.visit(ctx.namespaceBody())
        self.visitChildren(ctx)
        self.rustCode += "}\n"
        self.namespaceDepth -= 1

    def visitAttributeDeclaration(self, ctx: CPP14Parser.AttributeDeclarationContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.visitChildren(ctx)
        self.rustCode += ";\n"

    def visitTheOperator(self, ctx: CPP14Parser.TheOperatorContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.New() is not None:
            self.rustCode += " " + ctx.getText() + " "
            self.rustCode += "// new operator in not allowed in Rust\n"

        elif ctx.Delete() is not None:
            self.rustCode += "// delete operator in not allowed in Rust\n"
            self.rustCode += " " + ctx.getText() + " "

        elif ctx.PlusPlus() is not None:
            self.rustCode += " += 1 "
            self.rustCode += "// ++ is not supported in Rust\n"

        elif ctx.MinusMinus() is not None:
            self.rustCode += " -= 1 "
            self.rustCode += "// ++ is not supported in Rust\n"

        else:
            self.rustCode += " " + ctx.getText() + " "

    def visitInitializer(self, ctx: CPP14Parser.InitializerContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.LeftParen() is not None:
            self.rustCode += "( "
            self.visit(ctx.expressionList())
            self.rustCode += " )"

        else:
            self.visit(ctx.braceOrEqualInitializer())

    def visitBraceOrEqualInitializer(self, ctx: CPP14Parser.BraceOrEqualInitializerContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if "{" in ctx.getText():
            self.hasBracket = True
        self.rustCode += " = "
        if self.hasBracket:
            if self.isVectorDeclaration:
                self.rustCode += "vector!["
            elif self.isMapDeclaration:
                self.rustCode += "map!["
            elif self.isUnMapDeclaration:
                self.rustCode += "unordered_map!["
            elif self.isDequeDeclaration:
                self.rustCode += "deque!["
            elif self.isSetDeclaration:
                self.rustCode += "set!["
            elif self.isUnorderedSetDeclaration:
                self.rustCode += "unordered_set!["
            elif self.isStringDeclaration:
                self.rustCode += "string!["
            else:
                self.rustCode += " [ "
        self.visit(ctx.initializerClause())
        if self.hasBracket:
            self.rustCode += " ]"
        self.hasBracket = False

    def visitExpressionList(self, ctx: CPP14Parser.ExpressionListContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        return super().visitExpressionList(ctx)

    def visitCondition(self, ctx: CPP14Parser.ConditionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.expression() is not None:
            self.visit(ctx.expression())

        else:
            if ctx.attributeSpecifierSeq() is not None:
                self.visit(ctx.attributeSpecifierSeq())

            self.visit(ctx.declSpecifierSeq())
            self.visit(ctx.declarator())

            if ctx.Assign() is not None:
                self.rustCode += " = "
                self.visit(ctx.initializerClause())
            else:
                self.visit(ctx.bracedInitList())

    def visitUnaryExpression(self, ctx: CPP14Parser.UnaryExpressionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.postfixExpression() is not None:
            self.visit(ctx.postfixExpression())

        elif ctx.noExceptExpression() is not None:
            self.visit(ctx.noExceptExpression())

        elif ctx.newExpression() is not None:
            self.visit(ctx.newExpression())

        elif ctx.deleteExpression() is not None:
            self.visit(ctx.deleteExpression())

        elif ctx.Alignof() is not None:
            self.rustCode += "mem::size_of::<"
            self.visit(ctx.theTypeId())
            self.rustCode += ">()"

        elif ctx.Sizeof() is not None and ctx.unaryExpression() is not None:
            self.rustCode += "mem::size_of_val("
            self.visit(ctx.unaryExpression())
            self.rustCode += ")"

        elif ctx.Sizeof() is not None and ctx.theTypeId() is not None:
            self.rustCode += "mem::size_of_val("
            self.visit(ctx.theTypeId())
            self.rustCode += ")"

        elif ctx.Sizeof() is not None and ctx.Identifier() is not None:
            self.rustCode += "mem::size_of_val("
            self.visit(ctx.Identifier())
            self.rustCode += ")"

        elif ctx.unaryExpression() is not None:
            if ctx.unaryOperator() is not None:
                self.visit(ctx.unaryOperator())
                self.visit(ctx.unaryExpression())

            elif ctx.PlusPlus() is not None:
                self.visit(ctx.unaryExpression())
                self.rustCode += "+= 1"

            else:
                self.visit(ctx.unaryExpression())
                self.rustCode += "-= 1"

    def visitUnaryOperator(self, ctx: CPP14Parser.UnaryOperatorContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.Tilde() is not None:
            self.rustCode += "// Delete Operator not supported\n"
            self.rustCode += "~ "

        else:
            self.rustCode += ctx.getText() + " "
            if self.isPointerDeclaration:
                self.rustCode += " mut "

    def visitPostfixExpression(self, ctx: CPP14Parser.PostfixExpressionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.primaryExpression() is not None:
            self.visit(ctx.primaryExpression())

        elif ctx.LeftBracket() is not None:
            self.visit(ctx.postfixExpression())
            self.rustCode += "["
            self.visit(ctx.getChild(2))
            self.rustCode += "as usize]"

        elif ctx.LeftParen() is not None and ctx.postfixExpression() is not None:
            self.visit(ctx.postfixExpression())
            self.rustCode += "("
            # Passing mutable reference for swap in vector
            if ctx.postfixExpression().idExpression() is not None \
                    and ctx.postfixExpression().idExpression().getText() == "swap":
                self.rustCode += "&mut "
            if ctx.expressionList() is not None:
                self.visit(ctx.expressionList())
            # Handling Default Second for resize function
            if ctx.postfixExpression().idExpression() is not None \
                    and ctx.postfixExpression().idExpression().getText() == "resize" \
                    and len(ctx.expressionList().initializerList().Comma()) == 0:
                if self.stlDataTypeMap.get(ctx.postfixExpression().postfixExpression().getText()) == 'string':
                    self.rustCode += ", '0'"
                else:
                    self.rustCode += ", 0"

            self.rustCode += ")"

        elif ctx.PlusPlus() is not None:
            self.visit(ctx.postfixExpression())
            self.rustCode += "+=1 "

        elif ctx.MinusMinus() is not None:
            self.visit(ctx.postfixExpression())
            self.rustCode += "-=1 "

        elif ctx.Dot() is not None or ctx.Arrow() is not None:
            self.visit(ctx.postfixExpression())
            self.rustCode += "."
            if ctx.idExpression() is not None:
                self.visit(ctx.idExpression())
                # if ctx.Template() is not None:
                #     self.rustCode += "//Templates not supported\n"
            else:
                self.visit(ctx.pseudoDestructorName())

        elif ctx.simpleTypeSpecifier() is not None or ctx.typeNameSpecifier() is not None:

            if ctx.LeftParen() is not None:
                self.rustCode += "("
                if ctx.expressionList() is not None:
                    self.visit(ctx.expressionList())
                self.rustCode += ")"

            else:
                self.visit(ctx.bracedInitList())

            self.visit(ctx.getChild(0))

        elif ctx.Less() is not None:
            self.rustCode += " ( "
            self.visit(ctx.expression())
            self.rustCode += " ) "
            self.rustCode += " as "
            self.visit(ctx.theTypeId())

        else:
            self.rustCode += " " + ctx.getText() + " "

    def visitPrimaryExpression(self, ctx: CPP14Parser.PrimaryExpressionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.LeftParen() is not None:
            self.rustCode += "("
            self.visit(ctx.expression())
            self.rustCode += ")"

        elif ctx.This() is not None:
            # There is not reference to this as in rust as such
            # putting self as of now
            self.rustCode += "self"
            self.selfPresent = True

        elif ctx.lambdaExpression() is not None:
            # Convert cpp lambda expressions to rust closures
            self.visit(ctx.lambdaExpression())
        elif ctx.idExpression() is not None:
            if ctx.idExpression().unqualifiedId() is not None:
                self.idFromPrimaryExpression = True
            self.visitChildren(ctx)
            self.idFromPrimaryExpression = False
        else:
            self.visitChildren(ctx)

    def visitLambdaExpression(self, ctx: CPP14Parser.LambdaExpressionContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.isSimpleAssignment = False
        self.visit(ctx.lambdaIntroducer())
        # closure parameters
        if ctx.lambdaDeclarator() is not None:
            self.visit(ctx.lambdaDeclarator())
        else:
            self.rustCode += "||"
        # the closure body
        self.visit(ctx.compoundStatement())

    def visitLambdaDeclarator(self, ctx: CPP14Parser.LambdaDeclaratorContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.lambdaCapture() is not None:
            self.visit(ctx.lambdaCapture())

    def visitLambdaCapture(self, ctx: CPP14Parser.LambdaCaptureContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.captureDefault() is not None:
            if ctx.captureDefault().Assign() is not None:
                # implicitly capture by copy
                self.rustCode += "move "

    def visitLambdaDeclarator(self, ctx: CPP14Parser.LambdaDeclaratorContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        # No need to check for Mutable keyword, since parameters are made mutable by default in the program
        if ctx.parameterDeclarationClause() is not None:
            self.rustCode += "|"
            self.visit(ctx.parameterDeclarationClause())
            self.rustCode += "|"
        if ctx.exceptionSpecification() is not None:
            self.visit(ctx.exceptionSpecification())
        # todo: handle attributes in future here
        if ctx.trailingReturnType() is not None:
            self.visit(ctx.trailingReturnType())

    def visitMemInitializerList(self, ctx: CPP14Parser.MemInitializerListContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        childCount = ctx.getChildCount()
        for i in range(childCount):
            child = ctx.getChild(i)
            childText = child.getText()
            if childText == "," or childText == "...":
                self.rustCode += childText + "\n"
            else:
                self.visit(child)

    def visitMemInitializer(self, ctx: CPP14Parser.MemInitializerContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        self.visit(ctx.meminitializerid())
        if ctx.bracedInitList() is not None:
            self.visit(ctx.bracedInitList())
        else:
            self.rustCode += ":"
            if ctx.expressionList() is not None:
                self.visit(ctx.expressionList())
            else:
                self.rustCode += "NULL // Cannot initialize with empty int Rust please update accordingly\n"

    def visitMeminitializerid(self, ctx: CPP14Parser.MeminitializeridContext):
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.Identifier() is not None:
            self.rustCode += " " + ctx.Identifier().getText() + " "
        else:
            self.visit(ctx.classOrDeclType())

    def visitClassOrDeclType(self, ctx: CPP14Parser.ClassOrDeclTypeContext):
        return super().visitClassOrDeclType(ctx)

    def statementBlockVisitor(self, ctx: CPP14Parser.StatementContext):
        # ensures that the statement block is wrapped in curly braces
        logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)
        
        if ctx.compoundStatement() is None:
            self.rustCode += "{\n"
            self.visit(ctx)
            self.rustCode += "}\n"
        else:
            self.visit(ctx)

def expressionVisitor(self, ctx: ParserRuleContext):
    logToCsv(inspect.currentframe().f_code.co_name, ctx.getText(), self.rustCode)

    self.visit(ctx.getChild(0))
    childCount = ctx.getChildCount()
    if childCount > 1:
        for i in range(1, childCount, 2):
            if ctx.getChild(i).getText() in self.opKeywordConversionMap:
                self.rustCode += " " + self.opKeywordConversionMap[ctx.getChild(i).getText()] + " "
            else :
                self.rustCode += " " + ctx.getChild(i).getText() + " "
            self.visit(ctx.getChild(i + 1))


def singleParameterFunctionHandling(ctx: CPP14Parser.SimpleDeclarationContext):
    
    if ctx.declSpecifierSeq() is not None \
            and ctx.declSpecifierSeq().declSpecifier(0) is not None \
            and ctx.declSpecifierSeq().declSpecifier(0).typeSpecifier() is not None \
            and ctx.declSpecifierSeq().declSpecifier(0).typeSpecifier().trailingTypeSpecifier() is not None \
            and ctx.declSpecifierSeq().declSpecifier(0).typeSpecifier().trailingTypeSpecifier().simpleTypeSpecifier() is not None \
            and ctx.declSpecifierSeq().declSpecifier(0).typeSpecifier().trailingTypeSpecifier().simpleTypeSpecifier().theTypeName() is not None \
            and ctx.declSpecifierSeq().declSpecifier(0).typeSpecifier().trailingTypeSpecifier().simpleTypeSpecifier().theTypeName().className() is not None \
            and ctx.initDeclaratorList() is not None \
            and ctx.initDeclaratorList().initDeclarator(0) is not None \
            and ctx.initDeclaratorList().initDeclarator(0).declarator() is not None \
            and ctx.initDeclaratorList().initDeclarator(0).declarator().pointerDeclarator() is not None \
            and ctx.initDeclaratorList().initDeclarator(0).declarator().pointerDeclarator().noPointerDeclarator() is not None \
            and ctx.initDeclaratorList().initDeclarator(0).declarator().pointerDeclarator().noPointerDeclarator().declaratorid() is None:
        return True

    return False

# declarator id for differentiation

def pointerHandling(ctx: CPP14Parser.MemberdeclarationContext):
    
    if ctx.memberDeclaratorList() is not None \
            and ctx.memberDeclaratorList().memberDeclarator(0) is not None \
            and ctx.memberDeclaratorList().memberDeclarator(0).declarator() is not None \
            and ctx.memberDeclaratorList().memberDeclarator(0).declarator().pointerDeclarator() is not None \
            and ctx.memberDeclaratorList().memberDeclarator(0).declarator().pointerDeclarator().pointerOperator(0) is not None:
        return True

    return False


def isOpOverloadedUnary(ctx: CPP14Parser.FunctionDefinitionContext):
    if ctx.declarator() is not None \
            and ctx.declarator().pointerDeclarator() is not None \
            and ctx.declarator().pointerDeclarator().noPointerDeclarator() is not None:
        noPointerDecl = ctx.declarator().pointerDeclarator().noPointerDeclarator()
        if noPointerDecl.parametersAndQualifiers() is not None \
            and noPointerDecl.parametersAndQualifiers().parameterDeclarationClause() is None:
                return True
    return False


def getFunctionName(self,ctx: CPP14Parser.FunctionDefinitionContext):
    
    if ctx.declarator() is not None \
            and ctx.declarator().pointerDeclarator() is not None \
            and ctx.declarator().pointerDeclarator().noPointerDeclarator() is not None \
            and ctx.declarator().pointerDeclarator().noPointerDeclarator().noPointerDeclarator() is not None \
            and ctx.declarator().pointerDeclarator().noPointerDeclarator().noPointerDeclarator().declaratorid() is not None:
        declId = ctx.declarator().pointerDeclarator().noPointerDeclarator().noPointerDeclarator().declaratorid()
        unqualifiedId = ""
        if declId.idExpression() is not None \
                and declId.idExpression().qualifiedId() is not None \
                and declId.idExpression().qualifiedId().unqualifiedId() is not None:
            # return declId.idExpression().qualifiedId().unqualifiedId().getText()
            unqualifiedId = declId.idExpression().qualifiedId().unqualifiedId()
        elif declId.idExpression() is not None \
                and declId.idExpression().unqualifiedId() is not None:
            unqualifiedId = declId.idExpression().unqualifiedId()
        returnText = unqualifiedId.getText()
        if unqualifiedId.operatorFunctionId() is not None:
            # we have an operator as the function name
            op = unqualifiedId.operatorFunctionId().theOperator().getText()
            if op in self.opConversionMap:
                returnText = op

        return returnText

    return None

def getFunctionScopedParentName(ctx: CPP14Parser.FunctionDefinitionContext):
    
    if ctx.declarator() is not None \
            and ctx.declarator().pointerDeclarator() is not None \
            and ctx.declarator().pointerDeclarator().noPointerDeclarator() is not None \
            and ctx.declarator().pointerDeclarator().noPointerDeclarator().noPointerDeclarator() is not None \
            and ctx.declarator().pointerDeclarator().noPointerDeclarator().noPointerDeclarator().declaratorid() is not None: 
        decl = ctx.declarator().pointerDeclarator().noPointerDeclarator().noPointerDeclarator().declaratorid()
        if decl.idExpression() is not None \
                and decl.idExpression().qualifiedId() is not None \
                and decl.idExpression().qualifiedId().nestedNameSpecifier() is not None:
            nested_name_spec = decl.idExpression().qualifiedId().nestedNameSpecifier()

            if nested_name_spec.theTypeName() is not None:
                return nested_name_spec.theTypeName().getText()
            
            elif ctx.declSpecifierSeq() is not None \
                    and ctx.declSpecifierSeq().declSpecifier(0) is not None \
                    and ctx.declSpecifierSeq().declSpecifier(0).typeSpecifier() is not None \
                    and ctx.declSpecifierSeq().declSpecifier(0).typeSpecifier().trailingTypeSpecifier() is not None \
                    and ctx.declSpecifierSeq().declSpecifier(0).typeSpecifier().trailingTypeSpecifier().simpleTypeSpecifier() is not None: 
                simple_type_specifier = ctx.declSpecifierSeq().declSpecifier(0).typeSpecifier().trailingTypeSpecifier().simpleTypeSpecifier()
                if simple_type_specifier.theTypeName() is not None and simple_type_specifier.theTypeName().className() is not None:
                    return simple_type_specifier.theTypeName().className().getText()

        return None

    return None

def getFunctionReturnType(ctx: CPP14Parser.FunctionDefinitionContext):
    
    if ctx.declSpecifierSeq() is not None \
            and ctx.declSpecifierSeq().declSpecifier(0) is not None \
            and ctx.declSpecifierSeq().declSpecifier(0).typeSpecifier() is not None \
            and ctx.declSpecifierSeq().declSpecifier(0).typeSpecifier().trailingTypeSpecifier() is not None \
            and ctx.declSpecifierSeq().declSpecifier(0).typeSpecifier().trailingTypeSpecifier().simpleTypeSpecifier() is not None:

        return ctx.declSpecifierSeq().declSpecifier(0).typeSpecifier().trailingTypeSpecifier().simpleTypeSpecifier().getText()

    return None

def declaratorHasParameters(ctx: CPP14Parser.DeclaratorContext):
    
    if ctx.pointerDeclarator() is not None \
            and ctx.pointerDeclarator() is not None \
            and ctx.pointerDeclarator().noPointerDeclarator() is not None \
            and ctx.pointerDeclarator().noPointerDeclarator().parametersAndQualifiers() is not None:
        return True
    return False

def memberDeclarationIsFuntion(ctx: CPP14Parser.MemberdeclarationContext):
    
    if ctx.memberDeclaratorList() is not None \
            and ctx.memberDeclaratorList().memberDeclarator(0) is not None \
            and ctx.memberDeclaratorList().memberDeclarator(0).declarator() is not None \
            and declaratorHasParameters(ctx.memberDeclaratorList().memberDeclarator(0).declarator()) is True:
        return True
    return False
