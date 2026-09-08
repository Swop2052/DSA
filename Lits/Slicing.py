"""
Topic: List Slicing
Description: Slicing allows you to extract a sub-part of a list.
Syntax: list[start:end]. It starts at 'start' index and goes up to, but NOT including, 'end' index.
"""

# Initial list of student marks
marks = [78, 85, 92, 67, 74]
# Indexes: 0   1   2   3   4
print("Full List:", marks)
print("-" * 25)

# Get items starting from index 1 up to index 3 (does not include index 3)
print("Items from index 1 to 3 [1:4]:", marks[1:4])

# Leaving the start empty means "start from the beginning"
# Get the first three items (indexes 0, 1, 2)
print("First three items [:3]:", marks[:3])

# Leaving the end empty means "go until the very end"
# Get items from index 2 to the end (indexes 2, 3, 4)
print("From index 2 to the end [2:]:", marks[2:])

# Using negative indexing to slice from the right side
# Get the last three items
print("Last three items [-3:]:", marks[-3:])