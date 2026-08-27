# 114_Dict_IQ.py
# Topic: Nested dicts inside a list
#
# A dict can hold another dict as a VALUE (nested).
# A list can hold dicts. Combine them: a list of dicts, where each
# dict contains a nested "address" dict.
# Access path: list[index]["key"]["nested_key"]

student_infor1 = {
    "name": "Pramod",
    "age": 67,
    "address": {
        "home_address": "ND",
        "office_address": "KA"
    }
}
student_infor2 = {
    "name": "Amit",
    "age": 69,
    "address": {
        "home_address": "GOA",
        "office_address": "KA"
    }
}

student_list = [student_infor1,student_infor2]
print(student_list)
print(student_list[0])                                  # whole first dict
print(student_list[0]["name"])                          # Pramod
print(student_list[0]["address"]["office_address"])     # KA