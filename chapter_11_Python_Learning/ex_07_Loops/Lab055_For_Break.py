# This program shows the break statement inside a for loop.
# break stops the loop completely when it is reached.

# Loop through 0 to 9 (10 numbers in total).
for i in range(0, 10):  # 0 to 9, times -> 10
    # Print the current number.
    print(i)
    # When i reaches 5, stop the loop right here.
    if i == 5:
        break
