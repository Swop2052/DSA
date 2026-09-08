"""
Topic: Updating List Items
Description: Since Lists are "changeable" (mutable), you can modify the value 
of an item by referring to its index number.
"""

# Initial list of student marks
marks = [78, 85, 92, 67, 74]
print("Original Marks:", marks)

# Change the mark at index 3 (which is currently '67') to '72'
marks[3] = 72

# Print the list after updating the value
print("Updated Marks (Changed index 3 to 72):", marks)