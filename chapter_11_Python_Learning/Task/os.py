import os
print(os.getcwd())
fullpath= os.path.join(os.getcwd(),"chapter_11_Python_Learning/Task/test.txt")

print(fullpath)

file= open(fullpath,'r')

print(file.read())