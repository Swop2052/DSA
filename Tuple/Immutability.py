"""
Topic: Tuples are Unchangeable (Immutable)
Description: The most important difference between a List and a Tuple is that 
you CANNOT change, add, or remove items after the Tuple has been created.
"""

# Initial tuple of student marks
marks = (78, 85, 92, 67, 74)
print("Original Tuple:", marks)

# Attempting to change a value WILL CAUSE AN ERROR!
print("\n--- Why Tuples are different from Lists ---")
print("If we try to do: marks[0] = 99")
print("Python will throw an error: 'tuple' object does not support item assignment")

# Un-comment the line below to see the error yourself:
# marks[0] = 99

print("\nConclusion: Tuples are completely locked and safe from accidental changes!")
