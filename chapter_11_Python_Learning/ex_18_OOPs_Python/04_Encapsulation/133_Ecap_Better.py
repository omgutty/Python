# 133_Ecap_Better.py
# Topic: Access modifiers - public / protected / private
#
# Encapsulation controls WHO can see WHAT.
# Python uses NAMING CONVENTIONS (no real enforcement):
#   public    name              -> visible anywhere
#   protected _name              -> "internal use", still accessible
#   private   __name             -> name-mangled, NOT directly accessible

class Car:
    def __init__(self):
        self.public_pramod = "pramod"       # public  - anyone can read it
        self._protected_baby = "pass123"    # protected - meant for internal use
        self.__private_baby = "pass123"     # private - hidden from outside

    def nany(self):
        # Created inside a method -> also an instance attribute
        self.__password_yogesh_private = "345"


object_ref = Car()
print(object_ref.public_pramod)  # ✅ public - prints "pramod"
print(object_ref._protected_baby)
#print(object_ref.__private_baby)

object_ref.nany()  # creates the private attribute on the object

# print(object_ref.__password_yogesh_private)
# ❌ AttributeError! Private names are name-mangled:
#    the real name is _Car__password_yogesh_private
# Encapsulation at work: the outside world cannot touch private data.
