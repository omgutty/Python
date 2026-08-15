"""# Task for the Today
# Take a 2 input from the user
# Print the Quotient and Remainder
# 15 ->  num1
# 2 -> num2
# Q -> 7
# R -> 1

// , %"""

# This program takes two numbers and prints the QUOTIENT (//) and
# the REMAINDER (%) of dividing them.

# // gives the quotient, % gives the remainder.
a= float(input("Enter first value :"))
b= float(input("Enter second value :"))

quoatient= a//b   # e.g. 15 // 2 = 7
remainder= a%b    # e.g. 15 % 2 = 1

print("Quotient: ",a)    # NOTE: this prints a (the input), not the quotient
print("Remainder: ", b)  # NOTE: this prints b (the input), not the remainder

#solution 2
# Same task again, but with a zero check to avoid dividing by zero.

a= float(input("Enter first value :"))
b= float(input("Enter second value :"))

if a == 0:
    print("Cannot divide by zero")
else:
    print(f"Quotient: {a // b}")
    print(f"Remainder: {a % b}")