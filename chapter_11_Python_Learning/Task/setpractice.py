set_of_numbers= {1,2,3,4,5,2,5}
print(set_of_numbers)

# duplicate numbers are  filter out 

list1= [1,2,3,4,5,6,5,4,3,2,1]

set1= set(list1)
print(set1)


t=("the", "for", "good", "the")
print(t)

print(set(t))

mixed_set= {1,"Tan", True, 5.11}
print (mixed_set)

for item in mixed_set:
    print(item)

mixed_set.add(111)
mixed_set.remove(1)
print (mixed_set)


a= {1,2,3,4,5}
b= {1,1,3,6,7}

print(a|b) 
#{1, 2, 3, 4, 5, 6, 7}
print(a.union(b))
#{1, 2, 3, 4, 5, 6, 7}

print(a & b)
#{1, 3}
print(a.intersection(b))
#{1, 3}

print(a-b)
#{2, 4, 5}
print(a.difference(b))
#{2, 4, 5}

print(b-a)
#{6, 7}

print(b.difference(a))
#{6, 7}