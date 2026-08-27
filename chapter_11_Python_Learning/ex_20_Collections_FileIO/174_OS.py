# 174_OS.py
# Topic: os.getcwd + os.path.join + reading a file
#
# os.getcwd() -> current working directory (where the script runs).
# os.path.join(...) -> builds a path SAFELY for any OS (\\ on Windows,
# / on Linux). open(path, 'r').read() loads the whole file as text.
# NOTE: this expects to run from the repo ROOT (the path is absolute
# from the cwd) - run it with the venv python from the Python folder.

import os
print(os.getcwd())
full_path = os.path.join(os.getcwd(), "chapter_11_Python_Learning/ex_20_Collections/pramod.txt")
print(full_path)

file = open(full_path, 'r')
print(file.read())