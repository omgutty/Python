# 105_Extra.py
# Topic: Set comprehensions + frozenset
#
# Set comprehension: {expression for item in iterable}
#   builds a set with the expression applied to each item.
# frozenset: an IMMUTABLE set - created once, never changed.
#   Useful as a dict key or when you need a constant collection.
#   add()/remove() are NOT available -> they raise AttributeError.

squares = {x ** 2 for x in range(5)}   # {0, 1, 4, 9, 16}
print(squares)

# Frozen Set (Immutable Set)
# A frozenset cannot be changed after creation.
my_list = [1, 2, 3, 3]
fset = frozenset(my_list)              # duplicates removed, then frozen
# fset.add(4)                          # ❌ AttributeError: 'frozenset' object has no attribute 'add'
print(fset)