# This program shows that assigning a name inside a function creates a LOCAL variable.
# It does NOT change the global variable with the same name.
public_toilet = "PB"


def home():
    # These two are local to home(): they exist only inside this function.
    private_toilet = "PT"
    print(private_toilet)
    # This creates a NEW local variable; the global one stays "PB".
    public_toilet = "LPB"
    print(public_toilet)


home()