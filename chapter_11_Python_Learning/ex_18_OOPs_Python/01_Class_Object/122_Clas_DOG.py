# 122_Clas_DOG.py
# Topic: Class & Object - Dog example
#
# Blueprint (class) -> attributes (what a dog HAS) + methods (what a dog DOES)
# Object (instance) -> a real dog created from the blueprint.

class Dog:
    # ---------- A) ATTRIBUTES (properties) ----------
    # Data variables of the dog. None = "not set yet".
    name = None
    breed = None
    height = None
    weight = None

    # ---------- B) BEHAVIOURS (methods) ----------
    def bark(self):
        print("Barking")
        # print(name)      # ❌ Error! 'name' is not a local variable
        print(self.name)   # ✅ self.name -> the attribute of THIS dog

    def talk(self):
        print("Talking")


# ---------- CREATING OBJECTS ----------
print("Outside ?")

# Dog()  -> creates a NEW Dog object
# chow   -> object REFERENCE (a variable pointing to that object)
chow = Dog()

# chow.name is still None because we never assigned it.
# To give values we would need a constructor (__init__) - see 02_Constructor.
