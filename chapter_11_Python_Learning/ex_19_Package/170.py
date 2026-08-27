# 170.py
# Topic: Importing from a package + a single module
#
# Two import styles side by side:
#   1. PACKAGE: `from package import util_module, util_module2`
#      package/ is a folder marked by __init__.py. We import two
#      MODULES from it, then call module.function().
#   2. SINGLE MODULE: `import mymodule` then mymodule.greet(...).

from package import util_module,util_module2

util_module.blah("dutta")     # function from util_module.py


# This module is a normal Python file where you can directly call the functions.
import mymodule
print(mymodule.greet("pramod"))   # function from mymodule.py
