# This program shows *args with a real-life example: making a pizza.
# The * collects all toppings into a tuple named "toppings".
def make_pizza(*toppings):
    print(toppings)


# Each pizza can have a different number of toppings.
pramod = make_pizza("cheese","corn")
yoga = make_pizza("cheese","corn","paneer","capsicm")
vinay = make_pizza("tomato")