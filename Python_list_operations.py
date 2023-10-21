# Traverse a Python list in reverse order
# Using iterate list elements and 
# insert() method

# Define a list
list1 = [10, 20, 30, 40, 50]

# Print the list
print("Original list: ", list1)

# Create a new list with elements 
# in reverse order
newlist = [] # an empty list
for item in list1:
    newlist.insert(0, item)

# Print the new list
print("List in reverse order:",newlist)
