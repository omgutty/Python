# abs2.py
# Topic: Abstraction - 3-level abstract chain (config/browser/test)
#
# context(ABC)      -> abstract readconfig()
# browser(context)  -> adds abstract startbrow() + closebrow()
# Testcase1(browser)-> implements ALL three -> finally concrete
# Testcase1 can be created because every abstract rule is fulfilled.
# runtc() uses all three in sequence.

from abc import ABC, abstractmethod


class context(ABC):

    @abstractmethod
    def readconfig(self):      # rule level 1
        pass

class browser(context):

    @abstractmethod
    def startbrow(self):       # rule level 2
        pass

    @abstractmethod
    def closebrow(self):       # rule level 2
        pass


class Testcase1(browser):      # implements everything

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