# This program practises functions with DEFAULT parameter values.
import math  # imports the math module (not used below, but available)

# A simple function with no parameters.
def gree():
    print ("hello ")


gree()  # call the function


# name="om" is a DEFAULT value:
# if you call sayhello() without an argument, name becomes "om".
def sayhello (name= "om"):
    print ("hello ",name.upper())  # .upper() makes the name ALL CAPS

sayhello ("raju")
