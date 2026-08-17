# 120_Class.py
# Topic: Class & Object basics
#
# A class is a BLUEPRINT / template.
# It has:
#   - Attributes (data variables / properties)  -> what the object "has"
#   - Behaviours (methods / functions)          -> what the object "can do"
#
# An object is a REAL INSTANCE created from the blueprint.

class Person:
    # ---------- ATTRIBUTES (data variables / properties) ----------
    # These describe the object. They start as None (no value yet).
    name = None
    id = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None

    # ---------- BEHAVIOURS (methods) ----------
    # Every method's FIRST parameter must be 'self'.
    # self = "this object" -> a reference to the current instance.
    # Python passes it automatically, you never call it yourself.

    def talk(self):  # No Arg with No Return
        print("I can Talk")

    def sleep(self, name):  # Arg with No Return
        print("I am a Method!!")
        print("Sleep", name)

    def sleep2(self, name):  # Arg with Return
        print("I am a Method!!")
        return None

    def walk(self):
        print("I am walking")

    def method_walk_return(self):  # No Arg with Return
        return "I am walking"


# A function can live OUTSIDE a class too
def function_outside():
    print("Outside")


# ---------- CREATING OBJECTS (instances) ----------
# Person() calls the blueprint and creates a real object.
# Each object is INDEPENDENT - it has its own copy of the attributes.
geeta = Person()
amit = Person()
navita = Person()

# geeta.name is None because we never set it -> prints None
print(geeta.name)  # - A

# Calling a method on the object (self = geeta automatically)
geeta.sleep("pramod")  # - B
