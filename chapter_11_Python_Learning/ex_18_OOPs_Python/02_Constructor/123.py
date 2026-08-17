# 123.py
# Topic: Constructor (__init__)
#
# __init__ is a SPECIAL method that runs AUTOMATICALLY
# the moment an object is created.
# We use it to give the object its starting values.

class MobilePhone:
    model = None  # class attribute (shared, will be overwritten by instance)

    def __init__(self):
        # This runs automatically when MobilePhone() is called
        print("This is Constructor, I will be called when the Object is created!")
        # self points to the current object (this phone)
        # self.model reads the attribute 'model' of THIS object
        print(self.model)  # None at this point (never set)

    def talk(self):
        print("Normal F(n)")


# Creating the object -> __init__ fires automatically:
#   "This is Constructor, ..." and "None" get printed
iphone = MobilePhone()
iphone.talk()  # then we manually call a normal method
