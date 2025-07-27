# This script demonstrates how to remove duplicates while maintaining the list order.
# -------------------------------------------------------------------------------------------------------------------------------
old = ['a', 'b', 'a', 'c', 'b', 'a']

new = list(set(old))                            # Removes duplicates, but doesn't maintain list order
print(new)

new = []                                        # Removes duplicates and maintains list order
for item in old:
    if item not in new:
        new.append(item)
print(new)

# Optimized 1 Line Code: Removes duplicates and maintains list order
# list(): Turn back into list | dict.fromkeys(): Dictionaries are unique
# .keys(): Only want keys result
new = list(dict.fromkeys(old).keys())
print(new)                                      