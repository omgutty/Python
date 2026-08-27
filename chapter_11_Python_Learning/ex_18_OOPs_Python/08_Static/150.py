# 150.py
# Topic: Static method - utility function on the class
#
# sum() is static: it takes a, b and returns a value. No self,
# so it can be called directly on the class name. Perfect for
# pure helper functions that don't need object state.

class OClassName:
    @staticmethod
    def sum(a, b):
        return a + b

print(OClassName.sum(4,5))   # 9 (called on the class, no object)