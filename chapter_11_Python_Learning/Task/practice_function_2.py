# ============================================================
# WHY THE ORIGINAL ERROR HAPPENED (UnboundLocalError)
# ------------------------------------------------------------
# Python decides a name's scope by scanning the WHOLE function
# body, not line by line. If a name is ASSIGNED anywhere inside
# a function — even on the last line — it becomes LOCAL to that
# function. So `print(public_person)` at the top of the function
# was trying to read a LOCAL variable that had no value yet.
#
# Read-only access falls back to the global; assignment requires
# `global` (Option 1) or passing/returning values (Option 2).
#
# NOTE: Python has no real public/private — `relative_person` is
# just LOCAL to family(). stranger() can't see it because it
# doesn't exist outside the function.
# ============================================================


public_person = "PP"    # module-level (global) variable


# ============================================================
# OPTION 1 — `global` keyword  (works, but use sparingly)
# `global public_person` tells Python: "for the whole function,
# this name refers to the module-level variable." Reads AND
# writes both hit the global.
# ============================================================
def family():
    global public_person            # declare once at the top
    relative_person = "RP"
    print(public_person)            # reads global -> "PP"
    print(relative_person)
    public_person = "PPP"           # overwrites the global
    print(public_person)            # "PPP"


def stranger():
    print(public_person)            # only READS -> gets the global
    # print(relative_person)        # NameError: local to family() only


print("--- OPTION 1: global keyword ---")
family()
stranger()                          # global is now "PPP"
print("Global after option 1:", public_person)      # "PPP"

public_person = "PP"                # reset for the next option
print()


# ============================================================
# OPTION 2 — parameter + return  (idiomatic, recommended)
# Pass the value IN as a parameter and hand the new value BACK
# via return. The function never touches the global directly.
# ============================================================
def family_clean(person):
    relative_person = "RP"
    print(person)                   # receives "PP"
    print(relative_person)
    person = "PPP"                  # changes the local copy
    print(person)                   # "PPP"
    return person                   # send the new value out


print("--- OPTION 2: parameter + return ---")
public_person = family_clean(public_person)   # caller decides
print("Global after option 2:", public_person)  # "PPP"

public_person = "PP"                # reset for the next option
print()


# ============================================================
# OPTION 3 — keep it local
# If the function should NOT touch the global, just READ it and
# use a different local name for anything you want to change.
# ============================================================
def family_local():
    print(public_person)            # reads the global "PP" — fine
    local_person = "RP"
    print(local_person)
    local_person = "PPP"            # changes ONLY the local
    print(local_person)             # "PPP"


print("--- OPTION 3: keep it local ---")
family_local()
print("Global after option 3:", public_person)    # still "PP"
