# A simple Python script using Match Cases for (Dynamic) Type Checking
# -------------------------------------------------------------------------------------------------------------------------------
var = 0.025

match var:
    case str():
        print("str")
    case int():
        print("int")
    case float():
        print("float")
    case bool():
        print("bool")
    case list():
        print("list")
    case dict():
        print("dict")
    case None:
        print("None")
    case _:
        print("Unknown")
# ------------------------------------------------------------------------------------------------------------------------------
var = {'type': 'error', 'code': 404}

match var:
    case str(s) if s.startswith('P'):
        print(f"String starting with P: {s}")
    case {'type': t, 'code': c}:
        print(f"{t.capitalize()} {c}")
    case {'data': {'id': id}}:
        print(f"Nested ID: {id}")
    case dict():
        print("Other dictionary")
    case None:
        print("None")
    case _:
        print("Unknown type")