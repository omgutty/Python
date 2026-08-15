# This program demonstrates SETS, plus filter() and map().
# A set is an unordered collection with NO duplicates.

# set() removes duplicate values automatically.
numbers_list = [1, 2, 3, 4, 5, 5]
numbers_set = set(numbers_list)  # {1, 2, 3, 4, 5} - the extra 5 is gone
print(type(numbers_set))  # <class 'set'>
print(numbers_set)


###################
# filter() vs map()
###################

# filter() keeps only the items where the function returns True.
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 8, 10]

# even_num returns True only for even numbers (x % 2 == 0).
def even_num(x):
    return x % 2 == 0

# filter(even_num, num) keeps only even numbers, duplicates included.
print(set(filter(even_num, num)))   # as a set  -> duplicates removed
print(list(filter(even_num, num)))  # as a list -> keeps all duplicates

# NOTE: map() is the sibling of filter() - it TRANSFORMS every item
# (e.g. lambda x: x * 2), while filter() only SELECTS items.

############
