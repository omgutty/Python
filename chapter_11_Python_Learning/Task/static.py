# static.py
# Topic: Static vs instance methods + default parameter
#
# greet() is STATIC (no self) -> call on the class: utility.greet().
# bye() is an INSTANCE method -> MUST have self first -> needs an
# object: t.bye("Gow"). Calling t.bye("Gow") actually becomes
# utility.bye(t, "Gow"). greet's name="om" is a DEFAULT - used when
# no argument is given (utility.greet() prints "Hi om").

class utility:

    @staticmethod
    def greet(name="om"):
        print ("Hi", name)

    def bye(self, name):
        print ("Bye", name )

utility.greet("siva")    # Hi siva
utility.greet()          # Hi om (default)

t=utility()
t.bye("Gow")             # Bye Gow

#t.greet("gow")          # also works: static methods can be called on an object
