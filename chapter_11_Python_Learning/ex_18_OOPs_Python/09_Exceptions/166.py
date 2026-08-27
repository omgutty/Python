# 166.py
# Topic: raise - deliberately throwing an error
#
# raise lets YOUR code create an error on purpose when a condition
# is not met. vwo_login("pramod") would raise an Exception with the
# message "Unauthorized Access!!". vwo_login("admin") returns fine.

def vwo_login(user):
    if user != "admin":
        raise Exception("Unauthorized Access!!")   # intentional crash
    return "Welcome Admin"

# print(vwo_login("pramod"))   # ❌ would raise Exception
print(vwo_login("admin"))      # Welcome Admin