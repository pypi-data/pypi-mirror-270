from cffi import FFI
from .util import get_library_name, read_file
import json
import sys
import os
import logging
logging.basicConfig(format='%(levelname)s:%(asctime)s %(funcName)s:%(lineno)d - %(message)s', level=logging.INFO)


# Create an FFI instance
ffi = FFI()

lib_name = get_library_name()

logging.debug(f"library name: {lib_name}")
logging.debug(f"__file__: {__file__}")

library_path = os.path.join(os.path.dirname(__file__), 'libs', lib_name)

# Load the shared library
lib = ffi.dlopen(library_path)  # Update the path to your shared library

# Declare the function signature for the C function
ffi.cdef("""
    char* evaluate(const char* content, const char* content);
""")



def evaluate(content: str, statement: str) -> str:
    """
    Evaluates json string against the rule.

    Args:
    content (str): The json formatted string.
    statement (str): The rule.

    Returns:
    str: The evaluation result.
    """

    # Convert Python string to C string
    c_content = ffi.new("char[]", content.encode())
    c_statement = ffi.new("char[]", statement.encode())

    # Call the C function
    c_result = lib.evaluate(c_content, c_statement)

    # Convert C string to Python string
    result = ffi.string(c_result).decode()

    ffi.release(c_content)
    ffi.release(c_statement)

    return result


def evaluate_dict(content: dict, statement: str) -> str:
    """
    Evaluates dict object against the rule.

    Args:
    content (dict): The dict object which represents the content to evaluated.
    statement (str): The rule.

    Returns:
    str: The evaluation result.
    """

    content_str = json.dumps(content)

    # Convert Python string to C string
    c_content = ffi.new("char[]", content_str.encode())
    c_statement = ffi.new("char[]", statement.encode())

    # Call the C function
    c_result = lib.evaluate(c_content, c_statement)

    # Convert C string to Python string
    result = ffi.string(c_result).decode()

    ffi.release(c_content)
    ffi.release(c_statement)

    return result


if __name__ == "__main__":
    filePath: str = sys.argv[1]

    content_json = read_file(filePath)

    statement: str = sys.argv[2]

    content = json.dumps(content_json)

    result: str = evaluate(content, statement)

    print(result)

