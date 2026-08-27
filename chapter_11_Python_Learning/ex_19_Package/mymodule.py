# mymodule.py
# Topic: A standalone single module
#
# Compare with the 'package' folder: this is just ONE .py file,
# imported with `import mymodule` (no folder, no __init__.py).
# Call its functions as mymodule.greet(...).

def greet(name):
    return "Hello " + name