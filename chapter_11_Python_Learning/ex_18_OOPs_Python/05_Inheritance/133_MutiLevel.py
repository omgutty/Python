# 133_MutiLevel.py
# Topic: Multilevel Inheritance
#
# A chain: TestSuite -> BaseTest -> UITest.
# UITest can use methods from BOTH its direct parent AND the grandparent.
# (Like a family tree: child inherits from parent, parent from grandparent.)

class TestSuite:                       # GRANDPARENT (level 1)
    def info(self):
        print("This is GF - Step 1")


class BaseTest(TestSuite):             # PARENT (level 2) - inherits from TestSuite
    def setup(self):
        print("BaseTest - F - Step 2")


class UITest(BaseTest):                # CHILD (level 3) - inherits from BaseTest
    def run(self):
        self.info()      # ✅ grandparent's method, available through the chain
        self.setup()     # ✅ parent's method
        print("Running Test Case")


test = UITest()
test.run()
