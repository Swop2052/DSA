marks = [78, 85, 92, 85, 78]

# Create a separate copy
reverse_marks = marks.copy()

# Reverse the copied List
reverse_marks.reverse()

# Compare both Lists
if marks == reverse_marks:
    print("Palindrome")
else:
    print("Not Palindrome")