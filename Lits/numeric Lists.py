"""
Topic: Operations on Numeric Lists
Description: Python provides built-in functions like sum(), max(), and min()
that make it easy to perform mathematical operations on a list of numbers.
"""

# Initial list of student marks
marks = [78, 85, 92, 67, 74]
print("Student Marks:", marks)
print("-" * 25)

# Calculate the total sum of all marks
total = sum(marks)
print(f"Total Marks: {total}")

# Find the highest (maximum) mark in the list
highest = max(marks)
print(f"Highest Mark: {highest}")

# Find the lowest (minimum) mark in the list
lowest = min(marks)
print(f"Lowest Mark: {lowest}")

# Count total number of marks
count = len(marks)
print(f"Total Count: {count}")

# Calculate the average (Total / Count)
average = total / count
print(f"Average Mark: {average}")