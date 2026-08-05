#loop 
# range - range( start, stop-1, step)
# range always start from 0 
# default step is 1 

# for i in range (1,10):
#     print (i) 

# print only even numbers in this range  1-100
for i in range(0, 101, 2):
    print (i)

for i in range(2, 101, 2):
    print(i)

for i in range(1, 101):
    if i % 2 == 0:
        print(i)   


#while loop I  C  U 

#what is the diff between for loop and while loop 
#only diff is while loop intilization is out side that it 

test_id=0
while test_id<5:
    print("running your test ", test_id)
    test_id +=1