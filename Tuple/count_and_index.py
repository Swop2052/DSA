"""
Topic: Tuple Methods (count & index)
Description: Since Tuples cannot be changed, they only have 2 built-in methods:
1. count() - Returns how many times a value appears.
2. index() - Searches the tuple for a value and returns its position.
"""

# Tuple containing some duplicate marks
marks = (78, 85, 92, 85, 74)
print("Marks Tuple:", marks)
print("-" * 30)

# 1. count()
# Count how many times the mark '85' appears
occurrences = marks.count(85)
print(f"The mark 85 appears {occurrences} times.")

# 2. index()
# Find the position of the mark '92'
position = marks.index(92)
print(f"The mark 92 is located at index {position}.")
