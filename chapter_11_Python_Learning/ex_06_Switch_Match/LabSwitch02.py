# This program shows the match statement matching TEXT instead of numbers.
# The user picks a test type, and a matching message is printed.

# Tell the user what to do.
print("Enter the which Test you want to run")
# Ask for the test type as text (a string).
test_type  = input("Enter the Test Type : API, UI, Performance, Security ")

# match checks the text stored in test_type.
match test_type:
    # Each case compares test_type with a piece of text.
    case "API":
        print("We are running a POSTMAN API Testcase.")
    case "UI":
        print("We are running a Selenium Testcase.")
    case "Performance":
        print("We are running a  Performance Testcase.")
    case "Security":
        print("We are running a  Security Testcase.")
    # Default case: runs when none of the text above matches.
    case _:
        print("Invalid Type.")