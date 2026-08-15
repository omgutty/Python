# This program shows the match statement (Python's switch-case).
# It turns a day number (1 to 7) into the name of the day.

# Ask the user for a day number and convert it to an int.
day = int(input("Enter day in digit\n"))

# match checks the value of 'day' against the cases below.
match day:
    # If day equals 1, run this case.
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    # The underscore _ is the default: it runs when no case matched.
    case _:
        print("Invalid input")