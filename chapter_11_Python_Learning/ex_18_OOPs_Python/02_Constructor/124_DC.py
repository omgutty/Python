# 124_DC.py
# Topic: Parameterized Constructor
#
# "DC" = Default Constructor (no args)  vs  "PC" = Parameterized Constructor.
# Here the constructor TAKES arguments so each object starts with its own values.
#
# IMPORTANT: once you define a parameterized __init__(self, ...),
# the default Dog() with NO arguments is GONE -> calling it raises an error.

class Dog:
    # Attributes - Instance variables | Data variables
    name = None
    breed = None
    height = None
    weight = None
    race = None

    # Parameterized Constructor: must pass nameGiven and breedGiven
    def __init__(self, nameGiven, breedGiven):
        print("Param C")
        # self.name = THIS dog's name (instance attribute)
        # nameGiven = the value passed in
        self.name = nameGiven
        self.breed = breedGiven

    def bark(self):
        print("Barking! -> ", self.name)

    def talk(self):
        print("talking")


# Each object gets its OWN name & breed via the constructor
chow = Dog("chow", "mastiff")
chow.bark()

desi = Dog("rancho", "desi")
desi.bark()

# ❌ This will FAIL - we don't have a Default Constructor (no-arg version).
# Dog.__init__ requires 2 arguments, so this raises:
#   TypeError: Dog.__init__() missing 2 required positional arguments
straydog = Dog()
