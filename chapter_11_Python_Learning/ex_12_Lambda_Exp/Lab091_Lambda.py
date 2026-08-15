# def add(n):
#     return n + 10

# l_add = lambda n:n+10
# print(l_add(30))


# This program compares normal functions with lambda functions.
# A lambda is a tiny nameless function written on one line:
#     lambda arguments: expression

# Normal function: multiply two numbers and return the result.
def mul(a, b):
    return a * b


# lambda a, b: a * b  ==  nameless function that takes a and b, returns a * b
mul_l = lambda a, b: a * b
print(mul_l(3, 4))  # prints 12


# Normal function: add three numbers together.
def sum_three_num(a, b, c):
    return a + b + c


# lambda a, b, c: a + b + c  ==  nameless function that adds three numbers
op_f = lambda a, b, c: a + b + c
print(op_f(3, 4, 5))  # prints 12