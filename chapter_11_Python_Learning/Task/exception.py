# exception.py
# Topic: try / except / else / finally - full error handling
#
# try: the risky division. except: multiple handlers - a tuple for
# (ZeroDivisionError, TypeError), then ValueError, then a catch-all
# Exception. else: runs only if NO error happened (prints c).
# finally: ALWAYS runs last - even on error.

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
    print(c)                # only when no error occurred
finally:
    print("unexpected error ")   # always runs

