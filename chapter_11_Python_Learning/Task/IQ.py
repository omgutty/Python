# Frequency of Characters in a String
# Write a program to count the frequency
# of each character in a given string.

string = "omnamassivaya"

# Why a dict? We store pairs: character (key) -> its count (value).
# It starts EMPTY because nothing is counted yet.
char_count = {}

# for char in string: walks the string one character at a time.
# Each round, 'char' holds the current character.
for char in string:
    # char_count.get(char, 0):
    #   - character already a key? get() returns its current count
    #   - first time we see it? get() returns 0 (no KeyError crash)
    # + 1 -> add one for this occurrence
    # store the new count back into the dict
    char_count[char] = char_count.get(char, 0) + 1

# Final result: {'o': 1, 'm': 2, 'n': 1, 'a': 4, 's': 2, 'i': 1, 'v': 1, 'y': 1}
print(char_count)
