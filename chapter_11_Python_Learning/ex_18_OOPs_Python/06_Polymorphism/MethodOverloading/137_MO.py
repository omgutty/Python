# 137_MO.py
# Topic: Method Overloading - Python does NOT support true overloading
#
# In languages like Java you can define add(a,b) and add(a,b,c) and
# both exist. In Python the LAST definition of a method WINS - earlier
# ones are overwritten. So only the second add() exists here.
# Note: the second add actually SUBTRACTS - a classic "gotcha" example.
# (True "overloading" in Python is simulated with default parameters -
# see 139_MO.py.)

class MathClass:
    # def add(self, a,b):
    #     return a+b      # overwritten by the definition below!

    def add(self,a,b):
        return a-b        # this is the ONLY add() that exists

obj_ref = MathClass()
print(obj_ref.add(3,4))        # -1  (3 - 4, NOT 7!)
print(obj_ref.add(3.12,4.45))  # -1.33 (floats work too)