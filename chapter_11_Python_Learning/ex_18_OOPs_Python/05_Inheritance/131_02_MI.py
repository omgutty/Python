# 131_02_MI.py
# Topic: Multiple Inheritance (MI)
#
# A class can inherit from MORE THAN ONE parent.
# TestHybrid gets methods from BOTH APIBase and DBBase.

class APIBase:
    def api_auth(self):
        print("Authenticatin API")


class DBBase:
    def db_connect(self):
        print("Connecting to the DB")


# Child inherits from TWO parents -> has api_auth() AND db_connect()
class TestHybrid(APIBase, DBBase):
    def run(self):
        self.api_auth()      # method from APIBase
        self.db_connect()    # method from DBBase
        print("Test Case Running.")


tc1 = TestHybrid()
tc1.run()
