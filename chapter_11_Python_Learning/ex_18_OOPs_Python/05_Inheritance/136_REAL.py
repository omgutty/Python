# 136_REAL.py
# Topic: Inheritance + Constructor + REAL use case (test automation)
#
# Real-world pattern: a BASE test class holds common setup (browser launch),
# and each CHILD test class (login, signup) reuses it.
# The parent's __init__ receives the browser via the child.

class BaseTest:
    def __init__(self, browser):
        self.browser = browser  # stored on the object

    def setup(self):
        print(f"Launching {self.browser}")


# Child 1 - login test. It does NOT define its own __init__,
# so it inherits BaseTest.__init__ -> must pass a browser.
class LoginTest(BaseTest):
    def run_test(self):
        self.setup()                       # parent's method
        print("Running login test...")


# Child 2 - signup test, same parent
class SignupTest(BaseTest):
    def run_test(self):
        self.setup()
        print("Running signup test...")


# Each test object gets its own browser
t = LoginTest("chrome")
t.run_test()

t = SignupTest("firefox")
t.run_test()

# Key idea: the browser-launching logic lives ONCE in the parent.
# Children only add their own specific behaviour (login vs signup).
