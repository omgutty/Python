# 136_PPP.py
# Topic: Public / Protected / Private (PPP) - full example
#
# Python naming convention for access levels:
#   self.name      -> PUBLIC   (accessible everywhere)
#   self._name     -> PROTECTED (accessible, but "internal use")
#   self.__name    -> PRIVATE  (name-mangled, hidden from outside)
#
# NOTE: `self.__api__key` has DOUBLE underscores BOTH sides.
# That is a DUNDER (magic) name - it is NOT name-mangled!
# Double underscore on both sides = special/reserved, NOT a private marker.

class TestExample:
    def __init__(self):
        self.driver = "Chrome"          # public
        self._config = "STAG"           # protected
        self.__api__key = "ABC12345"    # dunder name - NOT private

    def show(self):
        print(f"Driver: {self.driver}")
        print(f"Config: {self._config}")
        print(f"API Key: {self.__api__key}")

    # Private methods - can only be called from inside the class
    def __private_method1(self):
        pass

    def __private_method2(self):
        pass

    # Public method that internally uses the private methods
    def work(self):
        self.__private_method1()
        self.__private_method2()


obj = TestExample()
obj.show()   # prints all three values
obj.work()   # calls the private methods internally

# Access levels:
# print(obj.driver)          # ✅ Public — accessible
# print(obj._config)         # ⚠️ Protected — accessible but discouraged
# print(obj.__api__key)     # ❌ AttributeError — private
