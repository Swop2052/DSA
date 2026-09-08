"""
Topic: Complete Tuple Project (Student Result Card)
Description: A mini-project combining Tuple Creation, Indexing, Unpacking, 
Looping, and utilizing the safety of Immutable Data.
"""

print("=== Student Result Card System ===\n")

# 1. Student Information stored in a Tuple (Name, Roll No, City)
# Tuples are used here because this information shouldn't change!
student_details = ("Amit Sharma", 101, "Mumbai")

# 2. Student Marks stored in a Tuple (Math, Science, English, History)
marks = (88, 92, 75, 80)

# --- Unpacking Details ---
(name, roll_no, city) = student_details
print(f"Student Name: {name}")
print(f"Roll Number : {roll_no}")
print(f"City        : {city}")
print("-" * 30)

# --- Processing Marks ---
print("Marks Breakdown:")
subjects = ("Math", "Science", "English", "History") # Tuple of subjects

# Loop using range and len to pair subject with mark
for i in range(len(marks)):
    print(f"{subjects[i]} : {marks[i]}")

print("-" * 30)
# --- Calculations ---
total_marks = sum(marks)
average = total_marks / len(marks)

print(f"Total Marks  : {total_marks} / 400")
print(f"Percentage   : {average}%")

# Using tuple immutability as a feature
print("\n[Security Note]: Since marks are stored in a Tuple, they are secure and cannot be altered accidentally by the program.")
