# This program shows a function with default values for all three parameters.
def sum_three(a=1, b=1, c=1):
    return a + b + c


# No values passed, so all defaults are used: 1 + 1 + 1 = 3
result1 = sum_three()
print(result1)

# Two values passed, "c" keeps its default: 1 + 2 + 1 = 4
result2 = sum_three(1, 2)
print(result2)

# All three values passed: 1 + 2 + 3 = 6
result3 = sum_three(1, 2, 3)
print(result3)

# Keyword arguments: order does not matter: 67 + 10 + 45 = 122
result5 = sum_three(b=67, a=10, c=45)
print(result5)

# Same values in a different order give the same answer.
result6 = sum_three(a=10, b=67, c=45)
print(result6)