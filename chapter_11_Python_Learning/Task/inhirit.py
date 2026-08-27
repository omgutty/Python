# inhirit.py
# Topic: Single inheritance - test automation base class
#
# logintest(BaseTest) inherits from BaseTest. The child can call the
# parent's setup() (inherited method) and read the parent's driver
# (inherited attribute). __driver2 is PRIVATE to BaseTest - the child
# cannot access it (name mangling hides it).

class BaseTest:
    driver= "chrome"
    __driver2= "FF"          # private -> hidden from the child

    def setup(self):
        print("Base test setup done")


class logintest(BaseTest):
    def run (self):
        self.setup()         # inherited from BaseTest
        print("Running the test case-->"+self.driver)   # inherited attribute



test= logintest()
test.run()
