# This program shows a decorator: a function that adds extra behaviour to another function.
# The decorator wraps the original function with extra steps before and after it runs.
def add_security(func):
     def wrapper():
        print("1.Before the function is called.")
        print("2.Add Helmet, Dashcash, gloves, knee guards, License")
        # Call the original function that was passed in.
        func()
        print("3.After the function is called.")
        print("4.Secure Driving, Leave all the items")

        return wrapper()

# @add_security applies the decorator: drive_ola_scooter = add_security(drive_ola_scooter)
@add_security
def drive_ola_scooter():
    print("I am driving ola scooter")


drive_ola_scooter()

@add_security
def drvie_zypp_scooter():
    print("Drving Zypp scooter")