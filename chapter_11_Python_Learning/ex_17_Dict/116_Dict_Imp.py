# 116_Dict_Imp.py
# Topic: Build a dict from two lists + merge dicts
#
# dict(zip(keys, values)) pairs the two lists up -> {key: value}.
# zip() stops at the SHORTER list: 4 keys but only 2 values
# -> only 2 pairs are made (the extra keys are dropped).
#
# Merge: dict1 | dict2 (Python 3.9+) combines two dicts.
# .get("a") reads a key SAFELY - returns None (or a default) instead
# of crashing with KeyError when the key is missing.

keys = ["name", "role", "experience", "abc"]
# values = ["Aman", "SDET", 3, 67,90]
values = ["Aman", "SDET"]

my_dict = dict(zip(keys, values))
print(my_dict)   # {'name': 'Aman', 'role': 'SDET'} - experience/abc dropped

# Merge Two Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = dict1 | dict2
print(merged_dict)                 # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(merged_dict.get("a"))        # 1 (safe read)