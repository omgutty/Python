# This program shows nested if-else: an if inside another if.
# It tells whether a number is negative, even, or odd.
# Find the positive number is even or odd

# Ask the user for a number and remove extra spaces with .strip().
num = int(input("Enter a numner").strip())

# Outer if: check if the number is not negative.
if  num>=0:
    # Inner if: check if the number can be divided by 2 with no remainder.
    if num%2 ==0:
        print("Even")
    # If the remainder is not 0, the number is odd.
    else:
        print("Odd")

# The number is negative, so we print this message instead.
else:
    print("Negative Number!")