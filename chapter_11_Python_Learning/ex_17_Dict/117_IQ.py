# 117_IQ.py
# Topic: Frequency of characters in a string (classic interview Q)
#
# Walk the string, count how many times each character appears.
# The dict maps: character -> count.
# char_count.get(char, 0): if char is already a key, get its count;
# if NOT, get 0 (no KeyError). Add 1 and store it back.
#
# For "automation":
#   a:2, u:1, t:2, o:2, m:1, i:1, n:1

string = "automation"
# {a : 2, u:1, t:2, o:2, m:1, i=1,n:1}

char_count = {}
for char in string:
    char_count[char] = char_count.get(char,0)+1

print(char_count)


