# 141_MOR.py
# Topic: Method Overriding
#
# A child class redefines a method it INHERITED from its parent.
# LoginTest.run() overrides BaseTest.run(). When you call t.run()
# on a LoginTest object, the CHILD version wins.
# Uncomment the BaseTest line to see the parent's version print.

class BaseTest:
    def run(self):
        print("Running the Base Test")

class LoginTest(BaseTest):
    def run(self):                    # overrides the parent's run()
        print("Runnning Login Test")

# t = BaseTest()    # would print "Running the Base Test"
t = LoginTest()
t.run()             # prints "Runnning Login Test" (child wins)