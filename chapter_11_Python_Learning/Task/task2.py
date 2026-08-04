"""# Task for the Today
# Take a 2 input from the user
# Print the Quotient and Remainder
# 15 ->  num1
# 2 -> num2
# Q -> 7
# R -> 1

// , %"""

# for the quotient and % for the remainder.
a= float(input("Enter first value :"))
b= float(input("Enter second value :"))

quoatient= a//b
remainder= a%b

print("Quotient: ",a)
print("Remainder: ", b)

#solution 2

a= float(input("Enter first value :"))
b= float(input("Enter second value :"))

if a == 0:
    print("Cannot divide by zero")
else:
    print(f"Quotient: {a // b}")
    print(f"Remainder: {a % b}")