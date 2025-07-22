# A simple Python script demonstrating how a Dictionary is more efficient than nested if-else cases.
# -------------------------------------------------------------------------------------------------------------------------------

def first():
    print('Calling: first')

def second():
    print('Calling: second')

def third():
    print('Calling: third')

def default():
    print('Calling: default')

var: int = 0

# Nested If-Else cases
"""if var == 0:
    first()
elif var == 1:
    second()
elif var == 2:
    third()
else:
    default()"""
# -------------------------------------------------------------------------------------------------------------------------------
# Dictionary takes the value you want to check for as a key
funcs: dict = {0: first,
               1: second,
               2: third}

# If value does not exist, then default() is called
final = funcs.get(var, default)
final()