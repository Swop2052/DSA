# Start with an empty List
marks = []

# Repeat 5 times
for i in range(5):

    # Take mark from the user
    mark = int(input("Enter student mark: "))

    # Add the mark to the List
    marks.append(mark)

# Display the final List
print("Marks:", marks)