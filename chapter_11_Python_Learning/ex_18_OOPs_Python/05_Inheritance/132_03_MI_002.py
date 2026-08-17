# 132_03_MI_002.py
# Topic: Multiple Inheritance conflict + MRO
#
# BOTH parents define the SAME method name: money()
# Child inherits from both -> WHICH money() runs?
# Answer: MRO - Method Resolution Order. Python checks parents
# LEFT to RIGHT. Father1 comes first -> Father1.money() wins.

class Father1:
    def money(self):
        print("F1 Money")


class Father2:
    def money(self):
        print("F2 Money")


class Child(Father1, Father2):  # Father1 checked FIRST
    def give_money(self):
        print("Son")
        self.money()  # resolves via MRO -> Father1's version


c = Child()
c.give_money()  # prints "Son" then "F1 Money"

# You can check the resolution order yourself:
# print(Child.__mro__)
# -> (Child, Father1, Father2, object)
