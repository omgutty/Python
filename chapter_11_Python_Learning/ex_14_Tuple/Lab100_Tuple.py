# This program compares LISTS (changeable) with TUPLES (unchangeable).
# A tuple is written with round brackets ( ) and cannot be changed after creation.

# First, a normal list - lists ARE changeable (mutable).
shopping_list_wife = ["bread", "butter", "paneer"]
shopping_list_wife[2] = "milk"  # this works: we replaced "paneer" with "milk"
print(shopping_list_wife)

# Real of Tuples
# A tuple - try changing it and Python will raise an error.
my_tuple = ("tta.com", "sdet.live")
print(my_tuple)
# list(my_tuple) converts the tuple into a list (so we can change it later).
my_api_list = list(my_tuple)

# Real case, where we Tuples
# Tuples are perfect for data that must NOT change, like fixed API URLs.
API_URLSs = ("https://sdet.live/python0x", "https://awesomeqa.com", "https://thetestingacademy.com")
print(API_URLSs[0])  # index 0 = first URL
print(API_URLSs[1])  # index 1 = second URL

# tuple() with nothing inside creates an EMPTY tuple.
t = tuple()
print(t)

# list() with nothing inside creates an EMPTY list.
l = list()
print(l)

