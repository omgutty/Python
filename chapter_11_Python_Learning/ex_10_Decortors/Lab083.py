# This program shows two decorators stacked on one function.
# Decorators run from the bottom up: decorator2 wraps the function first, then decorator1.
# @deco applies the decorator: say_hello = decorator1(decorator2(say_hello))
def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper


# @deco applies the decorator: say_hello = decorator1(decorator2(say_hello))
@decorator1
@decorator2
def say_hello():
    print("Hello!")


say_hello()