# All methods in this file are used to merge two arrays and sort them in different ways.

# Each method demonstrates a different approach to handling arrays in Python.
# The methods include:
# Removing duplicates via set() 
# Merging in Ascending and Descending order via sorted()
# Slicing and Reversing
# Index-Based Looping
# In-Place Swapping
# Using the reversed() function
# -------------------------------------------------------------------------------------------------------------------------------
def merge_arrays_ascend(arrayA, arrayB):
    # Merge arrayA and arrayB
    # Remove duplicates                                     # set() is used to remove duplicates
    # Sort list in ascending order                          # sort() is used to sort the list in Ascending order
    return sorted(set(arrayA + arrayB))

def merge_arrays_descend(arrayA, arrayB):
    # Sort list in descending order                         # "reverse = True" is used to sort the list in Descending order
    return sorted(set(arrayA + arrayB), reverse=True)

def Slice_Reversed(arrayA, arrayB):
    # Slice-Reversed list:
    # Return the reversed sorted list                       # [::-1] is used to reverse the sorted list
    return sorted(arrayA + arrayB)[::-1]

def Index_Based_Loop(arrayA, arrayB):
    # Index­-Based Loop & Inline Printing
    array = sorted(arrayA + arrayB)
    for i in range(len(array) - 1, -1, -1):
        print(array[i], end=' ')

def In_Place_Swap(arrayA, arrayB):
    # In-Place Swap
    array = sorted(arrayA + arrayB)
    for i in range(len(array)//2):
        array[i], array[-i-1] = array[-i-1], array[i]
    print(array)

def Reverse_Loop(arrayA, arrayB):
    # reversed()
    array = sorted(arrayA + arrayB)
    for x in reversed(array):
        print(x, end=' ')

# --------------------------------------------------------------------------------------------------------------------------------
a = [1, 2, 3, 3, 4, 5, 6]
b = [4, 4, 5, 6, 7, 8, 9]
c = merge_arrays_ascend(a, b)
print(c)                                    # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

d = merge_arrays_descend(a, b)
print(d)                                    # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1]

arrayE = [9, 7, 0]
arrayF = [5, 3, 6]
e = Slice_Reversed(arrayE, arrayF)
print(e)                                    # Output: [9, 7, 6, 5, 3, 0]
# --------------------------------------------------------------------------------------------------------------------------------
arrayG = [2, 8, 4]
arrayH = [3, 1, 7]
f = Index_Based_Loop(arrayG, arrayH)        # Output: 8 7 4 3 2 1
print()                                     # Print a new line for better readability

arrayI = [0, 5, 1]
arrayJ = [6, 9, 2]
g = In_Place_Swap(arrayI, arrayJ)           # Output: [9, 6, 5, 2, 1, 0]

arrayK = [3, 5, 2]
arrayL = [8, 1, 4]
h = Reverse_Loop(arrayK, arrayL)            # Output: 8 5 4 3 2 1
# --------------------------------------------------------------------------------------------------------------------------------