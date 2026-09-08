# The in operator checks whether a value exists.
marks = [78, 85, 92, 67, 74]

# Ask the user which mark they want to search
search = int(input("Enter marks to search: "))

# Check whether the mark exists
if search in marks:
    print("Marks found")
else:
    print("Marks not found")