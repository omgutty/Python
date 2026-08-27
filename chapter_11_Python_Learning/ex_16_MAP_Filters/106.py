# 106.py
# Topic: filter() - select items that pass a test
#
# filter(function, iterable) keeps ONLY the items for which the
# function returns True. It returns a filter object -> wrap in
# list() to see the results.
# Here even_num(x) returns True only for even numbers.

nums = [1, 2, 3, 4, 5, 6]

def even_num(x):
    return x%2==0

print(list(filter(even_num, nums)))   # [2, 4, 6]