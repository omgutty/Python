# 127_IQ.py
# Topic: Calculator class - methods with arguments and return
#
# A real use of classes: methods take inputs, compute, and RETURN results.
# self is passed automatically - a and b are the real arguments.

class Calc:
    a = None  # class attributes (not really used here, values come from user)
    b = None

    def __init__(self):
        print("DC")  # Default Constructor

    # Methods take a and b -> return the result (pure functions)
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


# Take the two numbers from the user (as float so decimals work)
a = float(input("Enter the value of a"))
b = float(input("Enter the value of b"))

# Create ONE calculator object, reuse it for all 4 operations
object_ref = Calc()

output_sum = object_ref.sum(a, b)
output_sub = object_ref.sub(a, b)
output_mul = object_ref.mul(a, b)
output_div = object_ref.div(a, b)
print(output_sum, output_sub, output_mul, output_div)
