import sys
import os
import time
import shutil
from antlr4 import *
from antlr4.tree.Trees import Trees
from dist.CPP14Lexer import CPP14Lexer
from dist.CPP14Parser import CPP14Parser
from CPPtoRustConverter import CPPtoRustConverter


def getFileStream(filePath, tempFilePath):
    try:
        with open(filePath, "rb") as source_file, open(
            tempFilePath, "wb"
        ) as destination_file:
            for line in source_file:
                line = line.replace(b"std::", b"")
                destination_file.write(line)
    except FileNotFoundError:
        print("Error: Source file not found!")
        exit()
    except PermissionError:
        print("Error: Insufficient permissions to access files!")
        exit()
    outputFile = FileStream(tempFilePath)
    return outputFile


def main(argv):

    os.environ["DEBUG"] = argv[2] if len(argv) > 2 else "0"

    with open("log.csv", "w") as file:
        pass  # Opening in 'w' mode and closing the file truncates it to 0 bytes

    start_time = time.perf_counter()
    filePath = argv[1]

    tempFilePath = "./.temp.cpp"
    input = getFileStream(filePath, tempFilePath)
    lexer = CPP14Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = CPP14Parser(stream)
    tree = parser.translationUnit()

    os.remove(tempFilePath)
    filename, file_extension = os.path.splitext(filePath)

    tree_filename = filename + "_tree.tree"
    output_filename = filename + "_converted.rs"

    with open(tree_filename, "w") as tree_output:
        tree_output.write(Trees.toStringTree(tree, None, parser))
    tree_output.close()

    convertor = CPPtoRustConverter()
    rustCode = convertor.convert(tree)

    with open(output_filename, "w") as output:
        output.write(rustCode)
    output.close()

    # for formatting
    os.system("rustfmt " + output_filename)
    end_time = time.perf_counter()

    # Calculate the time taken in milliseconds
    time_taken_ms = (end_time - start_time) * 1000

    print("Time taken: {:.2f} ms".format(time_taken_ms))


if __name__ == "__main__":
    main(sys.argv)
