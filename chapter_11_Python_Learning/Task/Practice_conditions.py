# This program practises CONDITIONS: if/else and match-case.
# if/else lets the program make decisions based on a True/False check.

# Ask the user for their age and turn the typed text into an int.
age = int (input("Enter the age"))

if age >=21:   # if the age is 21 or more -> allowed
    print("you are fine ")
else:          # otherwise (age is below 21) -> not allowed
    print("you are below age ")


age= int(input ("Enter the age \n").strip())# strip will remove extra spaces

if age<=0 or age>13:   # invalid age (0 or less, or older than 13)
    print("yes you can go to club")
else:                  # age is between 1 and 13
    if age>=21:        # this inner check can never be True here
        print("above 21")
    else:
        print("belo 21")

    print("you can not go to club")


print("Enter the which Test you want to run")
test_type  = input("Enter the Test Type : API, UI, Performance, Security ")

# match-case works like a switch: compare one value against several cases.
match test_type:
    case "API":
        print("We are running a POSTMAN API Testcase.")
    case "UI":
        print("We are running a Selenium Testcase.")
    case "Performance":
        print("We are running a  Performance Testcase.")
    case "Security":
        print("We are running a  Security Testcase.")
    case _:              # _ is the default case: anything not listed above
        print("Invalid Type.")

        # for invalid case we have  to add _ 
        