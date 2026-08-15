# This program shows a function defined INSIDE another function (inner function).
def f1():
    print("Welcome")
    #Step 1- Declare
    def f2():
        print("Hi")
    #Step 2 - Call
    f2()


# Calling f1() also runs the inner f2().
f1()
# f2() is only known inside f1, so calling it here would give an error.
#f2()