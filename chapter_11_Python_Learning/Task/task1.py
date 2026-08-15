
"""
# Task for the Today
# Take a 3 input from the user
# perform the add, sub, mul and div


"""

# This program takes 3 numbers from the user and does add, subtract,
# multiply and divide on them. Two different solutions are shown.

# Task one - solution 1
# input() asks the user to type something; float() turns it into a decimal number.
a= float(input ("enter first  numbers :"))
b= float(input("enter second number :"))
c= float(input("enter third number :"))

print("Addition of three numbers:" +str(a+b+c))          # + joins text; str() turns a number into text
print("subtraction  of three numbers:" +str(a-b-c))
print("multiplication  of three numbers:" +str(a*b*c))
print(f"Division:       {a / b / c:.2f}")  # :.2f rounds to 2 decimals

# solution 2
# Same task, but this time the division checks for dividing by zero.

a = float(input("enter first number: "))
b = float(input("enter second number: "))
c = float(input("enter third number: "))

add = a + b + c
sub = a - b - c
mul = a * b * c

if b==0 or c==0:   # dividing by zero is not allowed in maths
    print ("Division : not possible (divide by zero)")
else:
    print(f"Division: {a/b/c:.2f}")  # which gives us with 2 decimals