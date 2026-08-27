# class.py
# Topic: Class basics - attributes + method
#
# Attributes (name, heigh, weight) start as None. speak() is a
# method: its first parameter must be self. The class only DEFINES
# the blueprint here - nothing is printed until an object is created
# and speak() is called (no object is created in this file).

class human:
    name= None
    heigh=None
    weight= None

    def speak(self):
        print("speaking")
        print (self.name)
        