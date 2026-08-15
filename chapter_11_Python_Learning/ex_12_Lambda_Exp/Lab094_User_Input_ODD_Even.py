# Write a program to calcuclate even and odd
# def find_even_odd(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")


# This program uses lambdas with user input to check even/odd and find a square.

# Ask the user for a number and convert the text they type into an int.
user_input = int(input("Enter the number"))
# lambda num: "Even" if num % 2 == 0 else "Odd"  ==  nameless function:
# if num divided by 2 leaves 0 remainder -> "Even", otherwise -> "Odd"
check_even_odd_f = lambda num: "Even" if num % 2 == 0 else "Odd"
# Run the lambda with the user's number and print the result.
result = check_even_odd_f(user_input)
print(result)


# Same even/odd check, but written as a one-shot lambda:
# we create the lambda and call it right away with the user's input.
print((lambda num: "Even" if num % 2 == 0 else "Odd")(int(input("Enter the number: "))))


import math  # math module gives us math.pow() for calculating powers
# lambda: ...  ==  a nameless function that takes NO arguments
# It asks for a number and returns that number raised to the power 2 (squared).
op2 = lambda: math.pow(int(input("Enter the number")), 2)
print(op2())