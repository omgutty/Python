# 130_01_SI.py
# Topic: Single Inheritance (SI)
#
# Inheritance = a class (child) REUSES the code of another class (parent).
#   LoginTest(BaseTest)  -> LoginTest is the CHILD of BaseTest
# Child can use the parent's methods AND attributes.

class BaseTest:
    driver = "chrome"    # parent attribute (public)
    __driver2 = "FF"     # parent private attribute -> hidden from the child

    def setUp(self):     # parent method
        print("Base Test Setup done!")


class LoginTest(BaseTest):  # <-- inherits from BaseTest
    def run(self):
        self.setUp()              # ✅ parent's method, called by the child
        print("Running the Testcases -> " + self.driver)  # ✅ parent's attribute
        # self.__driver2 -> ❌ would fail, private is not inherited for access


# Child object -> can call BOTH its own method and the inherited one
t = LoginTest()
t.run()
