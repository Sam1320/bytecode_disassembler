# Python Bytecode Disassembler

A simple tool to disassemble Python code into bytecode, available as a web interface.

## 🌐 Web Interface

Try it online: **[Live Demo](https://sam1320.github.io/bytecode_disassembler)**

The web interface provides an interactive way to explore Python bytecode directly in your browser, powered by Pyodide. You can type code directly, use provided examples, or upload a Python (`.py`) file.

## Features

### Web Interface
- Interactive code editor
- Real-time bytecode disassembly
- File upload for `.py` scripts
- Pre-loaded examples to get started quickly
- Mobile-responsive design
- No installation required - runs entirely in the browser

## Usage

### Web Interface
Simply open `index.html` in your browser or visit the [live demo](https://sam1320.github.io/bytecode_disassembler).

## How It Works

The web application uses Python's built-in `dis` module, running via Pyodide in the browser, to compile and disassemble Python code. The bytecode is the low-level representation of Python code that is executed by the Python virtual machine (CPython).

Understanding bytecode can be useful for:
- Learning how Python works internally
- Debugging complex issues
- Optimizing performance-critical code 