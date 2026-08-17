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
######################################

sq= {x+2 for x in range(5)}
print(sq)


######################################
"""# Find the all non repeating character in a string 

Example: 
Input : swiss -> s - 3, w = 0, i = 0

Output : w i"""

 # ---- Approach 1 : Set based (fits this file's theme) ----
    # Idea: while walking the string, remember every character we have seen.
    # If we ever see a character a second time, mark it as "repeated".
    # At the end: non-repeating = seen - repeated (same set difference
    # as a - b earlier in this file, lines 41-44).

text = input("Enter word: ")

seen = set()        # every character we have come across
repeated = set()    # characters that appeared more than once

for ch in text:
    if ch in seen:      # already saw it before -> it repeats
        repeated.add(ch)
    seen.add(ch)        # always remember this character

non_repeating = seen - repeated   # seen minus repeated -> appears exactly once
print("Approach 1 (sets):", non_repeating)   # {'w', 'i'} (order not guaranteed)

