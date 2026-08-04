
"""
# Task for the Today
# Take a 3 input from the user
# perform the add, sub, mul and div


"""

# Task one - solution 1
a= float(input ("enter first  numbers :"))
b= float(input("enter second number :"))
c= float(input("enter third number :"))

print("Addition of three numbers:" +str(a+b+c))
print("subtraction  of three numbers:" +str(a-b-c))
print("multiplication  of three numbers:" +str(a*b*c))
print(f"Division:       {a / b / c:.2f}")  # :.2f rounds to 2 decimals

# solution 2

a = float(input("enter first number: "))
b = float(input("enter second number: "))
c = float(input("enter third number: "))

add = a + b + c
sub = a - b - c
mul = a * b * c

if b==0 or c==0:
    print ("Division : not possible (divide by zero)")
else:
    print(f"Division: {a/b/c:.2f}")  # which gives us with 2 decimals