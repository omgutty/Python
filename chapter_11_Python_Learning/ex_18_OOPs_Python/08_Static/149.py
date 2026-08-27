# 149.py
# Topic: Static method - call WITHOUT an object
#
# @staticmethod marks a method that does NOT receive self (or cls).
# It behaves like a plain function living inside the class.
# Call it on the CLASS directly: Utility.greet_course_name(...)
# No object needed -> no self injected.

class Utility:

    @staticmethod
    def greet_course_name(name):   # no self!
        print("Hi,", name)


Utility.greet_course_name("PyATB")   # Hi, PyATB