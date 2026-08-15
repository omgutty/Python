# This program checks the age and adds a validity check first.
# It shows nested if-else: one if inside another if.

# Ask for the age, remove extra spaces with .strip(), and make it an int.
age = int(input("Enter the age\n").strip()) # trim()

# First check: is the age impossible (0 or negative, or over 130)?
if age <= 0 or age > 130:
    print("Enter a valid age")
else:
    # The age is valid. Now check if the person is old enough (21+).
    if age >= 21:
        print("Yes, can go club")
    else:
        print("No, can't go club")