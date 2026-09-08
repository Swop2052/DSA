"""
Topic: Unpacking a Tuple
Description: "Packing" a tuple is when we assign values to it.
"Unpacking" is when we extract those values back into separate variables.
"""

# Packing a tuple with student info
student_info = ("Rahul", 20, "Pune")
print("Packed Tuple:", student_info)
print("-" * 30)

# Unpacking the tuple into 3 separate variables
(name, age, city) = student_info

print("--- After Unpacking ---")
print("Student Name:", name)
print("Student Age:", age)
print("Student City:", city)
