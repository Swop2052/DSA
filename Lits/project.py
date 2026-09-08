"""
Topic: Comprehensive List Project (Student Marks Analyzer)
Description: A mini-project that combines creating lists, indexing, calculations, 
sorting, conditions, and searching into a single program.
"""

print("=== Student Marks Analyzer System ===\n")

# 1. Create an empty List
marks = []

# -------------------------------
# INPUT SECTION
# -------------------------------
print("--- 1. Enter Marks ---")
# Take 5 marks from the user
for i in range(5):
    mark = int(input(f"Enter student mark {i+1}: "))
    marks.append(mark)

# -------------------------------
# BASIC INFORMATION
# -------------------------------
print("\n--- 2. Basic Information ---")
print("All Marks:", marks)
print("First mark:", marks[0])
print("Last mark:", marks[-1])
print("Number of marks:", len(marks))

# -------------------------------
# CALCULATIONS
# -------------------------------
print("\n--- 3. Calculations ---")
print("Total sum of marks:", sum(marks))
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))
print("Average mark:", sum(marks) / len(marks))

# -------------------------------
# SORTING (Using a Copy)
# -------------------------------
print("\n--- 4. Sorting ---")
# Create a separate copy so we don't mess up the original order
sorted_marks = marks.copy()
# Sort from highest to lowest (Descending)
sorted_marks.sort(reverse=True)
print("Marks sorted (Highest to Lowest):", sorted_marks)

# -------------------------------
# CONDITIONS
# -------------------------------
print("\n--- 5. Excellent Marks (80 or above) ---")
# Check every mark and print if it's >= 80
for mark in marks:
    if mark >= 80:
        print(f"Excellent mark found: {mark}")

# -------------------------------
# SEARCHING
# -------------------------------
print("\n--- 6. Search functionality ---")
# Ask the user for a mark to search
search = int(input("Enter a mark to search in the list: "))

# Check whether the mark exists
if search in marks:
    print(f"Success! The mark {search} was found.")
else:
    print(f"Sorry. The mark {search} was not found.")