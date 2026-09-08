"""
Topic: Tricky Concept - Tuple with Only One Item
Description: To create a tuple with only one item, you MUST add a comma after the item.
Otherwise, Python will just treat it as a normal variable with parentheses around it.
"""

# Correct way: Add a comma
tuple_with_one_item = ("Apple",)
print("With Comma    :", type(tuple_with_one_item))

# Incorrect way: Missing comma (Python treats it as a String)
not_a_tuple = ("Apple")
print("Without Comma :", type(not_a_tuple))
