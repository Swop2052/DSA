"""
Topic: Copying a List
Description: The copy() method creates a separate, independent copy of the list.
Changes made to the copied list will not affect the original list.
"""

# Initial list of student marks
marks = [78, 85, 92, 67, 74]

# Create a completely separate copy of the list
sorted_marks = marks.copy()

# Modify only the copied list (sort in descending order)
sorted_marks.sort(reverse=True)

# Display both lists to show they are independent
print("Original Marks (Unchanged):", marks)
print("Sorted Marks (Copied List):", sorted_marks)