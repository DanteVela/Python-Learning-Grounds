# To run the file, simply call "python [Filename].py" by using the "cmd Terminal".

# -------------------------------------------------------------------------------------------------------------------------------

# Importing
import math
math.sqrt(9)  # Calculate the square root of 9

import time
# Print the current time
print("The current time is: ", time.ctime())

# -------------------------------------------------------------------------------------------------------------------------------

# How to Comment
a = 5
# a = a + 1
print(a)

# -------------------------------------------------------------------------------------------------------------------------------

# Indenting
x = 1
if 2*x == 1:
    print("yes")

# -------------------------------------------------------------------------------------------------------------------------------

# Variables
x = 1
x = x + 2

# Print the value of x
print("The value of x is: ", x)

# -------------------------------------------------------------------------------------------------------------------------------

# Strings
x = "abc"
y = "de"
z = x + y

# Print the value of z
print("The value of z is: ", z)
# Print the type of z
print("The type of z is: ", type(z))

z = z[1:3]  # Slicing the string | Similar to arrays
# Print the sliced value of z
print("The sliced value of z is: ", z)

# -------------------------------------------------------------------------------------------------------------------------------

# Functions
def f(x):
    y = x + 2
    return y

# Call the function f with argument 5
f(5)

# Print the result of the function call
print("This is a function call with argument 5: ", f(5))

# Multiple functions
def f(x):
    return 2*x

def g(y):
    return 1 + y

# Call the functions f and g with argument 4
g(f(4))
f(g(4))

# Print the result of the function calls
print("This is a function call with argument 4: ", g(f(4)))     # (2*4)+1
print("This is a function call with argument 4: ", f(g(4)))     # 2*(1+4)

# -------------------------------------------------------------------------------------------------------------------------------

# if Statements
x = 2
if x+1 == 3:
    print(x)
if x+1 == 4:
    print(x)

# if-else Statement
x = 2
if x == 1:
    print(5)
else:
    print(1)

# -------------------------------------------------------------------------------------------------------------------------------

# Loops
for i in range(1, 100):
    if i%2 == 0:  # Check if i is even
        print("This is a loop with i = ", i)

# -------------------------------------------------------------------------------------------------------------------------------

# Arrays
a = [1, 2, 3, 4]
print("The array a is: ", a)
a.append(8)  # Append 8 to the array a
print("The array a after appending 8 is: ", a)

# Looping through arrays in 2 ways
for i in range(len(a)):
    print("This is a loop with a[i] = ", a[i])

for x in a:
    print("This is a loop with x = ", x)

# Delete from array
a = [1, 2, 3, 4, 5]
a.pop()  # Remove the last element from the array
print("The array a after popping the last element is: ", a)

# -------------------------------------------------------------------------------------------------------------------------------

# Dictionary
d = {'cat': 'meow', 'dog': 'bark', 'bird': 'chirp'}

# Print the value associated with the key 'cat'
print("The value associated with the key 'cat' is: ", d['cat'])

d['dog'] = 'run' # Assign a new value to the key 'dog'

# Print everything in the dictionary
print("Dictionary:", d)

# -------------------------------------------------------------------------------------------------------------------------------

# Sets

# 1
# Set vs Dictionary adding elements
s = set()  # Create an empty set
d = {}  # Create an empty dictionary

s.add(3)  # Add an element to the set
s.add(6)
s.add(9)
s.remove(9)  # Remove an element from the set
d[3] = 45  # Add a key-value pair to the dictionary
d[6] = 89
d[1] = 89
d[1] = 67  # Update the value for the key 1 in the dictionary
print("Set:", s)
print("Dictionary:", d)

# Sets cannot have duplicates
s.add(1)
s.add(1)  # Adding a duplicate element to the set
print("Set after adding duplicates:", s)  # The set will still only contain unique elements

# 2
# Dictionary & Set that associates the elements to something

s = set(['cat', 'dog', 'bird'])  # Create a set with initial elements
d = {'cat':'joe', 'dog':'janet', 'bird':'jack'}  # Create a dictionary with initial key-value pairs
print("Set with initial elements:", s)
print("Dictionary with initial key-value pairs:", d)

# 3
# Set operations
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])

# Intersection
s3 = s1.intersection(s2)  # Find common elements in both Sets
print("Intersection of s1 and s2:", s3)  # Print the intersection of the two Sets

# Union
s3 = s1.union(s2)  # Combine all unique elements from both Sets
print("Union of s1 and s2:", s3)  # Print the union of the two Sets

# Difference
s3 = s1.difference(s2)  # Find elements in s1 that are not in s2
print("Difference of s1 and s2 (s1 - s2):", s3)  # Print the difference of the two Sets

len(s3)  # Get the number of elements in the Set
len(d)  # Get the number of key-value pairs in the Dictionary

# -------------------------------------------------------------------------------------------------------------------------------