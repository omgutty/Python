
# This program practises Python KEYWORDS (reserved words) and the
# print() function options (sep, end, file, flush).

import keyword

# mport tell python to load module 
# key word is build in python module 

# keyword.kwlist is the list of ALL reserved words in Python.
print(keyword.kwlist)

## these are reserver keywords
##['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# print(*values: object,
#     sep: str | None = " ",
#     end: str | None = "\n",
#     file: SupportsWrite[str] | None = None,
#     flush: Literal[False] = False)


print ("om ", sep='*', end='_', file="adf", flush=True);

# ============================================================
# print() full signature:
#   print(*values, sep=" ", end="\n", file=sys.stdout, flush=False)
# ============================================================

# --- 1. values: everything you want to print (can be many) ---
print("hello", "world")          # -> hello world
print(1, 2, 3)                   # -> 1 2 3

# --- 2. sep: separator placed BETWEEN values (default is a space) ---
print("a", "b", "c", sep="-")    # -> a-b-c
print("om", "sam", sep="*")      # -> om*sam

# --- 3. end: what comes AFTER everything (default is a newline) ---
print("loading", end="...")      # no newline, just "..."
print("done")                    # -> loading...done  (same line)

# --- 4. file: where output goes (default is the terminal) ---
# NOTE: file must be a FILE OBJECT, NOT a string like "adf" (that was a bug!)
with open("output.txt", "w") as f:   # "w" = write mode, creates output.txt
    print("om", file=f)              # writes INTO output.txt instead of terminal
# "with" automatically closes the file when the block ends

# --- 5. flush: force output out immediately (default False) ---
# Without flush, Python buffers output and writes it in batches.
# flush=True pushes it out right away - useful for progress bars / live logs.
import time
print("step 1...", flush=True)   # appears instantly
time.sleep(2)
print("step 2...", flush=True)

# --- All five together, the correct version of your line 19 ---
with open("output.txt", "w") as f:
    print("om", "sam", sep="*", end="_", file=f, flush=True)
    # values = "om", "sam"   ->  sep="*"  ->  om*sam
    # end="_"                ->  no newline, ends with _
    # file=f                 ->  written to output.txt
    # flush=True             ->  written immediately


# _ underscore is consider as variable

_=12
#identifieer/variable name 
#= operator 
#12 is literabl varibale value 
print(_) # 12

## Identifier roles 

#multi comment 

"""
hi 
hello 
namasty 

"""



# how to take input 

name= input("enter your name :")
print("hello ", name);

