# Create an empty List
marks = []

# -------------------------------
# INPUT
# -------------------------------

# Take 5 marks from the user
for i in range(5):

    # Take mark as input
    mark = int(input("Enter student mark: "))

    # Add the mark to the List
    marks.append(mark)


# -------------------------------
# BASIC INFORMATION
# -------------------------------

# Display all marks
print("\nMarks:", marks)

# Display the first mark
print("First mark:", marks[0])

# Display the last mark
print("Last mark:", marks[-1])

# Display the number of marks
print("Number of marks:", len(marks))


# -------------------------------
# CALCULATIONS
# -------------------------------

# Calculate total
print("Total:", sum(marks))

# Find highest mark
print("Highest:", max(marks))

# Find lowest mark
print("Lowest:", min(marks))

# Calculate average
print("Average:", sum(marks) / len(marks))


# -------------------------------
# SORTED COPY
# -------------------------------

# Create a separate copy
sorted_marks = marks.copy()

# Sort from highest to lowest
sorted_marks.sort(reverse=True)

print("Highest to lowest:", sorted_marks)


# -------------------------------
# CONDITION
# -------------------------------

print("\nMarks 80 or above:")

# Check every mark
for mark in marks:

    # Print only marks 80 or above
    if mark >= 80:
        print(mark)


# -------------------------------
# SEARCH
# -------------------------------

# Ask the user for a mark
search = int(input("\nEnter marks to search: "))

# Check whether the mark exists
if search in marks:
    print("Marks found")
else:
    print("Marks not found")