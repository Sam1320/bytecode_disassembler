# Python Bytecode Disassembler

A simple tool to disassemble Python code into bytecode, available both as a command-line tool and a web interface.

## 🌐 Web Interface

Try it online: **[Live Demo](https://sam1320.github.io/bytecode_disassembler)**

The web interface provides an interactive way to explore Python bytecode directly in your browser, powered by Pyodide.

## Features

### Command Line Tool
- Disassemble entire Python files
- Disassemble code snippets provided as strings
- Disassemble specific functions from modules
- Interactive mode for entering code through stdin

### Web Interface
- Interactive code editor with syntax highlighting
- Real-time bytecode disassembly
- Pre-loaded examples to get started quickly
- Mobile-responsive design
- No installation required - runs entirely in the browser

## Usage

### Web Interface
Simply open `index.html` in your browser or visit the [live demo](https://sam1320.github.io/bytecode_disassembler).

### Command Line Tool

```bash
# Disassemble a file
python main.py -f your_file.py

# Disassemble a Python code string
python main.py -c 'def hello(): print("Hello, world!")'

# Disassemble a specific function from a module
python main.py -m your_module.py -n function_name

# Interactive mode (enter code from stdin)
python main.py

# Show usage examples
python main.py --examples
```

## Requirements

- Python 3.6+

## How It Works

The tool uses Python's built-in `dis` module to compile and disassemble Python code. The bytecode is the low-level representation of Python code that is executed by the Python virtual machine (CPython).

Understanding bytecode can be useful for:
- Learning how Python works internally
- Debugging complex issues
- Optimizing performance-critical code 