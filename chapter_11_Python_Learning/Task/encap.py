## hiding the login insidethe object


class applogin:

    def __init__(self, email_arg, password_arg):
        self.email= email_arg
        self.password= password_arg


    def loginmethod(self):
        if self.email=='om.gutty@gmail.com' and self.password=='asdf':
            print("successfull login")
        else:
            print("Login failed")

email= input("Enter email id : ")
password= input("Enter password : ")

validlogin=applogin(email,password)
validlogin.loginmethod()
applogin.loginmethod(validlogin)