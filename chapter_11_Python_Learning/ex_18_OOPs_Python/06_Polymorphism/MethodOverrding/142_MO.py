# 142_MO.py
# Topic: Method overriding - one base, many behaviours
#
# BaseTest.run() is overridden in BOTH children with different output.
# This is polymorphism: the SAME call (t.run()) behaves differently
# depending on the OBJECT's type.
# Try each of the three object types by uncommenting.

class TestSuite:
    def info(self):
        print("Test suite information")

class BaseTest(TestSuite):
    def setup(self):
        print("Base setup")

    def run(self):
        print("Base test execution")

class LoginTest(BaseTest):
    def run(self):  # overriding
        print("Login test execution")

class APITest(BaseTest):
    def run(self):  # overriding
        print("API test execution")


# t = LoginTest()   # -> Login test execution
# t = APITest()     # -> API test execution
t = BaseTest()      # -> Base test execution
t.run()