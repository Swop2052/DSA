"""
Topic: Packing and Unpacking a Tuple

Definitions:
1. Packing: When we create a tuple and assign multiple values to it, 
   it is called "packing" a tuple. We are packing all items into one single variable.
   Example: student = ("Rahul", 20, "Pune")

2. Unpacking: When we take those values OUT of the tuple and assign them 
   back into individual/separate variables, it is called "unpacking".
   Example: (name, age, city) = student
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
