# 132_Ecap_NICE.py
# Topic: Encapsulation + env variables (the "NICE" way)
#
# Improvement over 131: the real credentials are NOT hard-coded in the file.
# They live in a .env file, loaded with dotenv.
# The class encapsulates: validation logic + credential lookup.

from dotenv import load_dotenv  # reads variables from a .env file
import os                       # gives access to environment variables


class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        # user input stored on the object
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        load_dotenv()  # load the .env file (once per call here)
        # Compare user input against values stored in the environment
        if self.email == os.getenv("USERNAME") and self.password == os.getenv("PASSWORD"):
            print("Allowed, Login Sucess")
        else:
            print("Login Failed")


email = input("Enter the vwo login email ")
password = input("Enter the vwo login password ")

vwo_object_ref = VWOLoginPage(email, password)
vwo_object_ref.login_confirm()

# NOTE: password is still stored as a PUBLIC attribute (self.password),
# so anyone can read it -> in a real app you would make it private (_password)
print(vwo_object_ref.password)

print(os.name)  # the OS name, e.g. 'nt' on Windows
