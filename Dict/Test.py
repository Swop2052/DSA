# Step 1: Create a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "city": "Pune",
    "marks": 85
}

# Step 2: Access values using keys
print(student["name"])
print(student["marks"])

# Step 3: Find number of key-value pairs
print(len(student))

# Step 4: Add a new key-value pair
student["grade"] = "A"

# Step 5: Update an existing value
student["marks"] = 95

# Step 6: Check whether a key exists
print("city" in student)

# Step 7: Safely get a value
print(student.get("email"))

# Step 8: Get all keys
print(student.keys())

# Step 9: Get all values
print(student.values())

# Step 10: Get key-value pairs
print(student.items())

# Step 11: Add/update multiple values
student.update({
    "course": "Python",
    "college": "ABC College"
})

# Step 12: Nested dictionary
student["marks_detail"] = {
    "math": 90,
    "science": 85,
    "english": 88
}

# Access nested value
print(student["marks_detail"]["math"])

# Step 13: Dictionary containing a list
student["subjects"] = ["Python", "SQL", "HTML"]

# Access list inside dictionary
print(student["subjects"][0])

# Final student record
print(student)