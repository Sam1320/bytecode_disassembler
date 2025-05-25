# Python Bytecode Disassembler

A simple command-line tool to disassemble Python code into bytecode.

## Features

- Disassemble entire Python files
- Disassemble code snippets provided as strings
- Disassemble specific functions from modules
- Interactive mode for entering code through stdin

## Usage

```bash
# Disassemble a file
python bytecode_disassembler.py -f your_file.py

# Disassemble a Python code string
python bytecode_disassembler.py -c 'def hello(): print("Hello, world!")'

# Disassemble a specific function from a module
python bytecode_disassembler.py -m your_module.py -n function_name

# Interactive mode (enter code from stdin)
python bytecode_disassembler.py

# Show usage examples
python bytecode_disassembler.py --examples
```

## Requirements

- Python 3.6+

## How It Works

The tool uses Python's built-in `dis` module to compile and disassemble Python code. The bytecode is the low-level representation of Python code that is executed by the Python virtual machine (CPython).

Understanding bytecode can be useful for:
- Learning how Python works internally
- Debugging complex issues
- Optimizing performance-critical code 