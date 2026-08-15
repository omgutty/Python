# This program shows the logical operator not and comparison operators.
# A boolean value can only be True or False.

# is_pramod_married is a boolean variable holding True.
is_pramod_married = True
# not flips True to False.
print(not is_pramod_married)
# The original value is still True (not does not change the variable).
print(is_pramod_married)

# Logical Operator -> bool
# > , <  >= <=
x = 10
y = 20
# Is 10 greater than 20? No -> False.
print(x > y)
# Is 10 smaller than 20? Yes -> True.
print(x < y)

print(" --- ")

a = 10
b = 10
# Are the two values equal? Yes -> True.
print(a == b)
# >= means greater OR equal. 10 >= 10 is True.
print(a >= b) # 10 > 10 or 10 = 10