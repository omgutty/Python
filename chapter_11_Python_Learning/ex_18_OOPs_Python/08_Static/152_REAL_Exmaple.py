# 152_REAL_Exmaple.py
# Topic: Static methods - real-world reusable readers
#
# ExcelReader and MYSQLDBConnection expose STATIC methods, so any
# test class can call them WITHOUT creating an object. TC1 and TC2
# reuse the exact same reader code - write once, call anywhere.
# This is the "utility" pattern: no state, just behaviour.

class ExcelReader:
    @staticmethod
    def readExcelFile():
        print("Reading from Excel")

class MYSQLDBConnection:

    @staticmethod
    def readMySQLFile():
        print("Reading from MySQL")


class TC1:

    def runTC(self):
        ExcelReader.readExcelFile()           # static call, no object
        MYSQLDBConnection.readMySQLFile()
        print("Hi")

class TC2:

    def runTC(self):
        ExcelReader.readExcelFile()
        MYSQLDBConnection.readMySQLFile()
        print("Hi")

tc1 = TC1()
tc2 = TC1()
tc1.runTC()
tc2.runTC()