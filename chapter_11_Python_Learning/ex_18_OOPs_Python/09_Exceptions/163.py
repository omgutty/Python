# 163.py
# Topic: try / except / finally
#
# finally ALWAYS runs - whether an error happened or not.
# Typical use: cleanup (close a file, close a browser, release a
# connection) that must happen no matter what.

try:
    a = int(input("Enter num 1"))
    b = int(input("Enter num 2"))
    c = a / b
    print(c)
except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Div Error")
finally:
    print("I will always execute!")