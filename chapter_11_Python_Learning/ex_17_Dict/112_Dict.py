# 112_Dict.py
# Topic: Dictionaries - key-value pairs
#
# A dict stores KEY -> VALUE pairs. Keys are unique and must be
# immutable (strings, numbers, tuples). Values can be ANYTHING.
#   - read:   my_dict["key"]     (KeyError if missing)
#   - write:  my_dict["key"] = v (adds or overwrites)
#   - delete: del my_dict["key"]
#   - loop:   for key, value in my_dict.items()
#   - check:  "key" in my_dict   (True/False)

my_dict = {
    "name": "Aman",
    "age": 34,
    "role": "SDET",
    "exp": 3
}

print(my_dict)
print(my_dict["age"])        # 34
print(my_dict["role"])       # SDET

my_dict["role"] = "Manual Tester"   # overwrite existing value
print(my_dict)

del my_dict["age"]                   # remove a key
print(my_dict)

for key, value in my_dict.items():   # loop over all pairs
    print(key, value)

print("age" in my_dict)      # False (deleted)
print("role" in my_dict)     # True