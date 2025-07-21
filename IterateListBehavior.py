# Unexpected behavior in your loops while iterating over a list
# -------------------------------------------------------------------------------------------------------------------------------
items = ['A', 'B', 'C', 'D', 'E']

for item in items:
    if item == 'B':
        items.remove('B')   # This will cause an issue
    else:
        print(item)

# The above code will skip 'C' because the list is modified during iteration.
# To avoid this, iterate over a copy of the list or use a different approach.
# -------------------------------------------------------------------------------------------------------------------------------
new_items = []              # Temporary list to hold items

for item in items:
    if item == 'B':
        continue            # Skip 'B' without modifying the original list
    else:
        print(item)
        new_items.append(item)