# collection.py
# Topic: The collections module - namedtuple and Counter
#
# The collections module provides "upgraded" versions of Python's
# built-in containers. Two of the most useful:
#
#   namedtuple('Name', [fields])
#       A tuple whose items you can access by NAME (t.name) instead
#       of only by index (t[0]). Immutable, like a normal tuple.
#
#   Counter(iterable)
#       Counts how many times each item appears in a collection.
#       most_common(n) returns the n most frequent items.
#
# NOTE: `from collections import *` imports everything from the
# module. It works, but the explicit version is better style:
#   from collections import namedtuple, Counter

from collections import *

# -------- 1. TUPLE (plain) --------
# A tuple is an ordered, IMMUTABLE collection - cannot be changed
# after creation. Written with parentheses ().
t=('siva',36, True)   # 3 items: a string, an int, a bool

print(t)              # ('siva', 36, True)

# -------- 2. NAMEDTUPLE --------
# namedtuple('info', ['name', 'age', 'gender']) creates a NEW tuple
# TYPE called 'info' with 3 named fields.
info=namedtuple('info',['name', 'age','gender'])

# info('om', '66', 'Male') builds ONE tuple of that type.
# The values land in the fields in order: name='om', age='66'...
tinfo= info('om','66','Male')

print(tinfo.name)     # 'om' - access by field name (readable!)
print(tinfo)          # info(name='om', age='66', gender='Male')

# -------- 3. COUNTER --------
# Counter('string') counts how many times each character appears.
# It returns a dict-like object: character -> count.
c= Counter('abcderlasdfadsfadsasdf')

# most_common(3) -> the 3 most frequent characters, as (char, count)
# pairs, sorted from most to least frequent.
print(c.most_common(3))



