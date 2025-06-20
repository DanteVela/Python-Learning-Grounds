# To run the file, simply call "python [Filename].py" by using the "cmd Terminal".

# -------------------------------------------------------------------------------------------------------------------------------

# Two Sum Problem:

# Find two numbers that sum to the target
# May not use the same element twice
# Assume there is exactly one solution
nums = [1, 3, 4, 5, 7]
target = 7

# Example: 3+4 = 7 so we return the indices (1,2)

# (1,3), (1,4), (1,5), ..., (3,4),

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            index = (i, j)
            break
            # print(f"Indices: ({i}, {j})")  # Output: Indices: (1, 2)

# 4 + 3 + 2 + 1 = 4(4+1)/2

# 1 + ... + n = n(n)/2
# O(n^2)
# .5 * n^2

# -------------------------------------------------------------------------------------------------------------------------------

# Optimized Two Sum Solution using a Dictionary
# O(n)

def two_sum(nums, target):
    # Create an empty dictionary
    d = {}

    # Loop through the array
    for i, num in enumerate(nums):
        # Calculate the complement
        # complement = target - num
        
        # Check if the complement of current number is in dictionary
        if target - num in d:
            # Return the index of the complement and the current index
            return (d[target - num], i)
        # Add the current number and index to the dictionary
        d[num] = i

nums = [1, 3, 4, 5, 7]
target = 11

d = {}

# i = 0
# d = {}
""" is target - num in d"""         # is 7 - 1 in d? no
d[1] = 0

# i = 1
# d = {1: 0}
"""is target - num in d"""          # is 7 - 3 in d? no
d[3] = 1

# i = 2
# d = {1:0, 3:1}
"""is target - num in d"""          # is 7 - 4 in d? yes because d[3] = 1
# indicies = 2, d[3]

# -------------------------------------------------------------------------------------------------------------------------------