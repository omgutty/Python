# This program practises FUNCTIONS: defining them, calling them,
# and using parameters, return values and default values.

def student():           # define a function called student (no parameters)
    print ("Hi ")

student()                # call (run) the function


# A function can take parameters - values we pass in when calling it.
def student (name):
    print ("Hi ",name)


student("Kittu")
#student() # this gives argument missing  

# return sends a value back out of the function.
def sum(a,b):
    return a+b

print(sum(4,5))  # 4 + 5 = 9


# A default value is used when we call the function without that argument.
def default(name="om"):
    print ("Hi ", name)


default("kittu")   # uses "kittu"
default()          # no argument given -> uses the default "om"

# A function can return several values - Python packs them into a tuple.
def math_operator(a,b):
    return a+b, a-b,a*b

result= math_operator(3,5)
print(result) #(8,-2,15)
# Unpacking: put the three returned values into three variables.
a,s,m= math_operator(5,8)
print(a,s,m) # 13 -3 40


# *topping means "accept any number of arguments" - they arrive as a tuple.
def make_pizza(*topping):
    print(topping)

make_pizza("a", "b")
# unsure about the number of arguments are parameter are using 

def printmul(*arg):
    for i in arg:      # loop through every argument we received
        print(i)


printmul("a")
printmul("a","b")

###########
#local variable 
# A variable created INSIDE a function is local - only that function sees it.

pb_gloabl=12           # global variable: visible everywhere
def myfunction():
    pb_a=10            # local variable: only exists inside this function
    print(pb_a)
    print(pb_gloabl)   # a function CAN read a global variable
    print(pb_a)

myfunction()
print(pb_gloabl)
#print(pb_a)           # ERROR: pb_a is local, unknown outside the function

#before definition we cant call function 



