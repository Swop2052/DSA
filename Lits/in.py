"""
Topic: Checking Existence in a List (in operator)
Description: The 'in' operator checks whether a specific value exists inside a list.
It returns True if found, otherwise False.
"""

# Initial list of student marks
marks = [78, 85, 92, 67, 74]

# Ask the user which mark they want to search for
# Note: input() returns a string, so we convert it to an integer using int()
search = int(input("Enter marks to search: "))

# Check whether the requested mark exists in our list
if search in marks:
    print(f"Yes! The mark {search} was found in the list.")
else:
    print(f"No. The mark {search} was not found in the list.")