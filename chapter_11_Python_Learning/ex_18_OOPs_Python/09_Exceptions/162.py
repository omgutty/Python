# 162.py
# Topic: Multiple except blocks - separate handlers
#
# Each error type gets its OWN handler. Python checks them top-down
# and runs the FIRST matching one. ValueError (bad number text) and
# ZeroDivisionError (b == 0) produce different messages.

try:
    a = int(input("Enter num 1"))
    b = int(input("Enter num 2"))
    c = a / b
    print(c)
except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Div Error")