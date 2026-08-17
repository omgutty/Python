# 134_Ecap_Example.py
# Topic: Real-world encapsulation - Bank account
#
# The account number is PRIVATE (__account_number).
# Outsiders CANNOT read it directly - only the class method can,
# and only if you pass is_auth=True (access control!).
# This is encapsulation: data hidden + controlled access via methods.

class Bank:

    def __init__(self, account_number, balance):
        self.balance = balance             # public  - anyone can read/change
        self.__account_number = account_number  # private - hidden

    def check_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount  # modify through a method

    def show_me_account_number(self, is_auth):
        # Controlled access: only authorized callers see the account number
        if is_auth == True:
            print(self.__account_number)
        else:
            print("Not Allowed!")


icici = Bank(9876543210, 100)
icici.deposit(100)       # balance: 100 -> 200
icici.check_balance()    # 200

# print(icici.__account_number)
# ❌ AttributeError: private! The outside world cannot see it directly.
# If you are a cashier you can still see the account number -
# because the class offers a METHOD with the access check.
icici.show_me_account_number(True)   # 9876543210
