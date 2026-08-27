# 104_Set_Advance.py
# Topic: Sets - advanced (dedupe, length, iteration, add)
#
# set(list) converts any list into a set -> duplicates disappear.
# len() works on sets too (count of unique items).
# A for loop iterates over a set (order is NOT guaranteed).
# add() inserts ONE item; adding an existing item changes nothing.

set1 = set(["TheTestingAcademy", "For", "TheTestingAcademy."])
print(set1)
print(len(set1))     # 3 -> note "TheTestingAcademy" and "TheTestingAcademy." differ

for i in set1:
    print(i)         # iteration order is arbitrary


set1.add("Pramod")
set1.add("Pramod")   # second add is a no-op (already present)
print(set1)