# util_module.py
# Topic: A module inside the 'package' package
#
# A module is just a .py file. This one defines a function that
# other files import and call. Note: there is also a util_module2.py
# with the SAME function name - both live in separate files, so no
# conflict as long as you call them module.function().

def blah(name):
    print(name)