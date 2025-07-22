# A simple Python script demonstrating how zip and zip_longest functions combine lists with or without fillvalues.
from itertools import zip_longest
# -----------------------------------------------------------------------------------------------------------------------------

elements = ['A', 'B', 'C', 'D']
numbers = [1, 2]

# zip(): List with shortest length gets zipped while ignoring rest of elements if not same length
zipped = zip(numbers, elements)
print(list(zipped))

# zip_longest(): Ensures that everything is zipped with a default value of "None" if lists are not same length
# fillvalue: Changes the default value from "None" to a different value
zipped_long = zip_longest(numbers, elements, fillvalue='_')
print(list(zipped_long))