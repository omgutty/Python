# 168.py
# Topic: except with the error object (as fnf)
#
# "except FileNotFoundError as fnf" captures the ERROR OBJECT so we
# can print its message. If test.json does not exist, open() raises
# FileNotFoundError -> caught -> prints the message instead of crashing.

try:
    data = open("test.json").read()
except FileNotFoundError as fnf:
    print(fnf)   # [Errno 2] No such file or directory: 'test.json'