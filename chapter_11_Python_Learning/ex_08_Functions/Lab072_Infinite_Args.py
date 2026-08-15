# This program shows *args: a function that accepts ANY number of arguments.
# The * before the name collects all arguments into a tuple (a list-like value).
def print_mul_arg(*pramod_list):
    # args - List
    # A for loop visits each argument one by one and prints it.
    for i in pramod_list:
        print(i)


# Each call can pass a different number of arguments.
print_mul_arg("pramod")
print_mul_arg(2, 3, 1, 4, 3, 2, 2, 2, 2, 2, 2)
print_mul_arg("pramod", "dutta")
print_mul_arg("pramod", "dutta", "third")
print_mul_arg("pramod", "dutta", "third", 3.14)
print_mul_arg("pramod", "dutta", "third", 3.14, True)