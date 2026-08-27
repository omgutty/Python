class Person:
    name= None
    age= None
    phone= None

    def __init__(self):
        print("let take the user input, pleaes enter name, age phone")
        self.name= input("Enter name \n")
        self.age= input("Enter age \n ")
        self.phone= input("Enter phone number \n")

    def displayvalue(self):
        print("Name is : ", self.name, "Age is : ", self.age , "Phone number is : ", self.phone)


siva= Person()
siva.displayvalue()

siva= Person()
siva.displayvalue()