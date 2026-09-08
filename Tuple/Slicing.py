"""
Topic: Slicing a Tuple
Description: You can specify a range of indexes to extract a part of the tuple.
It works exactly the same as List slicing.
"""

# Initial tuple of student marks
marks = (78, 85, 92, 67, 74)
print("Full Tuple:", marks)
print("-" * 30)

# Get items from index 1 to 3
print("Items from index 1 to 3 [1:4]:", marks[1:4])

# Get the first three items
print("First three items [:3]:", marks[:3])

# Get items from index 2 to the end
print("From index 2 to the end [2:]:", marks[2:])
