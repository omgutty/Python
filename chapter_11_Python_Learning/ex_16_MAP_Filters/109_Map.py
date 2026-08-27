# 109_Map.py
# Topic: map() - transform EVERY item
#
# map(function, iterable) applies the function to each element and
# returns an iterator of the SAME length (one output per input).
# Wrap in list() to see it. filter() SELECTS; map() TRANSFORMS.

numbers = [1, 2, 3, 4, 5]

def sq(x):
    return x ** 2

# Map - Apply the fn on each element and give you same size list.

all_number = list(map(sq, numbers))
print(all_number)   # [1, 4, 9, 16, 25]