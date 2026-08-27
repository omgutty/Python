# 177.py
# Topic: with open() - safe file reading
#
# "with open(...) as file" auto-closes the file when the block ends
# (even on errors) - no manual close() needed. try/except catches a
# missing file instead of crashing. file.read() reads everything;
# file.readlines() would give a list of lines.

# with  open('testdata.txt', 'r') as file
# file = open('testdata.txt', 'r')

try:
    with open('testdata.txt', 'r') as file:
        content = file.read()
    # content = file.readlines() # list manner
        print(content)
except FileNotFoundError as fnfe:
    print(fnfe)