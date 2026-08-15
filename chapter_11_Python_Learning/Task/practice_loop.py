#loop 
# range - range( start, stop-1, step)
# range always start from 0 
# default step is 1 

# for i in range (1,10):
#     print (i) 

# print only even numbers in this range  1-100
# range(0, 101, 2): start at 0, stop BEFORE 101, take steps of 2
# so i becomes 0, 2, 4, 6 ... 100 (all even numbers).
for i in range(0, 101, 2):
    print (i)

for i in range(2, 101, 2):  # same idea, but starting from 2
    print(i)

for i in range(1, 101):     # go through 1 to 100
    if i % 2 == 0:          # % 2 gives the remainder -> 0 means even
        print(i)   


#while loop I  C  U 
# while loop: I = Initialise, C = Condition, U = Update (change the value)

#what is the diff between for loop and while loop 
#only diff is while loop intilization is out side that it 

test_id=0                    # I: start value (outside the loop)
while test_id<5:             # C: keep looping while this is True
    print("running your test ", test_id)
    test_id +=1              # U: increase by 1, or the loop never ends