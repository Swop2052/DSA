marks = [78, 85, 92, 67, 74]

# Create a separate copy
sorted_marks = marks.copy()

# Change only the copied List
sorted_marks.sort(reverse=True)

print("Original:", marks)
print("Sorted:", sorted_marks)