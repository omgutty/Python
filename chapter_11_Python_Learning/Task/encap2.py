from dotenv import load_dotenv  # reads variables from a .env file
import os                       # gives access to environment variables
from pathlib import Path        # lets us build a script-relative path


class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        # user input stored on the object
        self.email = email_arg
        self.password = password_arg1

    def login_confirm(self):
        load_dotenv(Path(__file__).parent / ".env")  # load .env next to this script
        # Compare user input against values stored in the environment
        if self.email == os.getenv("VWO_USERNAME") and self.password == os.getenv("VWO_PASSWORD"):
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
