# This program demonstrates joining strings with the + sign.
# It also shows str() turning a number into text so it can be joined.
name ="this is big line"
# type() confirms that name is a string (<class 'str'>).
print(type(name))


# str(1) turns the number 1 into text so + can join it to name.
name= name+str(1)
print(name)
print(type(name))


first_name= "Om"
last_name= "gutty"

# Join the names with a space (" ") in between.
fullname= first_name+" " +last_name
print(fullname)
print(type(fullname))