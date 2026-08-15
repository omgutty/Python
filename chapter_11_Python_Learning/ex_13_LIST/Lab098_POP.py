# squares = [1, 4, 9, 16, 25]
# print(squares)
# print(squares.pop()) # Remove and return item at index (default last)
# print(squares)
# print(squares.pop(1))
# print(squares)

# squares.clear()
# print(squares)

# # index(element, start, end)
# # Returns the index of the first occurrence of the element.
# This program shows more list tricks: range(), nested lists, and del.
# The commented lines at the top show other list methods (pop, clear, sort...).

numbers = [10, 20, 30, 20, 40]
# print(numbers.index(20))
# print(numbers.count(20))

# numbers.sort()
# print(numbers)

# numbers.sort(reverse=True)
# print(numbers)

# # max() / min() / sum() Works for numerical lists.
# print(max(numbers))  # 40
# print(min(numbers))  # 10
# print(sum(numbers))  # 120

# Slicing (start, end-1) - index
# print(numbers)  # [10, 20, 20, 30, 40]
# print(numbers[1:4]) 


# print("apple" in numbers)
# print(20 in numbers)

# range(1, 5) makes the numbers 1, 2, 3, 4 (stops before 5).
# list(range(...)) turns those numbers into a list.
l = list(range(1, 5))
print(l)

# Nested Lists: a list inside a list, like a table with rows and columns.
# matrix[1] is the second row [4,5,6], and [2] picks the third item -> 6.
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix[1][2])

# del removes an item by its index (here the first item, 10).
del numbers[0]
print(numbers)