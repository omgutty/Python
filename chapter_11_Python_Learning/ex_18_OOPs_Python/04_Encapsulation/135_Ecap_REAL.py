# 135_Ecap_REAL.py
# Topic: Private attributes & private methods (home example)
#
# "Home" with access levels:
#   public_var    -> everyone (father)
#   _protected_var -> family/brother level
#   __private_var  -> only INSIDE the class (baby / wife)
#
# Private methods (__wife) can only be called from INSIDE the class.

class Home:
    def __init__(self):
        self.public_var = "father"      # public
        self._protected_var = "brother" # protected
        self.__private_var = "baby"     # private

    # Public method - anyone can call it
    def mom(self):
        print(self.__private_var)   # ✅ private var readable INSIDE the class
        self.__wife()               # ✅ private method callable INSIDE the class

    # Private method - hidden from the outside
    def __wife(self):
        print("Private Wife")


object_ref = Home()

# object_ref.__wife()
# ❌ AttributeError: '_Home__wife' is not accessible from outside

# object_ref.__private_var
# ❌ AttributeError: private variable hidden from outside

# Only object_ref.mom() works, and it internally uses the private stuff.
