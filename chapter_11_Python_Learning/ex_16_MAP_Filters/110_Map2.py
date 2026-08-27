# 110_Map2.py
# Topic: map() with a named function - transform strings
#
# map() applies upper_case to every name -> all names become UPPERCASE.
# Same size in, same size out: 4 names in, 4 names out.

name = ["pramod", "dutta", "qa", "lucky"]


def upper_case(string):
    return string.upper()


upper_names = list(map(upper_case, name))
print(upper_names)   # ['PRAMOD', 'DUTTA', 'QA', 'LUCKY']