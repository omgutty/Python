# This program takes the user's name and greets them.
# Write a Program , take a user name and say Hello to Him

# Ask the user to type their name and store what they typed.
user_input = input("Enter your name\n")


# This function greets whatever name it receives.
def say_your_name(name):
    print("Hi,", name)


# Pass the user's input into the function as the argument.
say_your_name(user_input)