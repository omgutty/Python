# This program shows which variables each function can see (scope).
# "public_toilet" is global: every function can use it.
public_toilet = "PB"

def home():
    # "private_toilet" is local: it only exists inside home().
    private_toilet = "PT"
    print(public_toilet)
    print(private_toilet)

def stranger():
    # stranger() can see the global variable...
    print(public_toilet)
    # ...but NOT home()'s local variable, so this line is commented out.
    # print(private_toilet)