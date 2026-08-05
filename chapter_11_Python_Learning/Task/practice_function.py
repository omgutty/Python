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