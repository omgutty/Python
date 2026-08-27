# 147_REAL_Browser.py
# Topic: Abstraction chain - ExcelReader -> Browser -> TC1
#
# 3 levels of abstraction, each adding more rules:
#   ExcelReader: abstract readFromExcel()
#   Browser(ExcelReader): abstract startBrowser() + stopBrowser()
#   TC1(Browser): implements ALL abstract methods -> finally concrete
# TC1 can be instantiated because every abstract method is overridden.
# runTc() uses all of them in sequence.

from abc import ABC, abstractmethod

class ExcelReader(ABC):

    @abstractmethod
    def readFromExcel(self):
        pass

class Browser(ExcelReader):
    @abstractmethod
    def startBrowser(self):
        pass

    @abstractmethod
    def stopBrowser(self):
        pass


class TC1(Browser):
    def startBrowser(self):
        print("Starting")

    def stopBrowser(self):
        print("Stop")

    def readFromExcel(self):
        print("readFromExcel is ready")

    def runTc(self):
        self.startBrowser()
        self.readFromExcel()
        self.stopBrowser()


tc1 = TC1()
tc1.runTc()