# 161.py
# Topic: try / except - catching MULTIPLE error types at once
#
# except (TypeError, NameError, ValueError, ZeroDivisionError):
# catches ANY of these four with ONE handler. A tuple in the
# except clause = "catch any of these".

try:
    a = int(input("Enter num 1"))
    b = int(input("Enter num 2"))
    c = a / b
    print(c)
except (TypeError, NameError, ValueError, ZeroDivisionError):
    print("Error Due to the Type,Name, Value or Zero Div!")