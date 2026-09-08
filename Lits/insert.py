"""
Topic: Inserting Elements into a List (insert)
Description: The insert() method adds an item at a specific index/position in the list.
Unlike append(), which adds to the end, insert() can put the item anywhere.
"""

# Initial list of student marks
marks = [78, 85, 92, 67, 74]
print("Original Marks:", marks)

# Insert the mark '95' at index 2 (which is the 3rd position)
marks.insert(2, 95)

# Display the list after insertion
print("Marks after insert(2, 95):", marks)