## How to run

### Pre-requisites 

####  antlr4 python runtime
```
pip install antlr4
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