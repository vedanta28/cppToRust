PY = python3
TEST_DIR = tests
RS = rustc
TEST_FILES = $(wildcard $(TEST_DIR)/*.cpp)
PARSER = main.py



Color_Off = \033[0m     
Black = \033[0;30m       
Red = \033[0;31m          # Red
Green = \033[0;32m        # Green
Yellow = \033[0;33m       # Yellow
Blue = \033[0;34m        # Blue
Purple = \033[0;35m       # Purple
Cyan = \033[0;36m        # Cyan
White = \033[0;37m        

.PHONY: help all clean cleanexec test cleanall makedirs

help:
	@echo "${Cyan}\n!!! Welcome to the Makefile for CPP to Rust Transpiler !!!\n"
	@echo "${Green}"
	@echo "Command \tFunction\n"
	@echo "------- \t--------"
	@echo "${Yellow}"
	
clean:
	rm $(TEST_DIR)/*.rs
	rm $(TEST_DIR)/*.tree

test: $(TEST_FILES)
	@tests=0; \
	passed=0; \
	echo "${Cyan}\n!!! Running the Transpiler on the input files in the test directory ${TEST_DIR}/ !!!${Color_Off}\n"; \
	for input_file in $^; do \
		tests=$$(($$tests + 1)); \
		ofile=$$(echo $$input_file | cut -d "/" -f 2); \
		root=$$(echo $$ofile |cut -d '.' -f 1); \
		echo "${Blue}\n~~~> Running the parser on $$input_file ${Color_Off}\n"; \
		echo ;\
		$(PY) $(PARSER) "$$input_file";\
		EXIT_CODE=$$?; \
		if [ $$EXIT_CODE -ne 0 ]; then \
			echo "${Red}\n> Parser failed So skipping Rust Compilation\n"; \
			continue; \
		fi; \
		echo "${Green}\n> Parser passed So running Rust Compilation\n"; \
		$(RS) $(TEST_DIR)/"$$root"_converted.rs -o $(TEST_DIR)/$$root; \
		EXIT_CODE=$$?; \
		if [ $$EXIT_CODE -ne 0 ]; then \
			echo "${Red}\n> Rust Compilation failed\n"; \
			continue; \
		fi; \
		echo "${Green}\n> Rust Compilation passed\n"; \
		rm $(TEST_DIR)/$$root; \
		passed=$$(($$passed + 1)); \
	done; \
	echo "${Cyan}\n!!! Test Results !!!${Color_Off}\n"; \
	echo "${Blue}\nTotal Tests: $$tests ${Color_Off}\n"; \
	echo "${Green}\nTests Passed: $$passed${Color_Off}\n"; \
	echo "${Red}\nTests Failed: $$(($$tests-$$passed))${Color_Off}\n"

