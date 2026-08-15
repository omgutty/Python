# ============================================================
# TUPLES — immutable ordered collections
# ============================================================
# WHAT IS A TUPLE?
# A tuple is an ordered, IMMUTABLE collection of items.
#   - Ordered     -> items keep their position (index 0, 1, 2, ...)
#   - Immutable   -> once created, you CANNOT change, add or
#                    remove items (no item assignment, no append)
#   - Can hold MIXED types: int, str, bool, float, lists, ...
#   - Created with parentheses: (item1, item2, item3)
#     (commas matter most — parentheses are optional)
#
# TUPLE vs LIST — the key difference:
#   list  = [1, 2, 3]   -> MUTABLE, you can change items freely
#   tuple = (1, 2, 3)   -> IMMUTABLE, read-only once created
# Use a tuple when the data should never change (e.g. coordinates,
# config values, function return values).
#
# COMMON TUPLE OPERATIONS:
#   len(my_tuple)          -> number of items
#   my_tuple[0]            -> first item (indexing, same as list)
#   my_tuple[-1]           -> last item (negative indexing)
#   my_tuple[1:3]          -> slicing (returns a NEW tuple)
#   item in my_tuple       -> check if an item exists (True/False)
#   for x in my_tuple:     -> iterate over items
#   a, b, c = my_tuple     -> "unpacking": assign each item to a var
# ============================================================


# ---- 1. A basic tuple -----------------------------------------
my_tuple = (1, 2, 3)
print(my_tuple)          # (1, 2, 3)

# IMMUTABILITY: this line is a deliberate ERROR example.
# Tuples do not support item assignment — you cannot change
# an element after the tuple exists.
# Uncommenting the next line raises:
#   TypeError: 'tuple' object does not support item assignment
# my_tuple[0] = 12


# ---- 2. Mixed data types --------------------------------------
# A tuple can hold different types in one collection:
#   str ("Pramod"), int (34), bool (True), float (9.8)
info = ("Pramod", 34, True, 9.8)
print(info)              # ('Pramod', 34, True, 9.8)


# ---- 3. Tuple with ONE element (the classic gotcha) ------------
# To create a 1-item tuple you MUST add a trailing comma:  (3,)
# Without the comma, (3) is just the number 3 in parentheses,
# NOT a tuple — parentheses alone do NOT make a tuple, commas do.
single = (3,)
print(type(single))      # <class 'tuple'>

# Compare: (3) with no comma is an int, not a tuple:
#   not_a_tuple = (3)
#   print(type(not_a_tuple))   # <class 'int'>
