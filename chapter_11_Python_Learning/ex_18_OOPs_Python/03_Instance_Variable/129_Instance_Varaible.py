# 129_Instance_Varaible.py
# Topic: Variable scopes - Global vs Class/Instance vs Local
#
# Three kinds of variables, three scopes:

a = 10  # GLOBAL variable - visible EVERYWHERE (inside and outside the class)


class Person:
    b = 11  # CLASS variable (aka instance/class attribute, property)
    #  - belongs to the class blueprint
    #  - access it via self.b (or Person.b)
    #  - same value for every object UNLESS overwritten

    def print_infor(self):
        l = 10  # LOCAL variable - only exists inside THIS method
        print(self.b)  # class variable via self

    def talk(self):
        print(self.b)  # class variable - works because it's defined in the class
        print(a)       # global variable - works because globals are visible everywhere


# Try it: create a Person object and call the methods
# p = Person()
# p.print_infor()   # 11
# p.talk()          # 11 then 10

# Key rule:
#   global  -> defined outside the class, visible everywhere
#   class   -> defined inside the class, accessed with self. (or ClassName.)
#   local   -> defined inside a method, dies when the method ends
