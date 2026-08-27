# classpractice2.py
# Topic: Class practice - methods, self, instance attributes
#
# NOTE: walk() is MISSING self - calling om.walk() would fail with
# "walk() takes 0 positional arguments but 1 was given" because
# Python injects the object as the first argument. Every normal
# method needs self as its first parameter.

class human:
    name=None
    age= None

    def talk(self):
        print("human can talk")
        self.name='om'          # sets the INSTANCE attribute
        print(self.name)

    def walk():                 # ❌ missing self -> would crash if called
        print("human can walk")

om=human()

print(om.name)     # None (never set at creation)
om.talk()          # prints "human can talk" then "om"