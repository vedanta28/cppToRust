from antlr4 import *
from dist.CPP14Parser import CPP14Parser
from dist.CPP14ParserVisitor import CPP14ParserVisitor
from Utils import *


class CPPtoRustConverter(CPP14ParserVisitor):
    def __init__(self):
        # output
        self.rustCode = "#![allow(warnings, unused)]\n"

        # handling data type conversion
        self.currentTempDataType = ""
        self.Std = None

        # Handling known Function types
        self.currentFunction = ""

        # Handling switch case breaks and braces
        self.isSwitchStatementCaseBeingEvaluated = False
        self.switchEval = False

        # Handling Classes
        self.currentClassName = ""
        self.isFunctionDefinitionInsideClass = False
        self.isClassFunctionParameters = False
        self.isThisAConstructorCall = False
        self.attributesInClasses = {}
        self.currentFunctionParameters = set()
        self.selfPresent = False
        self.dontVisitNestedNameSpecifier = False

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
            "unsignedlonglongint": "u64",
            "size_t": "usize",
            "float": "f32",
            "double": "f64",
            "longdouble": "f64",  # Note: f128 was removed in Rust
            "bool": "bool",
        }


    def convert(self, tree):
        self.visit(tree)
        return self.rustCode

    # Visit a parse tree produced by CPP14Parser#literal.
    def visitLiteral(self, ctx: CPP14Parser.LiteralContext):
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
                self.currentFunction = ""

            self.rustCode += LiteralText

    # Expression Chain

    # Visit a parse tree produced by CPP14Parser#literal.
    def visitExpression(self, ctx: CPP14Parser.ExpressionContext):
        expressionVisitor(self, ctx)

    def visitLogicalOrExpression(self, ctx: CPP14Parser.LogicalOrExpressionContext):
        expressionVisitor(self, ctx)

    def visitLogicalAndExpression(self, ctx: CPP14Parser.LogicalAndExpressionContext):
        expressionVisitor(self, ctx)

    def visitInclusiveOrExpression(self, ctx: CPP14Parser.InclusiveOrExpressionContext):
        expressionVisitor(self, ctx)

    def visitExclusiveOrExpression(self, ctx: CPP14Parser.ExclusiveOrExpressionContext):
        expressionVisitor(self, ctx)

    def visitAndExpression(self, ctx: CPP14Parser.AndExpressionContext):
        expressionVisitor(self, ctx)

    def visitEqualityExpression(self, ctx: CPP14Parser.EqualityExpressionContext):
        expressionVisitor(self, ctx)

    def visitRelationalExpression(self, ctx: CPP14Parser.RelationalExpressionContext):
        expressionVisitor(self, ctx)

    def visitShiftExpression(self, ctx: CPP14Parser.ShiftExpressionContext):
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
        self.rustCode += " " + ctx.getText() + " "

    def visitAdditiveExpression(self, ctx: CPP14Parser.AdditiveExpressionContext):
        expressionVisitor(self, ctx)

    def visitMultiplicativeExpression(
        self, ctx: CPP14Parser.MultiplicativeExpressionContext
    ):
        expressionVisitor(self, ctx)

    def visitPointerMemberExpression(
        self, ctx: CPP14Parser.PointerMemberExpressionContext
    ):
        self.visit(ctx.getChild(0))
        childCount = ctx.getChildCount()
        if childCount > 1:
            self.rustCode += "// Safe Rust Code does not recommend raw pointers, thus references and addressing are not possible directly, refer to Rust documentation for more information\n"
            for i in range(1, childCount, 2):
                self.visit(ctx.getChild(i))
                self.visit(ctx.getChild(i + 1))

    def visitCastExpression(self, ctx: CPP14Parser.CastExpressionContext):
        if ctx.unaryExpression() is not None:
            self.visit(ctx.unaryExpression())
        else:
            # print(ctx.getText())
            self.visit(ctx.castExpression())
            self.rustCode += " as "
            self.visit(ctx.theTypeId())

    # visiting children
    def visitTheTypeId(self, ctx: CPP14Parser.TheTypeIdContext):
        # self.rustCode += ctx.theTypeId().getText()
        if ctx.getText() in self.conversion_map:
            self.rustCode += self.conversion_map[ctx.getText()]
        else:
            self.rustCode += ctx.getText()
        return super().visitTheTypeId(ctx)

    # visiting children
    def visitTypeSpecifierSeq(self, ctx: CPP14Parser.TypeSpecifierSeqContext):
        return super().visitTypeSpecifierSeq(ctx)

    # visiting children

    def visitAbstractDeclarator(self, ctx: CPP14Parser.AbstractDeclaratorContext):
        return super().visitAbstractDeclarator(ctx)

    def visitTypeSpecifier(self, ctx: CPP14Parser.TypeSpecifierContext):
        # print("arnav")
        # if ctx.enumSpecifier() is not None:
        #    print(ctx.enumSpecifier().enumHead().enumkey().getText())
        return super().visitTypeSpecifier(ctx)

    def visitTrailingTypeSpecifier(self, ctx: CPP14Parser.TrailingTypeSpecifierContext):
        return super().visitTrailingTypeSpecifier(ctx)


    def visitSimpleTypeSpecifier(self, ctx: CPP14Parser.SimpleTypeSpecifierContext):
        self.visitChildren(ctx) # vedanta
        # return

    def visitElaboratedTypeSpecifier(self, ctx: CPP14Parser.ElaboratedTypeSpecifierContext):

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
        # there are no classes in Rust only Structs
        self.rustCode += " struct "

    def visitTypeNameSpecifier(self, ctx: CPP14Parser.TypeNameSpecifierContext):
        self.rustCode += "// Yet to support Templates, please refer to the documentation" + " "
        self.visitChildren(ctx)

    def visitCvQualifier(self, ctx: CPP14Parser.CvQualifierContext):
        # initial assumption
        # TODO: This is not working properly
        return super().visitCvQualifier(ctx)

        if ctx.Const() is not None:
            self.rustCode += " *const "
        else:
            self.rustCode += " *mut "

    def visitClassSpecifier(self, ctx: CPP14Parser.ClassSpecifierContext):
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
            for i in nonAttributes:
                if i.functionDefinition() is not None:
                    functionName = getFunctionName(i.functionDefinition())
                    if self.currentClassName != functionName:
                        self.attributesInClasses.setdefault(self.currentClassName, set())
                        self.attributesInClasses[self.currentClassName].add(functionName)

            for i in nonAttributes:
                if i.functionDefinition() is not None:
                    self.rustCode += "pub "
                    self.isFunctionDefinitionInsideClass = True
                    self.isClassFunctionParameters = True
                    self.currentClassName = className.getText()
                self.visit(i)
                self.isFunctionDefinitionInsideClass = False
                self.currentFunctionParameters.clear()
            self.rustCode += " }\n"

        self.currentClassName = ""

    def visitClassHead(self, ctx: CPP14Parser.ClassHeadContext):
        if ctx.Union() is not None:
            self.rustCode += "// Currently ignoring unions in the transpilation\n"
        self.visitChildren(ctx)

    def visitAttributeSpecifierSeq(self, ctx: CPP14Parser.AttributeSpecifierSeqContext):
        return super().visitAttributeSpecifierSeq(ctx)

    def visitAttributeSpecifier(self, ctx: CPP14Parser.AttributeSpecifierContext):
        self.rustCode += "// Currently ignoring attribute specifiers in the transpilation\n"
        self.visitChildren(ctx)

    def visitAlignmentspecifier(self, ctx: CPP14Parser.AlignmentspecifierContext):
        self.rustCode += "// Currently ignoring alignment specifiers in the transpilation\n"
        self.visitChildren(ctx)

    def visitMemberSpecification(self, ctx: CPP14Parser.MemberSpecificationContext):
        # currently assuming all the methods to be public thus access specifiers have no meaning
        self.rustCode += "// Currently all methods and variables are assumed to be public\n"
        self.visitChildren(ctx)

    def visitMemberdeclaration(self, ctx: CPP14Parser.MemberdeclarationContext):
        if ctx.Semi() is not None:
            if pointerHandling(ctx):
                # this is has a pointer declarator then need to something else

                # if ctx.memberDeclaratorList() -> memberDeclarator(0) -> declarator() -> pointerDeclarator -> pointerOperator(0) is not None

                cntx = ctx.memberDeclaratorList().memberDeclarator(
                    0).declarator().pointerDeclarator()

                self.visit(cntx.noPointerDeclarator())

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
        expressionVisitor(self, ctx)

    def visitMemberDeclarator(self, ctx: CPP14Parser.MemberDeclaratorContext):
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
        return super().visitDeclarator(ctx)

    def visitPointerDeclarator(self, ctx: CPP14Parser.PointerDeclaratorContext):
        if len(ctx.pointerOperator()) > 0:
            self.rustCode += "// Handling Pointers...\n"
        self.visitChildren(ctx)

    def visitPointerOperator(self, ctx: CPP14Parser.PointerOperatorContext):
        if ctx.Star() is not None:
            if ctx.nestedNameSpecifier() is not None:
                self.visit(ctx.nestedNameSpecifier())

            self.rustCode += "*mut "

            if ctx.attributeSpecifierSeq() is not None:
                self.visit(ctx.attributeSpecifierSeq())

            if ctx.cvqualifierseq() is not None:
                self.visit(ctx.cvqualifierseq())

        else:
            self.rustCode += " " + ctx.getChild(0).getText() + " "
            if ctx.attributeSpecifierSeq() is not None:
                self.visit(ctx.attributeSpecifierSeq())

    def visitCvqualifierseq(self, ctx: CPP14Parser.CvqualifierseqContext):
        return super().visitCvqualifierseq(ctx)

    def visitNestedNameSpecifier(self, ctx: CPP14Parser.NestedNameSpecifierContext):
        self.rustCode += " " + ctx.getText() + " "

    def visitTheTypeName(self, ctx: CPP14Parser.TheTypeNameContext):
        return super().visitTheTypeName(ctx)

    def visitClassName(self, ctx: CPP14Parser.ClassNameContext):
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
        self.rustCode += "// Templates are yet to supported! Currently copying them as it is!\n"
        self.rustCode += " " + ctx.getText() + " "

    def visitEnumName(self, ctx: CPP14Parser.EnumNameContext):
        self.rustCode += " " + ctx.Identifier().getText() + " "
    
    def visitEnumSpecifier(self, ctx:CPP14Parser.EnumSpecifierContext):
        # self.rustCode += " " + ctx.getText() + " "
        return self.visitChildren(ctx)
    
    def visitEnumHead(self, ctx:CPP14Parser.EnumHeadContext):
        self.rustCode += " " + ctx.enumkey().getText() + " " + ctx.Identifier().getText() + " "
        return self.visitChildren(ctx)
    
    def visitEnumeratorList(self, ctx:CPP14Parser.EnumeratorListContext):
        # self.rustCode += " {\n " + ctx.getText() + " \n} "
        self.rustCode += " {\n "
        self.visitChildren(ctx)
        self.rustCode += " } "
        return
    
    def visitEnumeratorDefinition(self, ctx:CPP14Parser.EnumeratorDefinitionContext):
        # self.rustCode += " " + ctx.Identifier().getText() + " "
        self.rustCode += ctx.enumerator().getText() + " = " 
        self.visitChildren(ctx)
        self.rustCode += ",\n"

    def visitTypedefName(self, ctx: CPP14Parser.TypedefNameContext):
        self.rustCode += " " + ctx.Identifier().getText() + " "

    def visitNamespaceName(self, ctx: CPP14Parser.NamespaceNameContext):
        self.rustCode += " " + ctx.getText() + "::*"

    def visitDecltypeSpecifier(self, ctx: CPP14Parser.DecltypeSpecifierContext):
        self.rustCode += " " + ctx.getText() + " "
        self.rustCode += "// DeclType are yet to supported! Currently copying them as it is!\n"

    def visitNoPointerDeclarator(self, ctx: CPP14Parser.NoPointerDeclaratorContext):
        if ctx.declaratorid() is not None:
            self.visitChildren(ctx)

        elif ctx.pointerDeclarator() is not None:
            self.rustCode += " ( "
            self.visit(ctx.pointerDeclarator())
            self.rustCode += " ) "
        else:
            self.visit(ctx.noPointerDeclarator())
            if ctx.parametersAndQualifiers() is not None:
                self.visit(ctx.parametersAndQualifiers())
            else:
                self.rustCode += " [ "
                if ctx.constantExpression() is not None:
                    self.visit(ctx.constantExpression())
                self.rustCode += " ] "
                if ctx.attributeSpecifierSeq() is not None:
                    self.visit(ctx.attributeSpecifierSeq())

    def visitDeclaratorid(self, ctx: CPP14Parser.DeclaratoridContext):
        if ctx.Ellipsis() is not None:
            self.rustCode += " ... "
        self.visit(ctx.idExpression())
        if self.isThisATemplateDeclaration:
            self.rustCode += self.currentTemplateParameters
            self.currentTemplateParameters=""
            self.isThisATemplateDeclaration=False

    def visitIdExpression(self, ctx: CPP14Parser.IdExpressionContext):
        return super().visitIdExpression(ctx)

    def visitUnqualifiedId(self, ctx: CPP14Parser.UnqualifiedIdContext):
        if ctx.Identifier() is not None:

            IdentifierText = ctx.Identifier().getText()

            self.currentFunction = IdentifierText

            knownMappedFunction = knownFunctionMap.get(IdentifierText)

            if knownMappedFunction is not None:
                IdentifierText = knownMappedFunction

            elif IdentifierText == self.currentClassName:
                # print("Hi I am looking at a constructor call")
                IdentifierText = "new"

            elif (
                self.selfPresent is True
                and IdentifierText in self.attributesInClasses.setdefault(self.currentClassName,set())
                and IdentifierText not in self.currentFunctionParameters
            ):
                IdentifierText = "self." + IdentifierText

            self.rustCode += " " + IdentifierText + " "

        elif ctx.Tilde() is not None:
            self.rustCode += "// Mostly refers to the destructor function implementation... Need to look at how to implement this...\n"
            self.rustCode += " " + ctx.Tilde().getText()
            self.visit(ctx.getChild(1))

        else:
            self.visitChildren(ctx)

    def visitQualifiedId(self, ctx: CPP14Parser.QualifiedIdContext):
        if self.dontVisitNestedNameSpecifier is False:
            self.visit(ctx.nestedNameSpecifier())
        if ctx.Template() is not None:
            self.rustCode += " template "
        self.visit(ctx.unqualifiedId())

    def visitParametersAndQualifiers(self, ctx: CPP14Parser.ParametersAndQualifiersContext):
        self.rustCode += " ( "

        if self.isClassFunctionParameters:
            if self.isThisAConstructorCall is not True:
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
        self.visit(ctx.parameterDeclarationList())
        if ctx.Ellipsis() is not None:
            # Attributes walaa scene still not clear
            if ctx.Comma() is not None:
                self.rustCode += ", ..."
            else:
                self.rustCode += "..."

    def visitParameterDeclarationList(self, ctx: CPP14Parser.ParameterDeclarationListContext):
        expressionVisitor(self, ctx)

    def visitParameterDeclaration(self, ctx: CPP14Parser.ParameterDeclarationContext):
        if ctx.attributeSpecifierSeq() is not None:
            self.visit(ctx.attributeSpecifierSeq())
        # for accommodating types:
        if ctx.declarator() is not None:
            self.currentFunctionParameters.add(ctx.declarator().getText())
            self.rustCode += "mut "
            self.visit(ctx.declarator())
            self.rustCode += ":"
        elif ctx.abstractDeclarator() is not None:
            self.rustCode += "mut "
            self.currentFunctionParameters.add(
                ctx.abstractDeclarator().getText())
            self.visit(ctx.abstractDeclarator())
            self.rustCode += ":"

        self.visit(ctx.declSpecifierSeq())

        if ctx.Assign() is not None:
            self.rustCode += " = "
            self.visit(ctx.initializerClause())

    def visitInitializerClause(self, ctx: CPP14Parser.InitializerClauseContext):
        return super().visitInitializerClause(ctx)

    def visitAssignmentExpression(self, ctx: CPP14Parser.AssignmentExpressionContext):
        return super().visitAssignmentExpression(ctx)

    def visitConditionalExpression(self, ctx: CPP14Parser.ConditionalExpressionContext):
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
        self.rustCode += " " + ctx.getText() + " "

    def visitThrowExpression(self, ctx: CPP14Parser.ThrowExpressionContext):
        # initial assumption
        self.rustCode += "// Need to use third party crates to handle try/catch throw statements\n"
        self.rustCode += " throw "
        if ctx.assignmentExpression() is not None:
            self.visit(ctx.assignmentExpression())

    def visitBraceInitList(self, ctx: CPP14Parser.BracedInitListContext):
        self.rustCode += " { "
        if ctx.initializerList() is not None:
            self.visit(ctx.initializerList())
            if ctx.Comma() is not None:
                self.rustCode += " , "
        self.rustCode += " } "

    def visitInitializerList(self, ctx: CPP14Parser.InitializerListContext):
        childCount = ctx.getChildCount()

        for i in range(childCount):
            child = ctx.getChild(i)
            childText = child.getText()
            if childText == "," or childText == "...":
                self.rustCode += " " + childText
            else:
                self.visit(child)

        # return super().visitInitializerList(ctx)

    def visitBlockDeclaration(self, ctx: CPP14Parser.BlockDeclarationContext):
        return super().visitBlockDeclaration(ctx)

    def simpleDeclarationUtil(self, ctx: CPP14Parser.SelectionStatementContext, initDeclarator: CPP14Parser.InitDeclaratorContext):
        if ctx.declSpecifierSeq() is not None:
            if ctx.declSpecifierSeq().declSpecifier(0).getText() == "const":
                self.rustCode += "const"
            else:
                self.rustCode += "let mut "

        self.visit(initDeclarator.declarator())

        if ctx.declSpecifierSeq() is not None:
            if (ctx.declSpecifierSeq().getText() in self.classSet):
                self.rustCode += " = "
                self.visit(ctx.declSpecifierSeq())
                self.rustCode += "::new"
                if initDeclarator.initializer() is None:
                    self.rustCode += "()"
            else:
                if ctx.declSpecifierSeq().getText() != "auto":
                    self.rustCode += ":" # [FUTURE ISSUES 1]
                self.visit(ctx.declSpecifierSeq())
            # naive attempt to improve quality

        if initDeclarator.initializer() is not None:
            self.visit(initDeclarator.initializer())

        self.rustCode += ";\n"

    def visitSimpleDeclaration(self, ctx: CPP14Parser.SimpleDeclarationContext):

        # checking

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

            elif ctx.declSpecifierSeq() is not None:
                self.visitChildren(ctx)

        else:
            self.rustCode += ";\n"

    def visitInitDeclaratorList(self, ctx: CPP14Parser.InitDeclaratorListContext):
        expressionVisitor(self, ctx)

    def visitInitDeclarator(self, ctx: CPP14Parser.InitDeclaratorContext):
        return super().visitInitDeclarator(ctx)

    def visitTrailingReturnType(self, ctx: CPP14Parser.TrailingReturnTypeContext):
        self.rustCode += " -> "
        self.visit(ctx.trailingTypeSpecifierSeq())
        if ctx.abstractDeclarator() is not None:
            self.visit(ctx.abstractDeclarator())

    def visitAsmDefinition(self, ctx: CPP14Parser.AsmDefinitionContext):
        self.rustCode += "// This is ASM invocation please refer to supported rust methods for the ASM invocation. https://doc.rust-lang.org/reference/inline-assembly.html .\n"
        self.rustCode += 'unsafe { asm!( ' + \
            ctx.StringLiteral().getText() + ' ) }\n'

    def visitNamespaceAliasDefinitions(self, ctx: CPP14Parser.NamespaceAliasDefinitionContext):
        self.rustCode += "// Namespaces are not yet supported in this transpiler... Copying as it is\n"
        self.rustCode += ctx.getText() + "\n"

    def visitUsingDeclaration(self, ctx: CPP14Parser.UsingDeclarationContext):
        self.rustCode += "// Using Declarations are not yet supported in this transpiler... Copying as it is\n"
        self.rustCode += " using "
        self.rustCode += " " + ctx.getChild(1).getText() + " "
        self.visit(ctx.unqualifiedId())
        self.rustCode += ";\n"

    def visitUsingDirective(self, ctx: CPP14Parser.UsingDirectiveContext):
        if ctx.attributeSpecifierSeq() is not None:
            self.visit(ctx.attributeSpecifierSeq())
        self.rustCode += "use "
        if ctx.nestedNameSpecifier() is not None:
            self.visit(ctx.nestedNameSpecifier())
        self.visit(ctx.namespaceName())
        self.rustCode += ";\n"

    def visitStaticAssertDeclaration(self, ctx: CPP14Parser.StaticAssertDeclarationContext):
        self.rustCode += 'assert!('
        self.visit(ctx.constantExpression())
        self.rustCode += ', ' + ctx.StringLiteral().getText() + ');\n'

    def visitAliasDeclaration(self, ctx: CPP14Parser.AliasDeclarationContext):
        self.rustCode += "// Using Namespace Alias are not yet supported in this transpiler... Copying as it is\n"
        self.rustCode += ctx.getText() + "\n"

    def visitOpaqueEnumDeclaration(self, ctx: CPP14Parser.OpaqueEnumDeclarationContext):
        self.visit(ctx.enumkey())
        if ctx.attributeSpecifierSeq() is not None:
            self.visit(ctx.attributeSpecifierSeq())
        self.rustCode += " " + ctx.Identifier().getText() + " "
        if ctx.enumbase() is not None:
            self.visit(ctx.enumbase())
        self.rustCode += ";\n"

    def visitEnumKey(self, ctx: CPP14Parser.EnumkeyContext):
        self.rustCode += "enum"
        if ctx.Class() is None and ctx.Struct() is None:
            self.rustCode += "// Rust does not support unscoped enum types, make sure you add a scope to your enum\n"

    def visitEnumbase(self, ctx: CPP14Parser.EnumbaseContext):
        None
        # self.rustCode += ":"
        # self.visit(ctx.typeSpecifierSeq())

    def visitFunctionDefinition(self, ctx: CPP14Parser.FunctionDefinitionContext):

        usesScopeResolution: bool = False

        functionName = getFunctionName(ctx)
        if functionName is None:
            functionName = ""

        oldCurrentClassName = ""
        
        scopedParent = getFunctionScopedParentName(ctx)
        if scopedParent is not None:
            usesScopeResolution = True
            self.currentClassName = scopedParent.split("<")[0]
            self.isClassFunctionParameters = True
            self.rustCode += "impl" + self.currentTemplateParameters + " " + scopedParent + "{\n" 
            self.isThisATemplateDeclaration = False

        returnType = getFunctionReturnType(ctx)

        if self.namespaceDepth > 0:
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
        self.dontVisitNestedNameSpecifier = True
        self.visit(ctx.declarator())
        self.dontVisitNestedNameSpecifier = False

        if ctx.attributeSpecifierSeq() is not None:
            self.visit(ctx.attributeSpecifierSeq())

        if ctx.declSpecifierSeq() is not None and functionName != "main" and not self.isThisAConstructorCall:
            if returnType is not None and returnType != "void":
                self.rustCode += " -> "
            self.visit(ctx.declSpecifierSeq())

        elif self.isThisAConstructorCall:
            self.rustCode += " -> " + self.currentClassName + self.currentTemplateParameters + " "

        if ctx.virtualSpecifierSeq() is not None:
            self.visit(ctx.virtualSpecifierSeq())

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

        if usesScopeResolution is True:
            self.rustCode += "}\n" 
            self.isClassFunctionParameters = False

        self.selfPresent = False

    def visitDeclSpecifierSeq(self, ctx: CPP14Parser.DeclSpecifierSeqContext):
        signedNess = True
        lengthSpecifier = None
        dataType = None
        isAuto = False
        self.Std = None
        for i in ctx.declSpecifier():
            # print(i.getText(),end=" ")
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
            return super().visitDeclSpecifierSeq(ctx)
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
        return super().visitDeclSpecifierSeq(ctx)

    def visitDeclSpecifier(self, ctx: CPP14Parser.DeclSpecifierContext):
        # self.rustCode += "// Decl Specifiers need time\n"
        if ctx.Friend() is not None or ctx.Typedef() is not None or ctx.Constexpr() is not None:
            self.rustCode += " " + ctx.getText() + " "
        else:
            self.visitChildren(ctx)

    def visitStorageClassSpecifier(self, ctx: CPP14Parser.StorageClassSpecifierContext):
        self.rustCode += " " + ctx.getText() + " "

    def visitFunctionSpecifier(self, ctx: CPP14Parser.FunctionSpecifierContext):
        self.rustCode += " " + ctx.getText() + " "

    def visitFunctionBody(self, ctx: CPP14Parser.FunctionBodyContext):
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
        self.rustCode += "{ \n"
        if ctx.statementSeq() is not None:
            self.visit(ctx.statementSeq())
        self.rustCode += "} \n"

    def visitStatementSeq(self, ctx: CPP14Parser.StatementSeqContext):
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
        return super().visitStatement(ctx)

    def visitLabeledStatement(self, ctx: CPP14Parser.LabeledStatementContext):
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
        return super().visitDeclarationStatement(ctx)

    def visitExpressionStatement(self, ctx: CPP14Parser.ExpressionStatementContext):
        if ctx.expression() is not None:
            self.visit(ctx.expression())
        self.rustCode += ";\n"

    def visitSelectionStatement(self, ctx: CPP14Parser.SelectionStatementContext):
        if ctx.If() is not None:
            self.rustCode += " if "
            self.visit(ctx.condition())
            if ctx.statement(0).compoundStatement() is None:
                self.rustCode += "{\n"
                self.visit(ctx.statement(0))
                self.rustCode += "}\n"
            else:
                self.visit(ctx.statement(0))

            if ctx.Else() is not None:
                self.rustCode += " else "
                if ctx.statement(1).compoundStatement() is None:
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
            if ctx.statement(0).compoundStatement() is None:
                self.rustCode += "{\n"
                self.visit(ctx.statement(0))
                self.rustCode += "}\n"
            else:
                self.visit(ctx.statement(0))
            self.switchEval = False

    def visitIterationStatement(self, ctx: CPP14Parser.IterationStatementContext):
        # While loop
        if ctx.Do() is None and ctx.While() is not None:
            self.rustCode += " while "
            self.visit(ctx.condition())
            if ctx.statement().compoundStatement() is None:
                self.rustCode += "{\n"
                self.visit(ctx.statement())
                self.rustCode += "}\n"
            else:
                self.visit(ctx.statement())

        # Do while loop
        elif ctx.Do() is not None:
            self.rustCode += "loop {\n"
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
                self.rustCode += "// Will deal with for Range Declarations and Initializers later\n"
                self.rustCode += "for "
                self.visit(ctx.forRangeDeclaration())
                self.rustCode += " in "
                self.visit(ctx.forRangeInitializer())
                self.visit(ctx.statement())

    def visitJumpStatement(self, ctx: CPP14Parser.JumpStatementContext):
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
        self.rustCode += "// There are no try-catch blocks in rust, please code tweak code as per rust standards: https://stackoverflow.com/questions/55755552/what-is-the-rust-equivalent-to-a-try-catch-statement\n"
        self.rustCode += "try "
        self.visitChildren(ctx)

    def visitHandlerSeq(self, ctx: CPP14Parser.HandlerSeqContext):
        return super().visitHandlerSeq(ctx)

    def visitHandler(self, ctx: CPP14Parser.HandlerContext):
        self.rustCode += "catch ("
        self.visit(ctx.exceptionDeclaration())
        self.rustCode += ") \n"
        self.visit(ctx.compoundStatement())

    def visitExceptionDeclaration(self, ctx: CPP14Parser.ExceptionDeclarationContext):
        if ctx.Ellipsis() is not None:
            self.rustCode += "..."
        else:
            self.visitChildren(ctx)

    def visitEmptyDeclaration(self, ctx: CPP14Parser.EmptyDeclarationContext):
        self.rustCode += ";\n"

    def visitTemplateDeclaration(self, ctx: CPP14Parser.TemplateDeclarationContext):
        self.rustCode += "// Templates are not yet fully supported for conversion\n"
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
        # to consider, recursive template definitions
        self.visit(ctx.getChild(0))
        childCount = ctx.getChildCount()
        if childCount > 1:
            for i in range(1, childCount, 2):
                self.currentTemplateParameters += " " + ctx.getChild(i).getText() + " "
                self.visit(ctx.getChild(i + 1))

    def visitTemplateParameter(self, ctx: CPP14Parser.TemplateParameterContext):
        if ctx.typeParameter() is not None: 
            self.visit(ctx.typeParameter())
        else: # parameter declaration
            None
            # not handled yet
            # return super().visitTemplateParameter(ctx)

    def visitTypeParameter(self, ctx: CPP14Parser.TypeParameterContext):
        if ctx.Typename_() is None:
            self.rustCode += "\n Generics only allow for types as parameters\n"
        self.currentTemplateParameters += ctx.Identifier().getText() 
        # return super().visitTypeParameter(ctx)

    def visitExplicitInstantiation(self, ctx: CPP14Parser.ExplicitInstantiationContext):
        self.rustCode += "// Templates are not yet supported for conversion\n"
        if ctx.Extern() is not None:
            self.rustCode += "extern "

        self.rustCode += "template "
        self.visit(ctx.declaration())

    def visitExplicitSpecialization(self, ctx: CPP14Parser.ExplicitSpecializationContext):
        self.rustCode += "// Templates are not yet supported for conversion\n"
        self.rustCode += "template <>"
        self.visit(ctx.declaration())

    def visitLinkageSpecification(self, ctx: CPP14Parser.LinkageSpecificationContext):
        self.rustCode += "extern " + ctx.StringLiteral().getText()

        if ctx.LeftBrace() is not None:
            self.rustCode += "{ \n"
            if ctx.declarationseq() is not None:
                self.visit(ctx.declarationseq())
            self.rustCode += "} \n"

        else:
            self.visit(ctx.declaration())

    def visitNamespaceDefinition(self, ctx: CPP14Parser.NamespaceDefinitionContext):
        self.rustCode += "// Variables in namespaces are partically supported....\n"
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
            # print(ctx.originalNamespaceName().getText())
            self.rustCode += " " + ctx.originalNamespaceName().getText() + " "

        self.rustCode += "{\n"
        # if ctx.namespaceBody() is not None:
        #     self.visit(ctx.namespaceBody())
        self.visitChildren(ctx)
        self.rustCode += "}\n"
        self.namespaceDepth -= 1

    def visitAttributeDeclaration(self, ctx: CPP14Parser.AttributeDeclarationContext):
        self.visitChildren(ctx)
        self.rustCode += ";\n"

    def visitTheOperator(self, ctx: CPP14Parser.TheOperatorContext):
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
        if ctx.LeftParen() is not None:
            self.rustCode += "( "
            self.visit(ctx.expressionList())
            self.rustCode += " )"

        else:
            self.visit(ctx.braceOrEqualInitializer())

    def visitBraceOrEqualInitializer(self, ctx: CPP14Parser.BraceOrEqualInitializerContext):
        if ctx.bracedInitList() is not None:
            self.visit(ctx.bracedInitList())

        else:
            self.rustCode += " = "
            self.visit(ctx.initializerClause())

    def visitExpressionList(self, ctx: CPP14Parser.ExpressionListContext):
        return super().visitExpressionList(ctx)

    def visitCondition(self, ctx: CPP14Parser.ConditionContext):
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
        if ctx.Tilde() is not None:
            self.rustCode += "// Delete Operator not supported\n"
            self.rustCode += "~ "

        else:
            self.rustCode += ctx.getText() + " "

    def visitPostfixExpression(self, ctx: CPP14Parser.PostfixExpressionContext):
        if ctx.primaryExpression() is not None:
            self.visit(ctx.primaryExpression())

        elif ctx.LeftBracket() is not None:
            self.visit(ctx.postfixExpression())
            self.rustCode += "["
            self.visit(ctx.getChild(2))
            self.rustCode += "]"

        elif ctx.LeftParen() is not None and ctx.postfixExpression() is not None:
            self.visit(ctx.postfixExpression())
            self.rustCode += "("
            if ctx.expressionList() is not None:
                self.visit(ctx.expressionList())
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
                if ctx.Template() is not None:
                    self.rustCode += "//Templates not supported\n"
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
        if ctx.LeftParen() is not None:
            self.rustCode += "("
            self.visit(ctx.expression())
            self.rustCode += ")"

        elif ctx.This() is not None:
            # There is not reference to this as in rust as such
            # putting self as of now
            self.rustCode += "self"
            self.selfPresent = True

        else:
            self.visitChildren(ctx)

    def visitMemInitializerList(self, ctx: CPP14Parser.MemInitializerListContext):
        childCount = ctx.getChildCount()
        for i in range(childCount):
            child = ctx.getChild(i)
            childText = child.getText()
            if childText == "," or childText == "...":
                self.rustCode += childText + "\n"
            else:
                self.visit(child)

    def visitMemInitializer(self, ctx: CPP14Parser.MemInitializerContext):
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
        if ctx.Identifier() is not None:
            self.rustCode += " " + ctx.Identifier().getText() + " "
        else:
            self.visit(ctx.classOrDeclType())

    def visitClassOrDeclType(self, ctx: CPP14Parser.ClassOrDeclTypeContext):
        return super().visitClassOrDeclType(ctx)

def expressionVisitor(self, ctx: ParserRuleContext):
    self.visit(ctx.getChild(0))
    childCount = ctx.getChildCount()
    if childCount > 1:
        for i in range(1, childCount, 2):
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


def getFunctionName(ctx: CPP14Parser.FunctionDefinitionContext):
    if ctx.declarator() is not None \
            and ctx.declarator().pointerDeclarator() is not None \
            and ctx.declarator().pointerDeclarator().noPointerDeclarator() is not None \
            and ctx.declarator().pointerDeclarator().noPointerDeclarator().noPointerDeclarator() is not None \
            and ctx.declarator().pointerDeclarator().noPointerDeclarator().noPointerDeclarator().declaratorid() is not None:
        declId = ctx.declarator().pointerDeclarator().noPointerDeclarator().noPointerDeclarator().declaratorid()
        if declId.idExpression() is not None \
                and declId.idExpression().qualifiedId() is not None \
                and declId.idExpression().qualifiedId().unqualifiedId() is not None:
            return declId.idExpression().qualifiedId().unqualifiedId().getText()
        elif declId.idExpression() is not None \
                and declId.idExpression().unqualifiedId() is not None:
            return declId.idExpression().unqualifiedId().getText()

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
