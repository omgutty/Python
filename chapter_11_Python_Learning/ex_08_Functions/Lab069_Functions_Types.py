# This program shows the different types of functions in Python.
# A function is a reusable block of code that runs when we call it.
import math

# built in functions
# max() is a built-in function: it returns the biggest value given to it.
result = max(3, 4)
print(result)

# 1. They can't return -> non return
# No Return Type and No Parameter / Argument - NRNP

def greet():
    print("Hello")

# Call the function to run its code.
greet()

# 2. # No Return Type and with Argument/ Param
def greet_by_name(name):
    print("Hello,", name)


# Passing an argument ("Pramod") to the function's parameter.
greet_by_name("Pramod")

# 3. No Return Type and with Default Argument ( # positional argument)
def say_hello_default_arg(name="Pramod"):
    print("Hello", name.upper())


# .upper() is a built-in string method that makes text ALL CAPS.
say_hello_default_arg("Dutta")
# No value given, so the default "Pramod" is used.
say_hello_default_arg()


# A function can take many arguments, all at once or one by one.
def multiple_args(name1="A", name2="B"):
    print("Mul -> ", name1, name2)


multiple_args()
multiple_args("Lucky", "Sharma")
multiple_args(name1="Pramod")
multiple_args(name1="Dutta", name2="Amit")
multiple_args(name2="Amit")


# def test(name):
#     return name
# test("test")


# 4. Argument + return Type

def sum_of_two(a, b):
    return a + b


# The function returns the sum, which we save into "result".
result = sum_of_two(4, 56)
print(result)


def sum_of_two_number_with_default(num1=100, num2=200):
    print("I will sum the two numbers!")
    return num1 + num2


# Passing values with keywords; both defaults are replaced.
result = sum_of_two_number_with_default(num1=34, num2=34)
print(result)
# No values passed, so the defaults 100 and 200 are used.
result = sum_of_two_number_with_default()
print(result)