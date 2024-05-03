## C

#### Supported Constructs and their limitations:
- main function
    - needs care to ignore the return 0; if present
    - code snippets that use argc and argv are not dealt with. as the way to access cli arguments in rust is a bit different

- declaration and initialization of single dimensional arrays.

- declaration of multiple dimensional arrays

- declaration of simple datatypes and implicit as well as explicit casting.


- functions
    - currently only supports primitive data types. those that can be allocated space statically. They are copied by value.
    - types like string / vector is not dealt with. They cannot be passed as is. (see Unsupported Constructs)
    - arrays cannot be passed as of yet.

- while loops
    - issues with statements like while (1) as rust expects boolean values explicitly 

- for loops
    - handled by unwrapping to a while loop

- conditional statement
    - issues with statements like if (5) as rust expects boolean values explicitly 

- switch statement
    - handled without isssues

- printf 
    - handled without issues

- structs
    - structs can support all primitive data types. 

- enums
    - handled without issues


#### Unsupported Constructs:

- Pointers . Raw pointers can be declared and used to point to variables but they cannot be dereferenced. Smart pointers or references can be used but they are based on the principle: there can be at most one mutable reference to data. in c, multiple pointers to same position and can modify it.

- Arrays. Pointers and arrays are more or less the same. name of a array decays to a constant pointer to the first element of the array. this is used to pass them to functions. and pointer arithmetic is inherently unsafe in rust.

- strings . strings are character arrays in c. functions like strlen, strcpy, have corresponding functions in rust. but need a strategy to follow. better to make a corresponding character array in rust or make a string in rust ? (strings come with ownership issues)

- scanf . in constrast to how easy it is to handle printf. the way of taking input in rust is cumbersome. always checking the input is trimmed and correctly parsed before assigning to a target and handling any exceptions during parsing as well.

- header files . So far the header files have been ignored by the grammar. so might need to modify the grammar.

- Advanced constructs
    - Macros - Possible approach: expand macros before feeding to transpiler.
    - preprocessor directives
    - function pointers?
    - pointers to pointers?
    - pointer to arrays?
