import dis
import io
from contextlib import redirect_stdout

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
