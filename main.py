#!/usr/bin/env python3
import dis
import sys
import io
from contextlib import redirect_stdout
import argparse
import importlib.util

def disassemble_code(code_str):
    """
    Compile and disassemble a Python code string.
    
    Args:
        code_str (str): Valid Python code as a string
        
    Returns:
        str: The disassembled bytecode
    """
    # Compile the code string
    compiled_code = compile(code_str, '<string>', 'exec')
    
    # Capture the output of dis.dis() in a string
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        dis.dis(compiled_code)
    
    return buffer.getvalue()

def disassemble_function(module_name, function_name):
    """
    Disassemble a specific function from a module.
    
    Args:
        module_name (str): Name of the module
        function_name (str): Name of the function to disassemble
        
    Returns:
        str: The disassembled bytecode
    """
    # Import the module
    spec = importlib.util.spec_from_file_location("module", module_name)
    module = importlib.util.module_from_spec(spec)
    
    # Capture stdout during module import to suppress any print statements
    original_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        spec.loader.exec_module(module)
    finally:
        sys.stdout = original_stdout
    
    # Get the function
    func = getattr(module, function_name)
    
    # Disassemble the function
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        dis.dis(func)
    
    return buffer.getvalue()

def print_examples():
    examples = """
Examples:
  # Disassemble a file
  python bytecode_disassembler.py -f example.py
  
  # Disassemble a code string
  python bytecode_disassembler.py -c 'def hello(): print("Hello, world!")'
  
  # Disassemble a specific function from a module
  python bytecode_disassembler.py -m example.py -n hello
  
  # Interactive mode (stdin)
  python bytecode_disassembler.py
"""
    print(examples)

def main():
    parser = argparse.ArgumentParser(
        description='Disassemble Python code to bytecode',
        epilog='Use --examples for usage examples'
    )
    input_group = parser.add_mutually_exclusive_group()
    input_group.add_argument('-f', '--file', help='Python file to disassemble')
    input_group.add_argument('-c', '--code', help='Python code string to disassemble')
    input_group.add_argument('-m', '--module', help='Module file to disassemble a function from')
    input_group.add_argument('--examples', action='store_true', help='Show usage examples')
    parser.add_argument('-n', '--function', help='Function name to disassemble (used with -m)')
    
    args = parser.parse_args()
    
    if args.examples:
        print_examples()
    elif args.file:
        # Read from file
        with open(args.file, 'r') as f:
            code_str = f.read()
        print(disassemble_code(code_str))
    elif args.code:
        # Use the provided code string
        print(disassemble_code(args.code))
    elif args.module and args.function:
        # Disassemble a specific function from a module
        print(disassemble_function(args.module, args.function))
    else:
        # Read from stdin
        print("Enter Python code (Ctrl+D to end):")
        code_str = sys.stdin.read()
        print(disassemble_code(code_str))

if __name__ == "__main__":
    main()