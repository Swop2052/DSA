"""
Topic: Removing Elements by Index (pop)
Description: The pop() method removes an item at a specific index and returns it.
If no index is provided, pop() removes and returns the last item in the list.
"""

# Initial list of student marks
marks = [78, 85, 92, 67, 74]
print("Original Marks:", marks)

# Remove the item at index 2 (which is '92')
removed_mark = marks.pop(2)

# Display what was removed and the remaining list
print(f"Removed Mark: {removed_mark} (from index 2)")
print("Marks after pop(2):", marks)