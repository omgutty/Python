# 169.py
# Topic: ExceptionGroup (Python 3.11+) - raise MULTIPLE errors at once
#
# ExceptionGroup bundles several different errors into one object.
# check_div raises the group when a == 0. (Catching groups needs
# except* - a separate topic; this file just SHOWS the group.)

eg = ExceptionGroup("Multiple Ex", [
    ValueError("Invalid Value"),
    TypeError("Type Error "),
    ZeroDivisionError("Can't div Xero")
])


def check_div(a):
    if a == 0:
        raise eg   # raises all three errors together