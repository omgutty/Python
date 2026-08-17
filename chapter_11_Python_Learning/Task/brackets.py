"""Difference between () [] {} in Python — study reference.

Three bracket types, three different meanings:
  []  -> List
  ()  -> Tuple  (also: function calls, grouping, generators)
  {}  -> Dict   (also: set, when non-empty)
"""

######################################
# []  -> LIST
######################################
# Ordered, MUTABLE (can change), allows duplicates.

nums = [1, 2, 3]
nums.append(4)       # [1, 2, 3, 4]
nums[0] = 99         # change an element -> [99, 2, 3, 4]
print("list:", nums)

# Also used for indexing / slicing:
text = "hello"
print("index [0]:", text[0])       # h
print("slice [1:]:", text[1:])     # ello

######################################
# ()  -> TUPLE
######################################
# Ordered, IMMUTABLE (cannot change once created), allows duplicates.

t = (1, 2, 3)
print("tuple:", t)
# t[0] = 99   # ❌ TypeError: 'tuple' object does not support item assignment

# But () is ALSO used for other things:
# 1. Function calls
print("function call:", len("abc"))          # 3

# 2. Grouping expressions (no tuple created, just maths grouping)
result = (2 + 3) * 4
print("grouping:", result)                   # 20

# 3. Generator expressions (lazy sequence, NOT a tuple)
gen = (x * 2 for x in range(5))
print("generator:", list(gen))               # [0, 2, 4, 6, 8]

# Gotcha: (1) is just the integer 1, not a tuple!
print("(1) is:", (1))                        # 1
print("(1,) is:", (1,))                      # (1,)  <- comma makes it a tuple

######################################
# {}  -> DICT
######################################
# Key-value pairs, MUTABLE, keys must be unique, insertion order kept (3.7+).

person = {"name": "Tan", "age": 25}
person["age"] = 26          # update value
print("dict:", person)
print("dict value:", person["name"])         # Tan

# BUT {} is also used for SETS — non-empty curly braces = set.
s = {1, 2, 3}
print("set:", s)

# The classic gotcha: {} alone is an EMPTY DICT, not a set!
empty = {}
print("type of {}:", type(empty))            # <class 'dict'>
empty_set = set()                            # correct way to make an empty set
print("type of set():", type(empty_set))     # <class 'set'>

######################################
# SUMMARY TABLE
######################################
# | Brackets     | Name    | Ordered? | Mutable? | Duplicates? | Used for             |
# |--------------|---------|----------|----------|-------------|----------------------|
# | []           | List    | yes      | yes      | yes         | collection of items  |
# | ()           | Tuple   | yes      | no       | yes         | fixed collection,    |
# |              |         |          |          |             | function calls,      |
# |              |         |          |          |             | grouping, generators |
# | {}           | Dict    | yes(3.7+)| yes      | keys no,    | key -> value pairs   |
# |              |         |          |          | values yes  |                      |
# | {} non-empty | Set     | no       | yes      | no          | unique items         |
#
# Interview tie-in:
#   list vs tuple  -> mutable vs immutable
#   dict vs set    -> key-value pairs vs unique values only
