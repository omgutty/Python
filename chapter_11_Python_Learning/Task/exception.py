a = int(input ("enter number 1"))
b= int(input("enter number 2 "))

try:
    c=a/b
    #print (c)
except (ZeroDivisionError,TypeError):
    print("Error because ,devided with zero ")
except ValueError:
    print("value error ")
except Exception as e:
    print (e)
else:
    print(c)
finally:
    print("unexpected error ")

