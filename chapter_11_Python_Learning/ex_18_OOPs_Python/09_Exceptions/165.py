# 165.py
# Topic: try / except / else / finally - the full order
#
# else runs ONLY if no error happened (the try succeeded).
# finally ALWAYS runs.
# Order: try -> (except if error) -> else (if no error) -> finally.

try:
    a = int(input("Enter num 1"))
    b = int(input("Enter num 2"))
    c = a / b
except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Div Error")
else: # Runs only if try block succeeds.
    print(c)
finally:
    print("I will always execute!")