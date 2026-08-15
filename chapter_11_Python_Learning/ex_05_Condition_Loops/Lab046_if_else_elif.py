# This program finds the biggest (maximum) of three numbers.
# It shows if, elif (else if), and else working together.
# Problem  Find the Max between 3 numbers

# User inputs - num1, num2, num3 -> int
# O/p -> int or String with max number 

# Ask the user for three numbers and store them.
num1 = int(input("Enter the num1\n"))  # 5 , # 10
num2 = int(input("Enter the num2\n"))  # 3 , # 12
num3 = int(input("Enter the num3\n"))  # 2 , # 11

# result = max(num1,num2,num3)
# print(result)
# 5 > 3 and 5 >2 -> 5
# 5 > 3 and 5 >2 ->  5
# num1 > num2 and num1 > num3 -> num1
# num2 > num1 and num2 > num3 -> num2
# num3 - max

# First check: is num1 bigger than (or equal to) both other numbers?
if(num1>=num2 and num1>=num3):
    print(num1)
# If the first check failed, is num2 the biggest?
elif num2>=num3 and num2>=num1:
    print(num2)
# If neither num1 nor num2 was the biggest, num3 must be.
else:
    print(num3)