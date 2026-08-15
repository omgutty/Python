# ============================================================
# LAMBDA FUNCTIONS — one-line anonymous functions
# ============================================================
# A lambda is a normal function with NO name, written as a
# single expression. General syntax:
#
#   lambda <parameters> : <expression>
#
# - It CANNOT contain statements (no if/else blocks, no loops)
# - It AUTOMATICALLY returns the expression's value (no "return")
# - It is just a function object — assign it to a name and call it
#
# Every example below pairs a regular function with its lambda
# equivalent, so you can see the 1:1 mapping.
# ============================================================


# ---- 1. One input, one output --------------------------------
# Regular function version:
def multiplication(num):
    return num * 2

result = multiplication(3)
print(result)          # 6

# Same as above with lambda:
#   "lambda num: num*2"  =  a function that takes num and returns num*2
# The lambda itself returns the expression; result_l holds the function.
result_l = lambda num: num * 2
print(result_l(5))     # 10
# NOTE: calling result_l(5) runs the lambda with num=5, returning 5*2=10.


# ---- 2. Multiple inputs ---------------------------------------
# Regular function version:
def mul(a, b):
    return a * b

print(mul(5, 6))       # 30

# Lambda version — same logic, more than one parameter:
#   lambda a, b : a * b    ->  takes a and b, returns a*b
mul_l = lambda a, b: a * b
print(mul_l(5, 7))     # 35


# ---- 3. if/else inside a lambda -------------------------------
# Regular function version (uses a full if/else STATEMENT):
def find_eve_odd(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")

find_eve_odd(5)        # odd

# Lambda version — if/else as an EXPRESSION (ternary):
#   "Even" if num % 2 == 0 else "odd"
# This is the only way to do conditionals in a lambda: the ternary
# operator is an expression (it produces a value), unlike if/else
# which is a statement (lambda is not allowed to contain statements).
user_input = int(input("Enter the number: "))

check_even_odd_l = lambda num: "Even" if num % 2 == 0 else "odd"
print(check_even_odd_l(user_input))


# ---- 4. Gotcha: lambda needs to be CALLED ---------------------
import math

# BUG: this does NOT print 16.0.
# It prints the lambda OBJECT itself, like:
#   <function <lambda> at 0x000001...>
# Because we only built the function and printed it — we never
# called it. print() needs a CALL:
#
#   print((lambda: math.pow(4, 2))())     # 16.0
#
# Parentheses to build the lambda, then () to call it:
#   (lambda: math.pow(4, 2))()
# or store it first and call it, like the examples above.
print(lambda: math.pow(4, 2))

# Correct way (if you want to fix it):
#   power_l = lambda: math.pow(4, 2)
#   print(power_l())
