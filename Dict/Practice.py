"""
=========================================================
PYTHON DICTIONARY - PRACTICE PROJECTS
=========================================================
"""


# =====================================================================
# PROJECT 1
# =====================================================================
"""
1. Student Record Program

Question:
Create a student dictionary containing:
- name
- age
- subjects as a list
- marks as a tuple

Then print the student name, first subject, and marks.

Concepts:
Dictionary -> List -> Tuple -> Indexing
"""

print("--- 1. Student Record Program ---")

# Solution
student = {
    "name": "Rahul",
    "age": 20,
    "subjects": ["Python", "SQL", "HTML"],
    "marks": (85, 90, 78)
}

# Access dictionary value
print("Name:", student["name"])

# Access first element from list
print("First Subject:", student["subjects"][0])

# Access first mark from tuple
print("First Mark:", student["marks"][0])

print("\n\n") # <--- EXTRA SPACE FOR READABILITY



# =====================================================================
# PROJECT 2
# =====================================================================
"""
2. Student Marks Analysis

Question:
Create a dictionary containing:
- student name
- subjects list
- marks tuple

Find:
- total marks
- highest marks
- number of subjects
"""

print("--- 2. Student Marks Analysis ---")

# Solution
student2 = {
    "name": "Amit",
    "subjects": ["Python", "SQL", "Java"],
    "marks": (85, 92, 78)
}

# Tuple containing marks
marks2 = student2["marks"]

print("Name:", student2["name"])
print("Subjects:", student2["subjects"])

# Calculate total marks
print("Total:", sum(marks2))

# Find highest marks
print("Highest:", max(marks2))

# Count subjects using list length
print("Number of Subjects:", len(student2["subjects"]))

print("\n\n") # <--- EXTRA SPACE FOR READABILITY



# =====================================================================
# PROJECT 3
# =====================================================================
"""
3. College Student Information

Question:
Create a dictionary for a student containing:
- name
- city
- hobbies as a list
- birth year and admission year as a tuple

Print all information.
"""

print("--- 3. College Student Information ---")

# Solution
student3 = {
    "name": "Neha",
    "city": "Pune",
    "hobbies": ["Reading", "Drawing", "Music"],
    "years": (2005, 2024)
}

print("Name:", student3["name"])
print("City:", student3["city"])

# List
print("Hobbies:", student3["hobbies"])

# Tuple
print("Birth Year:", student3["years"][0])
print("Admission Year:", student3["years"][1])

print("\n\n") # <--- EXTRA SPACE FOR READABILITY



# =====================================================================
# PROJECT 4
# =====================================================================
"""
4. Product Information System

Question:
Create a dictionary for a product containing:
- product name
- price
- available colors as a list
- dimensions as a tuple

Then:
- print product name
- print first color
- print width from tuple
- update the price
"""

print("--- 4. Product Information System ---")

# Solution
product = {
    "name": "Laptop",
    "price": 50000,
    "colors": ["Black", "Silver", "Blue"],
    "dimensions": (15, 10, 1)
}

print("Product:", product["name"])

# Access List
print("First Color:", product["colors"][0])

# Access Tuple
print("Width:", product["dimensions"][0])

# Update Dictionary value
product["price"] = 55000

print("Updated Price:", product["price"])

print("\n\n") # <--- EXTRA SPACE FOR READABILITY



# =====================================================================
# PROJECT 5
# =====================================================================
"""
5. Mini Student Management System ⭐

Question:
Create a student dictionary containing:
- name
- age
- subjects -> List
- marks -> Tuple
- address -> Nested Dictionary

Then:
- Print student name
- Print all subjects
- Print first subject
- Print marks
- Print Math marks
- Calculate total marks
- Update city
"""

print("--- 5. Mini Student Management System ⭐ ---")

# Solution
student5 = {
    "name": "Rahul",
    "age": 20,
    
    # List
    "subjects": ["Python", "SQL", "HTML"],
    
    # Tuple
    "marks": (90, 85, 88),
    
    # Nested Dictionary
    "address": {
        "city": "Pune",
        "state": "Maharashtra"
    }
}

# 1. Student name
print("Name:", student5["name"])

# 2. All subjects
print("Subjects:", student5["subjects"])

# 3. First subject
print("First Subject:", student5["subjects"][0])

# 4. Marks
print("Marks:", student5["marks"])

# 5. Math marks
print("Math Marks:", student5["marks"][0])

# 6. Total marks
print("Total Marks:", sum(student5["marks"]))

# 7. Update city
student5["address"]["city"] = "Mumbai"

print("Updated City:", student5["address"]["city"])