# This program demonstrates a simple if-else condition.
# It checks the user's age and prints a different message for each case.

# Ask the user for their age and convert it to a whole number (int).
age = int(input("Enter the age\n"))

# if the condition (age >= 21) is True, run the if block.
if age >= 21:
    print("Yes, can go club")
# Otherwise (condition is False), run the else block.
else:
    print("No, can't go club")