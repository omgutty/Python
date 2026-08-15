# List - Collection  of items
# grocery List - butter, bread, banana, paneer.
# 10th marks - 90,91,92, 78, 56

# This program introduces LISTS - a collection of items stored together.
# A list is written with square brackets [ ] and can hold many values.

my_list = [1, 2, 3]  # Same type of data (int)
# A list can also mix different types: int, bool (True/False), str, float.
my_list2 = [1, True, "Pramod", 12.34]

print(my_list)
print(type(my_list)) # <class 'list'> , []
print(len(my_list))  # len() counts how many items are in the list -> 3
print(my_list[0])    # index 0 = first item -> 1 (counting starts at 0)
print(my_list[2])    # index 2 = third item -> 3
# print(my_list[6]) # IndexError: list index out of range