# This program demonstrates logical operators: and, or, not.
# Logical operators work on True/False values and give True/False back.

# Put 5 in a and 10 in b.
a, b = 5, 10
# and is True only when BOTH sides are True.
print(a > 0 and b > 0)  # True
# or is True when AT LEAST ONE side is True.
print(a > 0 or b < 0)   # True
# not flips the answer: True becomes False, False becomes True.
print(not (a > 0))      # False