# util_module2.py
# Topic: Second module inside the 'package' package
#
# Same function name as util_module.py on purpose - proves that
# same-named functions in DIFFERENT modules do not clash. Call it
# as util_module2.blah(...) to target THIS file.

def blah(name):
    print(name)