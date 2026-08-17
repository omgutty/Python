test = ["om", 'tan', "kit"]

om_give= list(filter(lambda x:x=="om", test))

print(om_give)

list_of_names= [1,2,3,4,5,6,7,8]

filteringnumber= list(filter(lambda x:x==1,list_of_names))
print(filteringnumber)

#########################################

list_of_names= [1,2,3,4,5,6,7,8]
def squreroot(x):
    return x**2

all_sq_numebers=list(map(squreroot,list_of_names))
print(all_sq_numebers)