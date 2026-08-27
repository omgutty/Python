# 139_MO.py
# Topic: Method overloading via defaults (the clean way)
#
# Only ONE add() exists (the second overwrites the first).
# Because c has a default, add() works with 2 OR 3 arguments.
# That is how Python "overloads": one method, flexible signature.

class MathClass:
    def add(self, a, b):
        return a + b            # overwritten below

    def add(self, a, b, c=10):  # the only add() that exists
        return a + b + c        # optional 3rd argument


obj_ref = MathClass()
print(obj_ref.add(3, 4, 5))     # 12  (all three used)
print(obj_ref.add(3.14, 4.14))  # 17.28 (c defaults to 10)