class BaseTest:
    driver= "chrome"
    __driver2= "FF"

    def setup(self):
        print("Base test setup done")


class logintest(BaseTest):
    def run (self):
        self.setup()
        print("Running the test case-->"+self.driver)



test= logintest()
test.run()
