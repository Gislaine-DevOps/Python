# Writing a program with the largest and smallest values in a list
# Creating a list
list = [[3, 4, 5, 6], [-1, -2, -3, -4], [0, 0, 0, 0], []]

# Finding the largest and smallest values in the lists
largest_values= max([3, 4, 5, 6], [-1, -2, -3, -4], [0, 0, 0, 0], [])
smallest_values= min([3, 4, 5, 6], [-1, -2, -3, -4], [0, 0, 0, 0], [])

# Printing the result
for list in list:
    if list:
        largest_values = max(list)
        smallest_values = min(list)
        print(f"{largest_values}, {smallest_values}")
    else:
        print("None")