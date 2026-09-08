"""
Topic: Sorting a List (sort)
Description: The sort() method arranges the items in the list in order.
By default, it sorts in Ascending order (smallest to largest).
We can pass 'reverse=True' to sort in Descending order (largest to smallest).
"""

# Example 1: Ascending Order
marks1 = [78, 85, 92, 67, 74]
print("Original List 1:", marks1)

# Sort from smallest to largest
marks1.sort()
print("Ascending Order (Smallest to Largest):", marks1)
print("-" * 40)

# Example 2: Descending Order
marks2 = [78, 85, 92, 67, 74]
print("Original List 2:", marks2)

# Sort from largest to smallest using reverse=True
marks2.sort(reverse=True)
print("Descending Order (Largest to Smallest):", marks2)