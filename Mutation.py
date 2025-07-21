# Mutable or Immutable Data Types in Python
# -------------------------------------------------------------------------------------------------------------------------------
# Mutable data types can be changed after they are created: list, dict, set...
# Immutable data types cannot be changed after they are created: int, float, bool, str, tuple, frozenset...
# -------------------------------------------------------------------------------------------------------------------------------
# This script demonstrates the concept of mutability in Python by modifying a list.
# It defines a function that appends an element to a list and shows how the original list is affected.
# -------------------------------------------------------------------------------------------------------------------------------
# "Pass by reference": When a mutable object is passed to a function, the function can modify the object in place.
def mutation(list):
    list.append(10)                                 # Append 10 to the list.
    return list                                     # This function modifies the list in place and returns it.

numbers = [1, 2, 3]
list_after_mutation = mutation(numbers)             # [1, 2, 3, 10] because lists are mutable, thus the original list is modified.

print("Original list:", numbers)                    # Output = [1, 2, 3, 10] because the original list was modified by the function.
print("List after mutation:", list_after_mutation)  # Output = [1, 2, 3, 10] because the function returned the modified list.