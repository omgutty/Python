# 160.py
# Topic: try / except - catching ONE specific error
#
# try: the risky code. If a ZeroDivisionError happens, the program
# does NOT crash - control jumps to the matching except block.
# Any other error would still crash (only ZeroDivisionError is caught).

a = int(input("Enter num 1"))
b = int(input("Enter num 2"))

try:
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Error becoz of the zero div b !=0")