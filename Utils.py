# File to Store all the utility functions for Convertor


# maps for data types and functions
typeMap = {
    "short": "i16",
    "short int": "i16",
    "int": "i32",
    "long long": "i64",
    "long long int": "i64",
    "signed short": "i16",
    "signed short int": "i16",
    "signed int": "i32",
    "signed long long": "i64",
    "signed long long int": "i64",
    "unsigned short": "u16",
    "unsigned short int": "u16",
    "unsigned int": "u32",
    "unsigned long long": "u64",
    "unsigned long long int": "u64",
}

knownFunctionMap = {
    "printf": "print!",
    "cout": "print!"
}


# functions for converting printf and cout to println!
def printfReplacer(LiteralText):

    printFormatsList = ['%d', '%c', '%s', '%f']
    new_string = LiteralText

    for format in printFormatsList:
        old_substring = format
        new_substring = "{}"

        split_list = new_string.split(old_substring)
        if len(split_list) > 1:
            new_list = [new_substring if i < len(
                split_list)-1 else '' for i in range(len(split_list)-1)]
            new_string = ''.join([split_list[i] + new_list[i]
                                 for i in range(len(split_list)-1)] + [split_list[-1]])

    return new_string


def coutHandler(texts):
    printingElements = []
    nonStringElements = []
    for printingText in texts:
        if '"' in printingText:
            printingElements.append(printingText[1:-1])
        else:
            if printingText == "endl":
                printingElements.append("\\n")
            else:
                printingElements.append("{}")
                nonStringElements.append(printingText)
    
    nonStringElements = [nonStringElement.replace("]", " as usize ]") for nonStringElement in nonStringElements]

    printingString = ''.join(printingElements)
    formatString = ','.join(nonStringElements)

    Comma = ""
    if len(formatString) > 0:
        Comma = ","

    finalString = '("' + printingString + '"' + Comma + formatString + ")"

    return finalString
