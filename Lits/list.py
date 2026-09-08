"""
Topic: Creating a List dynamically with User Input
Description: Start with an empty list and use a loop to repeatedly ask the user
for input, adding each new item to the list using append().
"""

# Start with an empty List
marks = []
print("--- Student Marks Entry System ---")

# Repeat 5 times using a for loop
for i in range(5):
    # Take mark from the user (converting the string input to an integer)
    mark = int(input(f"Enter student mark {i+1}: "))

    # Add the entered mark to our list
    marks.append(mark)

# Display the final dynamically created list
print("\nFinal List of Marks:", marks)