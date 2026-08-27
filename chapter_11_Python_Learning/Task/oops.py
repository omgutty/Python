# oops.py
# Topic: OOP practice - class, objects, methods
#
# NOTE: the methods use 's' instead of 'self' - the NAME does not
# matter, only the POSITION. The first parameter always receives the
# object, so s.name works exactly like self.name. ('self' is just a
# convention.)
# Two objects (siva, om) are created; each is independent.

class person:
    name= None
    id=None
    age= None


    def talk(s):                  # 's' receives the object (like self)
        print("I can talk")

    def sleep(s, name):           # 's' = object, name = real argument
        print("I can sleep ")
        print("sleep", name)

    # def sleep(s,name):
    #     print ("I can sleep 2 ")
    #     return None

def functionoutsite():
    print ("output")

siva= person()
om= person()

print (siva.name)      # None (never set)
om.sleep("omk")        # "I can sleep" then "sleep omk"

