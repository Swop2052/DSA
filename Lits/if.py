"""
Topic: Conditional Statements with Lists
Description: Using an 'if' statement inside a loop to evaluate each item in a list individually.
"""

# Initial list of student marks
marks = [78, 85, 92, 67, 74]
print("Analyzing Student Marks:")

# Iterate through every student's mark
for mark in marks:
    # Check whether the mark is 80 or above
    if mark >= 80:
        print(f"Mark: {mark} -> Excellent")
    else:
        print(f"Mark: {mark} -> Needs Improvement")