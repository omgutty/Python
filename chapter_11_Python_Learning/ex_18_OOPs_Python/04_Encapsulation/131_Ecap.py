# 131_Ecap.py
# Topic: Encapsulation - hiding login logic inside the object
#
# The user only calls login_confirm(). The logic of WHAT makes a login
# valid is ENCAPSULATED (hidden) inside the class.
# The email/password are stored on the object, not scattered around.

class VWOLoginPage:
    # Constructor stores user input on the object
    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    # Method that contains the business logic
    def login_confirm(self):
        if self.email == "pramod@gmail.com" and self.password == "pass123":
            print("Allowed to Login")
        else:
            print("Login Failed")


# Take credentials from the user
email = input("Enter the vwo login email ")
password = input("Enter the vwo login password ")

# Build the object with those credentials, then let the object decide
vwo_object_ref = VWOLoginPage(email, password)
vwo_object_ref.login_confirm()
