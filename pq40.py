'''Check if two lists have at-least one element common
'''
a = [1, 2, 3, 4]
b = [5, 6, 3, 8]

# Find common elements using set intersection
common = set(a) & set(b)

# Check if there are common elements
if common:
    print("Common", common)
else:
    print("Not common.")