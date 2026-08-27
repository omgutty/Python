# 144_Abs.py
# Topic: Abstraction - abstract class + abstract method
#
# Father(ABC) is abstract: it can define a rule (loan) that children
# MUST implement, and it cannot be instantiated itself.
# Amit MUST override loan() or Amit also becomes abstract.
# Father.__init__ is inherited by Amit -> name is stored.

from abc import ABC,abstractmethod

class Father(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def loan(self):      # the rule: every child must implement loan()
        pass

class Amit(Father):

    def loan(self):      # Amit fulfils the rule
        print("Giving the 50K loan")

amit = Amit("AMIT SHARMA")
amit.loan()