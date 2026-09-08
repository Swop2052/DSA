"""
Topic: Accessing List Items (Indexing)
Description: List items are indexed, meaning you can access them by their position number.
The first item has index 0, the second index 1, and so on.
Negative indexing means starting from the end (-1 is the last item).
"""

# Initial list of student marks
marks = [78, 85, 92, 67, 74]
print("Full List:", marks)
print("-" * 20)

# Access and print the very first mark (Index 0)
print("First mark (Index 0):", marks[0])

# Access and print the third mark (Index 2)
print("Third mark (Index 2):", marks[2])

# Access and print the last mark using negative indexing (Index -1)
print("Last mark (Index -1):", marks[-1])