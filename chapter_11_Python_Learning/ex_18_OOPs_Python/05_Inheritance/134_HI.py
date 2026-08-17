# 134_HI.py
# Topic: Hierarchical Inheritance (HI)
#
# ONE parent, MANY children.
# Both LoginTest and SignupTest inherit from the SAME BaseTest,
# but each child has its OWN extra method.

class BaseTest:
    def setup(self):
        print("Setup from BaseTest")


# Child 1
class LoginTest(BaseTest):
    def run(self):
        print("Running Login Test")


# Child 2 (same parent, different behaviour)
class SignupTest(BaseTest):
    def run(self):
        print("Running Signup Test")


# Both children can use the parent's setup()
LoginTest().setup()     # inherited from BaseTest
LoginTest().run()       # its own method

SignupTest().setup()    # inherited from BaseTest
SignupTest().run()      # its own method
