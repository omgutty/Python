# This program shows the membership operators in and not in.
# They check whether something is present inside a string (or a list).

# in checks if 'a' is inside the word 'apple' -> True.
result = 'a' in 'apple'
# 'b' is not inside 'apple' -> False.
result2 = 'b' in 'apple'
# not in checks the opposite: 'b' is NOT in 'apple' -> True.
result3 = 'b' not in 'apple'
# Print all three answers.
print(result)
print(result2)
print(result3)

# Bring in the math module so we can use math functions.
import math

# pi is a number in the math module (3.14159...).
print(math.pi)
# pow(x, y) raises x to the power y: 2 ** 2 = 4.0
print(math.pow(2, 2))
# sin, cos, tan are trigonometry functions (they use radians).
print(math.sin(90))
print(math.cos(90))
print(math.tan(90))

