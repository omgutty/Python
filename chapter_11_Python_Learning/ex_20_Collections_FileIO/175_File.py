# 175_File.py
# Topic: Reading a text file with os.path.join
#
# Build the file path with os.path.join (OS-safe) and read it with
# open(path, 'r').read(). The 'r' means read mode. Same pattern as
# 174 but pointing at testdata.txt.

import os

file_path = os.path.join(os.getcwd(),'chapter_11_Python_Learning/ex_20_Collections_FileIO/testdata.txt')
file_data = open(file_path,'r')
print(file_data.read())


