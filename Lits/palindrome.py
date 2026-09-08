"""
Topic: Checking if a List is a Palindrome
Description: A list is a palindrome if it reads the same forwards and backwards.
We can check this by making a copy, reversing the copy, and comparing it to the original.
"""

# List of marks that reads the same forwards and backwards
marks = [78, 85, 92, 85, 78]
print("Original List:", marks)

# Step 1: Create a separate copy of the list
reverse_marks = marks.copy()

# Step 2: Reverse the copied list
reverse_marks.reverse()
print("Reversed List:", reverse_marks)

# Step 3: Compare both lists
if marks == reverse_marks:
    print("Result: The list is a Palindrome!")
else:
    print("Result: The list is NOT a Palindrome.")