# ---------------------------------------------------------------------------------------------------------------------------------
# Incorrect method, creates a bug with growing list each call that wasn't passed in same memory location
def add_items(item, my_list=[]):
    print(f"{id(my_list)=}")
    my_list.append(item)
    return my_list

# Bug occurs here
print(add_items(1))
print(add_items(2))
print(add_items(3))

# This works since we're not using default list
print(add_items(1, [10, 20]))
print(add_items(2, [99, 100]))
print(add_items(3, []))
# ---------------------------------------------------------------------------------------------------------------------------------
# The fix is to set the default value to "None"
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []                                # If None, Create a fresh list with each call
    print(f"{id(my_list)=}")
    my_list.append(item)
    return my_list

print(add_item(1))
print(add_item(2))
print(add_item(3))