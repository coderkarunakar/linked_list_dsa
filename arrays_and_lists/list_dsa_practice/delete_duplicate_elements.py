# Write a python program to delete all duplicate elements from an list.

def remove_duplicates(lst):
    """
    Remove duplicates from a list and return a new list without duplicates.
    """
    return list(set(lst))

# example usage
my_list = [1, 2, 2, 3, 4, 4, 5]
new_list = remove_duplicates(my_list)
print(new_list)