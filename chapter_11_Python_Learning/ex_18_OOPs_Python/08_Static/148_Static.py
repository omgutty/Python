# 148_Static.py
# Topic: Class attribute shared across ALL objects
#
# count is a CLASS attribute - it belongs to the blueprint, not to
# one object. Every time __init__ runs (each new object), we do
# TestCounter.count += 1 -> the SAME shared counter goes up.
# This is how you count how many objects were created.

class TestCounter:
    count = 0          # class attribute (shared)

    def __init__(self):
        TestCounter.count +=1   # increment the shared counter

t1 = TestCounter()     # count -> 1
t2 = TestCounter()     # count -> 2
print(TestCounter.count)   # 2

# Each time an object is created, count increases.
# count is shared across all objects.