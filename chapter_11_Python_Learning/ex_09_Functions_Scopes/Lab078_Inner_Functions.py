# This program shows inner functions: functions defined inside another function.
# Each function has its own local variables.
def outer_function():
    var1 = 30 # local

    # inner_function can READ outer_function's local variable var1.
    def inner_function():
        var2 = 90
        print(var1)

    # inner_function2 creates its OWN var1, so it prints 100, not 30.
    def inner_function2():
        var1 = 100
        print(var1)
        # var2 belongs to inner_function, so this line would fail.
        # print(var2)


    inner_function()
    inner_function2()

outer_function()