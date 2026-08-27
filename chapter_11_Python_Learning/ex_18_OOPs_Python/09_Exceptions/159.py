# 159.py
# Topic: Unhandled ZeroDivisionError from user input
#
# The user's numbers go straight into a/b. If b is 0, the program
# CRASHES with ZeroDivisionError (nothing catches it).
# Compare with 160.py which wraps it in try/except.

a = int(input("Enter num 1"))
b = int(input("Enter num 2"))
c = a/b
print(c)
# ZeroDivisionError