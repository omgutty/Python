age = int (input("Enter the age"))

if age >=21:
    print("you are fine ")
else:
    print("you are below age ")


age= int(input ("Enter the age \n").strip())# strip will remove extra spaces

if age<=0 or age>13:
    print("yes you can go to club")
else:
    if age>=21:
        print("above 21")
    else:
        print("belo 21")

    print("you can not go to club")


print("Enter the which Test you want to run")
test_type  = input("Enter the Test Type : API, UI, Performance, Security ")

match test_type:
    case "API":
        print("We are running a POSTMAN API Testcase.")
    case "UI":
        print("We are running a Selenium Testcase.")
    case "Performance":
        print("We are running a  Performance Testcase.")
    case "Security":
        print("We are running a  Security Testcase.")
    case _:
        print("Invalid Type.")

        # for invalid case we have  to add _ 
        