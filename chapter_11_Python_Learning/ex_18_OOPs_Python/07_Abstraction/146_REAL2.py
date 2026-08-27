# 146_REAL2.py
# Topic: Abstraction - multiple abstract parents (real-world: Car)
#
# A Car needs an Engine (start/stop) AND a GearBox (setGear).
# Both are abstract: they declare the RULES, no implementation.
# Car inherits from BOTH and implements all three abstract methods.
# drive() orchestrates them. Abstract methods without a concrete
# implementation would make Car uninstantiable -> TypeError.

from abc import ABC, abstractmethod


class GearBox(ABC):
    @abstractmethod
    def setGear(self):     # rule from GearBox
        pass

class Engine:
    @abstractmethod
    def start(self):       # rule from Engine
        pass

    @abstractmethod
    def stop(self):        # rule from Engine
        pass


class Car(Engine,GearBox):   # must implement start, stop, setGear
    def start(self):
        print("Starting")

    def stop(self):
        print("Stop")

    def setGear(self):
        print("Gearbox is ready")

    def drive(self):         # orchestrates all three
        self.start()
        self.setGear()
        self.stop()


tesla = Car()
tesla.drive()