# poly.py
# Topic: Polymorphism - overloading (simulated) + overriding
#
# OVERLOADING: Python does not truly overload - the LAST method with
# a name wins. say_name(name, lastname="Dutta") has a default, so it
# can be called with one OR two arguments (that is Python's version).
# OVERRIDING: a child redefines a parent method (see the commented
# section below the separator).

#method overloading 
class MathClass:
    def add (self, a, b):
        return a+b           # works with ints AND floats


obj=MathClass()
print(obj.add(5,5))          # 10
print (obj.add(2.2,3.3))     # 5.5



class Person:
    def say_name(self,name):
        print("Hi", name)              # overwritten - never runs

    def say_name(self, name,lastname="Dutta"):   # the real one
        print ("Hi", name, lastname)

obj2=Person()

obj2.say_name("om", "gutty")     # Hi om gutty


# overridding. 
