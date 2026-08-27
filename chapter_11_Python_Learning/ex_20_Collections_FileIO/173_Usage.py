# 173_Usage.py
# Topic: __name__ guard with multiple functions
#
# All functions are DEFINED here. Only the __main__ guard decides
# what runs when this file is executed directly. If another file
# imports this one, none of f1/f2/f3/main run automatically.

def f1():
    print("f1")

def f2():
    print("f2")

def f3():
    print("f3")

def main():
    print("main from 173")

if __name__ == "__main__":
    main()
    f1()
    f2()
    f3()