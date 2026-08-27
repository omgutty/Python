from abc import ABC, abstractmethod


class context(ABC):

    @abstractmethod
    def readconfig(self):
        pass

class browser(context):

    @abstractmethod
    def startbrow(self):
        pass

    @abstractmethod
    def closebrow(self):
        pass


class Testcase1(browser):

    def readconfig(self):
        print ("reading the config ")
    
    def startbrow(self):
        print("start browser")

    def closebrow(self):
        print ("close browser")

    def runtc(self):
        self.readconfig()
        self.startbrow()
        self.closebrow()

tc1= Testcase1()
tc1.runtc()