# This program shows a function that returns several values at once.
# The three results are separated by commas in the return statement.
def math_operations(a, b):
    return a + b, a - b, a * b


# Python unpacks the three returned values into three separate variables.
sum_result, diff_result, mul_result = math_operations(3, 4)
print(sum_result)
print(diff_result)
print(mul_result)