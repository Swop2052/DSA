"""
Topic: Counting Occurrences in a List (count)
Description: The count() method returns the number of times a specific value appears in the list.
"""

# Initial list of student marks, notice '85' appears twice
marks = [78, 85, 92, 67, 74, 85]
print("Marks List:", marks)

# Count how many times the mark '85' appears
occurrences = marks.count(85)

print("The mark 85 appears", occurrences, "times in the list.")