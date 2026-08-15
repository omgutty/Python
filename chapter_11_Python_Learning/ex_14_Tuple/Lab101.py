# This program shows more tuple features: checking, looping, and
# converting between lists and tuples.

# A tuple of city names - round brackets ( ) mean it cannot be changed.
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print(len(cities))  # len() counts the items -> 4
print("Paris" in cities)      # "in" checks if an item exists -> True
print("New Delhi" in cities)  # -> False, it is not in the tuple

t = (12, 34, 56)
# t.append(12)  # ERROR: tuples have NO append - they cannot be changed!

# tuple([...]) builds a tuple from a list.
ENV_API_URLS = tuple(["abc.com/get", "xyz.com/post", "qwe.com/put"])
print(ENV_API_URLS)

# A for loop goes through each item of the tuple one by one.
colors = ("red", "green", "blue")
for c in colors:
    print(c)


my_list = [1, 2, 3]
my_tuple = tuple(my_list)  # convert list -> tuple
print(my_tuple)    # (1, 2, 3)


back_to_list = list(my_tuple)  # convert tuple -> list
print(back_to_list)   # [1, 2, 3]
print(max(back_to_list))   # max() gives the biggest value -> 3
# type