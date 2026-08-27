# 154_Ex.py
# Topic: Class methods + static methods + access modifiers
#
# Class attributes (counter) are shared by every object.
# @classmethod receives cls (the CLASS) instead of self - useful for
# working with class-level data. @staticmethod receives neither.
# This example also shows public / protected / private attributes.

a = 10
class Counter:
    counter = 0  # class attribute, shared by all

    def __init__(self, name):
        self.name = name              # public
        self.__name_private = name    # private (name-mangled)
        self._name_protected = name   # protected

    @classmethod
    def total(cls):                   # class method - gets cls
        return cls.count              # reads the CLASS attribute

    @staticmethod
    def is_valid(name):               # static method - gets nothing extra
        return bool(name.strip())     # True if name has non-space chars