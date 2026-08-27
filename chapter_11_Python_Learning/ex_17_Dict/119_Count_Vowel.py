# 119_Count_Vowel.py
# Topic: Count vowels in a string
#
# Loop over every character. If the character is one of "aeiou",
# increment the counter and remember it in a list.
# "in" on a string checks membership: is char one of these letters?

input_string = "hello, world!"
vowels = "aeiou"
vowels_count = 0
result = list()

for char in input_string:
    if char in vowels:
        vowels_count = vowels_count+1
        result.append(char)

print(vowels_count)   # 3  (e, o, o)
print(result)         # ['e', 'o', 'o']