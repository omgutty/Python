"""# Create a program to sum of three number from the user input,

# if user doesn't enter any number', use default as 100, 200, 300

# Logic Building

# Step 1 - I/O and O/P

# I/O -  int

# O/P - int

# Step 2 - Rough Logic

# return n1+n2+n3
#  """
# This program sums three numbers from the user. If the user leaves a
# box empty, a DEFAULT value (100, 200 or 300) is used instead.

a = input("Enter first number : ")
b = input("Enter second number : ")
c = input("Enter third number : ")

# Function with default values: used when we call it without arguments.
def sum_of_three(a=100, b=200, c=300):
    return a + b + c

# "int(a) if a else 100" means: if a is not empty, use int(a), else 100.
print(sum_of_three(
    int(a) if a else 100,
    int(b) if b else 200,
    int(c) if c else 300,
))

#  Option 2 — cleaner (small helper, avoids repetition):

# A helper function: asks the user, and returns the DEFAULT
# if they type nothing (or only spaces).
def get_number(prompt, default):
    value = input(prompt).strip()
    return int(value) if value else default

def sum_of_three(a=100, b=200, c=300):
    return a + b + c

a = get_number("Enter first number : ", 100)
b = get_number("Enter second number : ", 200)
c = get_number("Enter third number : ", 300)

print(sum_of_three(a, b, c))

#  Option 3 — robust (survives garbage input like "abc", not just empty):

# def get_number(prompt, default):
#     value = input(prompt).strip()
#     if not value:
#         return default
#     try:
#         return int(value)
#     except ValueError:
#         print(f"'{value}' is not a number, using default {default}")
#     return default