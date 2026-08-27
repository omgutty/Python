# 171.py
# Topic: collections module - Counter and defaultdict
#
# collections holds "better versions" of built-in containers.
#   Counter(iterable)     -> counts how many times each item appears
#   defaultdict(factory)  -> a dict that AUTO-CREATES missing keys
# The factory decides the default value: list, int, set, or a lambda.

from collections import *
# list -> coCollection of items
# tuple -> list but can't modified
# set ->  no duplicates
# dict -> key and value pair

# ++ version of the in built, better version of the inbuilt
# t = tuple(34, True, 123)


# info = namedtuple('info', ['name', 'age', 'ismarried', 'number'])
# t = info('pramod', 34, True, 9.8)
# print(t)

# print(t.name)
# print(t.age)
# print(t.ismarried)
# print(t.number)

c = Counter('abcdeabcabcdaba')  # count elements from a string
print(c.most_common(3))    # top 3 most frequent (letter, count)
print(c.total())           # total number of items counted

from collections import defaultdict

groups = defaultdict(list)        # missing key -> new empty list
for word in ["apple", "avocado", "banana"]:
    groups[word[0]].append(word)  # auto-creates 'a', 'b' lists

counts  = defaultdict(int)   # missing -> 0
uniques = defaultdict(set)   # missing -> set()
nested  = defaultdict(lambda: defaultdict(int))   # missing -> new dict
print(counts)