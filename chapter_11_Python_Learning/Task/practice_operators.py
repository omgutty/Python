# This program practises OPERATORS: logical, power, division and more.

a, b= 10, 20
print(a>0 and b<0)   # and: True only if BOTH sides are True -> False
print(a>0 or b<0)    # or: True if AT LEAST one side is True -> True
print (not (a>0))    # not: flips True to False -> False

#power
print (2*2)   # * is multiplication -> 4
print (2**3)  # ** is "to the power of" -> 2*2*2 = 8

# quadrent 
print (6//2) #3   # // is floor division -> whole number, no decimals

#div
print (6/2) # 3.0 ? (always gives you float )   # / always gives a float

# terminaory operator (brother of  if else )
# Ternary operator: a one-line if/else - "value if True else value if False"
x,y=10,20
print ("x is grater than y" if x>y else "x is less than y")

# membership operator 
# (the file ends here - "in" checks if something is inside a collection)
