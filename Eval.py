# The Eval.py file is as a Whitelisted Eval function that allows only safe mathematical expressions.
# It is not recommended to use Eval in production code due to security risks.
# This example is for educational purposes only.

# This is a Whitelist technique that lets us use Eval safely by restricting the available functions and modules.
# --------------------------------------------------------------------------------------------------------------------------------

import math

data = input("Exp: ")

# Whitelist of allowed functions and modules for Eval function.
# This restricts the execution context to only safe functions and modules.
allowed = {
    '__builtins__': None,  # Disable all built-in functions
    'abs': abs,  # Allow abs function
    'round': round,  # Allow round function
    'pow': pow,  # Allow power function
    'min': min,  # Allow min function
    'max': max,  # Allow max function
    'math': math,  # Allow math module for mathematical operations
}

try:
    # result = eval(data)           # Unsafe Eval, not recommended
    result = eval(data, allowed)    # Safe Eval, with restricted context
    print(result)
except Exception as e:
    print("Error:", e)