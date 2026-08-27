# 102.py
# Topic: Sets - the basics
#
# A set is an UNORDERED collection of UNIQUE items, written with {}.
# Key properties:
#   - no duplicates (they are removed automatically)
#   - no order guarantee (do NOT rely on positions like a list)
#   - items must be immutable (numbers, strings, tuples - not lists)
# Use it when you need "a bag of distinct things".

my_set = {1, 2, 3}
print(my_set)   # {1, 2, 3}


my_set_2 = {1, 2, 3, 3}
print(my_set_2)  # Duplicate 3 is removed -> prints {1, 2, 3}


