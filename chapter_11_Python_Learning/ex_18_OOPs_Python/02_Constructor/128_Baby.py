# 128_Baby.py
# Topic: Parameterized Constructor + instance method
#
# Simple example: constructor receives a name, method prints it.

class Baby:
    # NOTE: `name: None` is a TYPE HINT (Python >= 3.6).
    # It only says "name should be None-ish/not required" - it does NOT
    # enforce anything. The real value is set in __init__ below.
    name: None

    def __init__(self, nameGiven):
        # Store the passed name onto THIS object
        self.name = nameGiven

    def printName(self):
        print(self.name)


# Two separate babies, each with their own name
b = Baby("gugu")
b2 = Baby("sema")

b.printName()   # gugu
b2.printName()  # sema
