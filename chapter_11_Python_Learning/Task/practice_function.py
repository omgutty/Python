def student():
    print ("Hi ")

student()



def student (name):
    print ("Hi ",name)


student("Kittu")
#student() # this gives argument missing  

def sum(a,b):
    return a+b

print(sum(4,5))


def default(name="om"):
    print ("Hi ", name)


default("kittu")
default()

def math_operator(a,b):
    return a+b, a-b,a*b

result= math_operator(3,5)
print(result) #(8,-2,15)
a,s,m= math_operator(5,8)
print(a,s,m) # 13 -3 40


def make_pizza(*topping):
    print(topping)

make_pizza("a", "b")
# unsure about the number of arguments are parameter are using 

def printmul(*arg):
    for i in arg:
        print(i)


printmul("a")
printmul("a","b")

###########
#local variable 

pb_gloabl=12
def myfunction():
    pb_a=10
    print(pb_a)
    print(pb_gloabl)
    print(pb_a)

myfunction()
print(pb_gloabl)
#print(pb_a)

#before definition we cant call function 



