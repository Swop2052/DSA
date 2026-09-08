"""
Topic: Practice - Shopping List
Description: A practical exercise that takes 5 shopping items from the user,
stores them in a list, and performs basic operations.
"""

# TASK REQUIREMENTS:
# 1. Create an empty List.
# 2. Take 5 item names from the user.
# 3. Add every item using append().
# 4. Print the complete List.
# 5. Print the first item.
# 6. Print the last item.
# 7. Print the total number of items.

print("--- Welcome to the Shopping List Manager ---")

# Step 1: Create an empty shopping List
shopping_list = []

# Step 2 & 3: Take 5 items from the user and append them
for i in range(5):
    # Ask the user for an item
    item = input(f"Enter shopping item {i+1}: ")
    # Add the item to the List
    shopping_list.append(item)

print("\n--- Summary ---")
# Step 4: Display the complete List
print("Shopping List:", shopping_list)

# Step 5: Display the first item
print("First Item:", shopping_list[0])

# Step 6: Display the last item
print("Last Item:", shopping_list[-1])

# Step 7: Display the total number of items
print("Total Items:", len(shopping_list))