# This program shows a for loop running a "test case" 5 times.
# range(1, 6) gives the numbers 1, 2, 3, 4, 5 (6 is NOT included).
# for i in range(3, 5):
#     print(i)

# for i in range(1, 10,-1):
#     print(i)


# for i in range(10): # 0 to 9, 10 Times
#     print("Hello World!")

# Loop 5 times: test_id takes the values 1, 2, 3, 4, 5.
for test_id in range(1,6):
    # Print a message with the current test number.
    print("Running the test case : ",test_id)