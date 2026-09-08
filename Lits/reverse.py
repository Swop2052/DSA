"""
Topic: Reversing a List (reverse)
Description: The reverse() method flips the current order of the items in the list.
Important: reverse() does NOT sort from highest to lowest. It just flips it backwards!
"""

# Initial list of student marks
marks = [78, 85, 92, 67, 74]
print("Original Order:", marks)

# Reverse the current order directly
marks.reverse()

print("Reversed Order:", marks)

"""
--- VERY IMPORTANT DIFFERENCE ---
1. sort()
   - Actually arranges values (smallest to largest or vice versa).
2. reverse()
   - Just flips the current left-to-right order to right-to-left.
   - It does NOT mean "sort from highest to lowest".
"""