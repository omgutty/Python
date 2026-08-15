# This program asks the user for their age and checks if they are 18 or older.
# It shows the same check twice: with a normal if-else and with a ternary operator.

# Ask the user for their age, convert the text answer into a whole number (int).
user_age = int(input("Enter your age\n"))

# Normal if-else: run the right block depending on the condition.
if user_age >= 18:
    print("Yes You can go to GOA and vote")
else:
    print("Not you can't go and can't vote")

# Same logic written as a ternary operator (one line instead of four).
print("Yes You can go to GOA and vote" if user_age >= 18 else "Not you can't go and can't vote")