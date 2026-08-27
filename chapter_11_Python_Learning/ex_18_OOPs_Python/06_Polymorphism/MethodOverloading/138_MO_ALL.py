# 138_MO_ALL.py
# Topic: Simulated overloading with default parameters
#
# Two methods with the SAME name -> the LAST one wins (Python rule).
# Here the second say_name has a DEFAULT for lastname, so it can be
# called with ONE or TWO arguments -> "overloading" in Python style.
# t.say_name("Dutta") -> name="Dutta", lastname="Dutta" (default).

class Person:
    def say_name(self, name):
        print("Hi", name)                 # overwritten - never used

    def say_name(self, name, lastname="Dutta"):   # this one exists
        print("Hi,", name, lastname)


t = Person()
t.say_name("Dutta")   # Hi, Dutta Dutta