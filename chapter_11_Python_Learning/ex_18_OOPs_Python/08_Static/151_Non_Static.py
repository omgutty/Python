# 151_Non_Static.py
# Topic: Instance method vs static method in ONE class
#
# div() is an INSTANCE method -> needs self -> needs an object (t).
# sum() is a STATIC method -> no self -> call on the class name.
# Contrast: t.div(...) vs MathOperation.sum(...).

class MathOperation:

    def div(self, a, b):        # instance method (self = the object)
        return a / b

    @staticmethod
    def sum(a, b):              # static method (no self)
        return a + b



t = MathOperation()
print(t.div(10, 10))            # 1.0 (needs the object)

print(MathOperation.sum(10, 10))    # 20 (class name works)