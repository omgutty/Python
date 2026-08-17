# 126_USer_Inout_Class.py
# Topic: Constructor taking USER INPUT
#
# The constructor asks the user for values and stores them on self.
# -> the object is built FROM user input.

class Person:
    name = None
    age = None
    phone = None
    occupation = None

    def __init__(self):
        # Runs automatically -> user must type values for every field
        print("Let's take the user input, Please share the name,age,phone,occ")
        self.name = input("Enter the name\n")
        self.age = input("Enter the age\n")
        self.phone = input("Enter the Phone\n")
        self.occupation = input("Enter the occupation\n")

    def display_values(self):
        print("Name is ", self.name, "Age is ", self.age,
              "Phone is", self.phone, "occupation", self.occupation)


# First object -> user enters values once
amit = Person()
amit.display_values()

# Second object -> constructor runs AGAIN, user enters values again
# NOTE: each Person gets its OWN copy of the data
amit = Person()
amit.display_values()
