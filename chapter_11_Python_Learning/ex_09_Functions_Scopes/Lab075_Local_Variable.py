# This program shows the difference between global and local variables.
# A global variable is created outside any function, so every part of the program can see it.
pb_global_b = 12

def my_function():
    # "pb_a" is a local variable: it only exists inside this function.
    pb_a = 10
    print(pb_a)
    # The function can also read the global variable.
    print(pb_global_b)
    

# print(pb_a)
# "pb_a" is local, so it cannot be used here (outside the function).
print(pb_global_b)
my_function()