"""
Topic: Removing Elements by Value (remove)
Description: The remove() method deletes the first occurrence of a specific value.
Unlike pop(), which uses an index, remove() targets the actual item value.
"""

# Initial list of student marks
marks = [78, 85, 92, 67, 74]
print("Original Marks:", marks)

# Remove the specific value '67'
# Note: If '67' was not in the list, this would cause an error!
marks.remove(67)

# Display the list after removal
print("Marks after remove(67):", marks)