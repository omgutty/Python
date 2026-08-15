# ============================================================
# DECORATORS — WHAT IS REALLY HAPPENING
# ============================================================
# The @ syntax is JUST shorthand for an assignment:
#
#   @deco1
#   def numbers(): ...
#
# is literally the same as:
#
#   def numbers(): ...
#   numbers = deco1(numbers)
#
# So a decorator is:  a function that TAKES a function
# and RETURNS a new function (the replacement).
#
# The full contract has 3 parts:
#   1. The original function is passed IN as a parameter (fun)
#   2. A replacement function (wrapper) is built around it
#   3. The replacement is RETURNED, so it takes over the name
#
# If you break part 3 (no return), the name becomes None
# and calling it crashes:  TypeError: 'NoneType' object is not callable.
# ============================================================


def deco1(fun):
    # fun = the ORIGINAL function that @deco1 decorates.
    # At decoration time Python does:  numbers = deco1(numbers)
    # so "fun" here IS the numbers function.

    def wrap():
        # wrap = the REPLACEMENT function.
        # After decoration, the name "numbers" no longer points to the
        # original function — it points to THIS function instead.
        # The original survives only inside the closure: wrap "remembers" fun.

        # This line runs BEFORE the original function body.
        print("one")

        # THIS is the crucial line: we must call fun() here.
        # The original function body only runs because we call it.
        # If we never called fun(), the original print("Above are numbers")
        # would be silently lost — wrap would run and fun would not.
        fun()

        # Anything after fun() would run AFTER the original (e.g. teardown).

    # Mandatory: return the replacement so the assignment
    #   numbers = deco1(numbers)
    # puts a WORKING function back into the name "numbers".
    # Without this, deco1 returns None and numbers becomes None.
    return wrap


def deco2(fun):
    # Same structure as deco1 — this is the standard decorator skeleton:
    #   outer function takes the original (fun)
    #   inner function (wrap) wraps it with extra behavior
    #   return the inner function

    def wrap():
        print("Two")  # behavior BEFORE the original
        fun()         # call the original function
        # return value of fun() is discarded here — the original
        # function's return value is NOT forwarded unless we
        # explicitly "return fun()".

    return wrap


@deco1
@deco2
# Chained decorators apply BOTTOM-UP:
#   numbers = deco1(deco2(numbers))
# deco2 wraps the original FIRST, then deco1 wraps deco2's result.
def nummbers():
    # This is the ORIGINAL function. After decoration, the name
    # "nummbers" points to deco1's wrap, and this original body
    # only runs because the wrappers eventually call fun() -> this.
    print("Above are numbers")


# Calling nummbers() actually calls deco1's wrap, which calls
# deco2's wrap, which calls the original. Flow:
#   1. deco1.wrap prints "one"
#   2. deco1.wrap calls fun()  -> which is deco2.wrap
#   3. deco2.wrap prints "Two"
#   4. deco2.wrap calls fun()  -> which is the original
#   5. original prints "Above are numbers"
#
# Output:  one / Two / Above are numbers
nummbers()
