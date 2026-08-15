# This program shows the continue statement inside a for loop.
# continue skips the rest of the current round and jumps to the next number.

# Loop through the numbers 0 to 9.
for number in range(10):
    # If the number is even, skip it and go to the next round.
    if number % 2 == 0:
        continue
    # Only odd numbers reach this line.
    else:
        print(number)