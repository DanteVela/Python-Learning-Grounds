# ...
import numpy as np

# 0: Dimensional Array
array = np.array('A')

# ndim: Dimensions of Array
print(array.ndim)

# 1: Dimensional Array
array = np.array(['A', 'B', 'C'])
print(array.ndim)

# 2: Dimensional Array
array = np.array([['A', 'B', 'C'], 
                 ['D', 'E', 'F'], 
                 ['G', 'H', 'I']])
print(array.ndim)

# 3: Dimensional Array  (All values must be accounted for proper dimensions)
array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])

print(array.ndim)

# shape: of an array: Tuple Result
print(array.shape)

# Chain Indexing vs Multidimensional Indexing
print(array[0][0][0])       # Chain
print(array[0, 0, 0])       # Multidimensional - Layer, Row, Column

# String Concatenation
word = array[0, 0, 0] + array[2, 0, 0] + array[2, 0, 0]
print(word)