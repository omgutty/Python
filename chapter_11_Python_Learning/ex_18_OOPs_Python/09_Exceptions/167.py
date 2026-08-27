# 167.py
# Topic: Custom exceptions + raise built-in errors
#
# You can create YOUR OWN exception type by subclassing Exception.
# check_zero_div raises a BUILT-IN error with a custom message.
# can_you_drink(17) would raise InvalidAgeException (age < 18).
# can_you_drink(25) is fine (no error).

class InvalidAgeException(Exception):   # custom error type
    pass


def check_zero_div(a):
    if a == 0:
        raise ZeroDivisionError("Can't divide with zero")


def can_you_drink(age):
    if age < 18:
        raise InvalidAgeException("Invalid age of drinking")   # custom error


can_you_drink(17)   # ❌ would raise InvalidAgeException
can_you_drink(25)   # ✅ passes silently