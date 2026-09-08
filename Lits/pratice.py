# Task

# Create a program that takes 5 shopping items from the user and stores them in a List.

# Requirements
# Create an empty List.
# Take 5 item names.
# Add every item using append().
# Print the complete List.
# Print the first item.
# Print the last item.
# Print the total number of items.







# Create an empty shopping List
shopping_list = []

# Take 5 items from the user
for i in range(5):

    # Ask the user for an item
    item = input("Enter shopping item: ")

    # Add the item to the List
    shopping_list.append(item)


# Display the complete List
print("Shopping List:", shopping_list)

# Display the first item
print("First Item:", shopping_list[0])

# Display the last item
print("Last Item:", shopping_list[-1])

# Display the total number of items
print("Total Items:", len(shopping_list))