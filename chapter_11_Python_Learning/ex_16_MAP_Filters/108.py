# 108.py
# Topic: filter() to remove empty values
#
# filter keeps items where the function returns a TRUTHY value.
# Returning None (or 0, "", [], etc.) -> item is DROPPED.
# So non_empty() keeps only the non-empty strings.

names = ["QA", "", "Automation", "", "Tester"]

def non_empty(x):
    if x != "":
        return True
    return None

non_empty = list(filter(non_empty, names))  # removes empty strings
print(non_empty)   # ['QA', 'Automation', 'Tester']