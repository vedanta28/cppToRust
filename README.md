## How to run

### Pre-requisites

#### antlr4 python runtime

```
pip install antlr4-python3-runtime
```

#### Optional - (For Formatting Rust)

```
rustup component add rustfmt
# if not installed please comment the line
# os.system("rustfmt " + output_filename) in main.py
```

### Running the Program

#### Generating Lexer and Parser using anltr4 in Python inside "dist" directory

```
antlr4 -Dlanguage=Python3 CPP14Lexer.g4 -visitor -o dist
antlr4 -Dlanguage=Python3 CPP14Parser.g4 -visitor -o dist
```

#### Execution

```
python main.py filename
```

This will create file named `filename_converted.rs` and `filename_tree.tree` in the same directory as the input file.

## Support for C Constructs:

#### Supported Constructs and their limitations:

- main function

  - needs care to ignore the return 0; if present
  - code snippets that use argc and argv are not dealt with. as the way to access cli arguments in rust is a bit different

- declaration and initialization of single dimensional arrays.

- declaration and initialization of multi-dimensional arrays

- declaration of simple datatypes and implicit as well as explicit casting.

- functions

  - regular functions are supported
  - function pointers are not supported

- while loops

  - issues with statements like while (1) as rust expects boolean values explicitly

- for loops

  - handled by unwrapping to a while loop

- conditional statement

  - issues with statements like if (5) as rust expects boolean values explicitly

- switch statement

- printf

- structs

  - structs can support all primitive data types.

- enums

- arrays

- pointers

  - partially converted into raw pointers, will require manual intervention to correct the transpiled code

#### Unsupported Constructs:

- Pointers . Raw pointers can be declared and used to point to variables but they cannot be dereferenced. Smart pointers or references can be used but they are based on the principle: there can be at most one mutable reference to data. in c, multiple pointers to same position and can modify it.

- scanf . in constrast to how easy it is to handle printf. the way of taking input in rust is cumbersome. always checking the input is trimmed and correctly parsed before assigning to a target and handling any exceptions during parsing as well.

- strings . strings are character arrays in c. functions like strlen, strcpy, have corresponding functions in rust. but need a strategy to follow. better to make a corresponding character array in rust or make a string in rust (strings come with ownership issues)

- header files . So far the header files have been ignored by the grammar. so might need to modify the grammar.

- Advanced constructs
  - Macros
  - preprocessor directives
  - function pointers?
  - pointers to pointers?
  - pointer to arrays?

# Support for C++ Constructs

### Supported constructs and their limitations

- cout

- Stl containers : Vectors, stacks, queues, sets and maps

  - Implemented using a rust struct which acts as a wrapper over rust's equivalent containers
  - Doesn't implement iterators

- Classes

  - Constructors are converted into a function returning a struct. So transpiled constructors require manual rewriting
  - inheritance is not supported
  - operator overloading is supported for arithmetic operators

- Templates

  - using templates to support multiple datatypes is supported

- CPP Strings
  - Implemented using a rust struct which acts as a wrapper over rust's Strings
  - doesn't implement iterators

### Unsupported constructs

- exceptions
- NULL values : This requires conversion of NULL values to Options in rust, but since it requires lots of changes in logic as well, NULL values aren't supported
- function overloading
- default values for parameters
- safe and unsafe Pointers
  - Can be implemented using a rust wrapper struct
- cin : similar to scanf
- Iterators
- Range based for loops
  - Issue due to lack of support for iterators
- new statements
