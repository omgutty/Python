# my_list = [1, 2, 3]

# my_list[0] = "Pramod"
# my_list[1] = "Dutta"
# my_list[1] = "Dutta"

# print(my_list)
# # It will overwrite because a list is mutable. 

# for element in my_list:
#     print(element)

# # range() this also return the list
# for i in range(1, 5):  # 1,2,3,4
#     print(i)


my_list = [1, 2, 3]
# Indexing: each item has a position number (index), starting from 0.
print("element at the index 0 - ", my_list[0])
print("element at the index 1 - ", my_list[1])
print("element at the index 2 - ", my_list[2])

# append() - # Append object to the end of the list.
# append() adds ONE new item to the END of the list.
my_list.append(4)
print(my_list)

my_list.append(5)
print(my_list)

# extend() - Append a new list
# extend() adds ALL the items of another list to the end.
my_list.extend([7, 8, 10, 9])
print(my_list)

# insert()
# insert() puts a new item at a chosen position (index 1 here).
my_list.insert(1,"Dutta")
print(my_list)
print(len(my_list))  # len() counts the items again (now 9)

my_list.insert(0, 0)  # put 0 right at the front (index 0)
print(my_list)

my_list[1] = "Amit"  # change the item at index 1 -> lists are mutable
print(my_list)

my_list.remove("Amit")  # remove() deletes the first matching item
print(my_list)

# copy() makes a separate copy of the list.
my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

my_copy_list.remove("Dutta")  # removing from the copy

print(my_list)       # original list is unchanged
print(my_copy_list)  # only the copy lost "Dutta"