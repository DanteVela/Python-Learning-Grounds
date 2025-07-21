# Immediately Invoked Function Expression (IIFE) in Python
# -------------------------------------------------------------------------------------------------------------------------------
# Immediately Invoked Function Expression (IIFE):
# It defines a function and immediately invokes it.
@lambda _: _()
def function() -> str:
    print("This is an IIFE function")
    return 'IIFE executed successfully'

print(function)  # This will execute the function immediately