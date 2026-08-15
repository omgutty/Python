# This program practises VARIABLES: storing values, overwriting them,
# complex numbers, and multiple assignment.

print(); # is a function 
# something which can e repitative 

print (2+2+2.2);   # 2.2 is a float (decimal number) -> answer has decimals
print (2,3,5,"om", True)

pi=3.14   # a variable stores a value; here a float (decimal)

name= "Om"
name= "Kittue"   # same variable name -> the old value is overwritten

print(name);
# it will be override. kittue 



# complex 
complex_number= 2+3
print(complex_number)
print(complex_number.real)   # .real gives the real part of a complex number
print(complex_number.imag)   # .imag gives the imaginary part
print(type (complex_number))


# multiple vairable allowed
# Assign several variables on one line: a=3, b=4, _=5.
a,b,_=3,4,5
print(a+b+_)

# max() returns the biggest value from the arguments given.
result= max(3,4);
print(result)



