# This program demonstrates a lambda function (a nameless, one-line function).
# First we write a normal function, then we do the same job with a lambda.

# A normal function named triple_number: takes num and returns num * 3.
def triple_number(num):
    return num*3

# Call the normal function with 3 and store the answer.
result = triple_number(3)
print(result)  # prints 9


# lambda num: num*3  ==  a nameless function that takes num and returns num*3
result_l_format = lambda num:num*3
print(result_l_format(3))  # prints 9, same answer as the normal function