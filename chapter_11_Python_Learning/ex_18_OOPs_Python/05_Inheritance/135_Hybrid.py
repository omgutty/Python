# 135_Hybrid.py
# Topic: Hybrid Inheritance
#
# A MIX of multiple inheritance and multilevel inheritance.
# Class hierarchy here:
#
#         Base
#        /    \
#       A      B        <- A and B both inherit from Base (hierarchical)
#        \    /
#          C            <- C inherits from A AND B (multiple)
#
# C gets: base_method (via A->Base), a_method (A), b_method (B), c_method (C)

class Base:
    def base_method(self):
        print("Base method")


class A(Base):          # A -> Base (single inheritance)
    def a_method(self):
        print("A method")


class B(Base):          # B -> Base (single inheritance)
    def b_method(self):
        print("B method")


class C(A, B):          # C -> A and B (multiple inheritance)
    def c_method(self):
        print("C method")


obj = C()
obj.base_method()  # from Base (via A)
obj.a_method()     # from A
obj.b_method()     # from B
obj.c_method()     # from C itself
