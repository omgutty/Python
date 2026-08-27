# 113_Dict2.py
# Topic: Dict gotcha - duplicate keys
#
# A dict key can appear only ONCE. If you write the same key twice,
# the LAST value WINS (the earlier one is silently overwritten).
# Here "age" is written twice -> 65 is replaced by 67.

student_infor = {
    "name": "Pramod",
     "age": 65,
    "age": 67,          # same key again -> overwrites 65
    "address": "KA"
}
print(student_infor)                # age is 67, NOT 65
print(student_infor["name"])        # Pramod
print(student_infor["age"])         # 67

print(student_infor["address"])     # KA
student_infor["age"] = 100          # normal overwrite via assignment
print(student_infor)