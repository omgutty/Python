# 125_IQ.py
# Topic: Default Constructor (no arguments) - IQ question
#
# Here __init__ takes NO arguments (only self).
# It runs automatically each time an object is created.

class Dog:
    name = None   # class attribute
    breed = None

    def __init__(self):
        # Runs automatically on EVERY Dog() creation
        print("I will be called")


# Creating TWO objects -> __init__ runs TWICE -> "I will be called" x2
chow_ref = Dog()
mow_ref = Dog()

# name was never set on the objects -> still None
print(chow_ref.name)
print(mow_ref.name)
