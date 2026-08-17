# 130_Ecap.py
# Topic: Encapsulation (intro) - object carries its own data
#
# Encapsulation = bundling data (attributes) + methods that work on that data
# inside one object, and controlling access to the data.
# Here: each Car object HOLDS its name/make/model and uses them in a method.

class Car:
    name: None
    make: None
    model: None

    # Constructor stores the passed values onto THIS car
    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    # Method uses the object's OWN data (self.xxx)
    def start_engine(self):
        print("Starting a car with the name " + self.name)
        print("Starting a car with the make " + self.make)
        print("Starting a car with the model " + self.model)


# Two independent car objects, each with its own data
lambo = Car("Lambo", "V6", "2023")
lambo.start_engine()

mg_hector = Car("Hector", "1.5+ Turbo", "2024")
mg_hector.start_engine()
