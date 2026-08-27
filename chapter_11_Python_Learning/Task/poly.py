#method overloading 
class MathClass:
    def add (self, a, b):
        return a+b


obj=MathClass()
print(obj.add(5,5))
print (obj.add(2.2,3.3))



class Person:
    def say_name(self,name):
        print("Hi", name)

    def say_name(self, name,lastname="Dutta"):
        print ("Hi", name, lastname)

obj2=Person()

obj2.say_name("om", "gutty")


# overridding. 
