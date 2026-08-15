# This program demonstrates converting a string into a number.
# The quotes around "90" make it TEXT, not a number.
age="90"
# type() shows the data type: here it is a string (<class 'str'>).
print(type(age))

# int() converts the text "90" into the real number 90.
age= int (age)

# Now type() shows it is an integer (<class 'int'>).
print (type (age))
