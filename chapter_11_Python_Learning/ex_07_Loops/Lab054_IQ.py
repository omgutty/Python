# This program shows an if-else INSIDE a for loop.
# It prints a special word when the number is 5.

# Loop through the numbers 0 to 9.
for i in range(0, 10):
    # Check the current number: is it 5?
    if i == 5:
        # Special message for 5.
        print("Five")
    else:
        # For every other number, print the number itself.
        print(i)