# This program prints all EVEN numbers from 0 to 100.
# It uses the % (modulo) operator to check if a number is even.

# range(101) gives the numbers 0, 1, 2, ..., 100.
for i in range(101):  # 0 to 100
    # % gives the remainder: if i % 2 == 0, i divides evenly by 2 (even).
    if i % 2 == 0:
        print(i)
