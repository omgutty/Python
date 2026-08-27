# 118_IQ.py
# Topic: Dict equality
#
# Two dicts are EQUAL when they have the same key->value pairs,
# regardless of ORDER. (dict1 and dict2 hold the same pairs
# written in different order -> True.)
# Since Python 3.7 dicts keep insertion order, but order does NOT
# matter for comparison.

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 2, "a": 1}

print(dict1 == dict2)   # True