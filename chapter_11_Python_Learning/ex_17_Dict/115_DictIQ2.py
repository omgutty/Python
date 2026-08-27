# 115_DictIQ2.py
# Topic: List of dicts with nested address - access deeper levels
#
# Same pattern as 114: a LIST of dicts, each with a NESTED dict.
# To reach "office_address" of the 3rd student you chain the keys:
#   student_list[2]["address"]["office_address"]
# Index 2 = the THIRD element (Python lists start at 0).

student_infor1 = {
    "name": "Pramod",
    # "age": 65,
    "age": 67,
    "address": {
        "home_address": "ND",
        "office_address": "KA"
    }
}

student_infor2 = {
    "name": "Amit",
    # "age": 65,
    "age": 69,
    "address": {
        "home_address": "GOA",
        "office_address": "KA"
    }
}

student_infor3 = {
    "name": "Murthy",
    # "age": 65,
    "age": 120,
    "address": {
        "home_address": "PODI",
        "office_address": "vizag"
    }
}

student_list = [student_infor1,student_infor2,student_infor3]
print(student_list)
print(student_list[2]["address"]["office_address"])   # vizag