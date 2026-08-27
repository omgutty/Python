# 172_Builtin_Functions.py
# Topic: Python's BUILT-IN functions - reference
#
# Built-ins are always available - NO import needed, they work in every file.
# This file is a study reference only; nothing here runs.

# ---------- Convert one type to another ----------
# int(x)      -> convert to integer:  int("42") -> 42
# float(x)    -> convert to float:    float("3.5") -> 3.5
# str(x)      -> convert to string:   str(100) -> "100"
# bool(x)     -> convert to True/False: bool(0) -> False, bool(5) -> True
# list(x)     -> make a list:  list("abc") -> ['a','b','c']
# tuple(x)    -> make a tuple: tuple([1,2]) -> (1,2)
# set(x)      -> make a set (unique values): set([1,1,2]) -> {1,2}
# dict(x)     -> make a dict: dict([("a",1)]) -> {'a':1}
# frozenset(x)-> like set but immutable
# bytes(x)    -> make bytes from string/int
# bytearray(x)-> mutable version of bytes
# complex(x)  -> make complex number: complex(1,2) -> (1+2j)
# chr(n)      -> number to character: chr(65) -> 'A'
# ord(c)      -> character to number: ord('A') -> 65
# bin(n)      -> integer to binary string: bin(5) -> '0b101'
# hex(n)      -> integer to hex string:  hex(255) -> '0xff'
# oct(n)      -> integer to octal string: oct(8) -> '0o10'
# repr(x)     -> "developer" string of x (with quotes for strings)
# ascii(x)    -> like repr but escapes non-ASCII

# ---------- Numbers & Math ----------
# abs(x)      -> absolute value: abs(-7) -> 7
# round(x, n) -> round to n decimals: round(3.14159, 2) -> 3.14
# pow(a, b)   -> a raised to b: pow(2, 3) -> 8 (same as 2**3)
# divmod(a,b) -> (quotient, remainder): divmod(13,4) -> (3,1)
# sum(iter)   -> total of a list: sum([1,2,3]) -> 6
# min(iter)   -> smallest: min(3,1,2) -> 1
# max(iter)   -> largest:  max(3,1,2) -> 3
# hash(x)     -> numeric hash of an object (used in dict/set)

# ---------- Iteration & Sequences ----------
# range(n)    -> 0..n-1: list(range(3)) -> [0,1,2]
# len(x)      -> length: len("hello") -> 5
# enumerate(x)-> index+value pairs: list(enumerate("ab")) -> [(0,'a'),(1,'b')]
# zip(a, b)   -> pair up iterables: list(zip([1,2],["a","b"])) -> [(1,'a'),(2,'b')]
# map(f, it)  -> apply f to each item: list(map(str, [1,2])) -> ['1','2']
# filter(f,it)-> keep items where f is True: list(filter(None,[0,1,2])) -> [1,2]
# sorted(x)   -> new sorted list: sorted([3,1,2]) -> [1,2,3]
# reversed(x) -> reverse iterator: list(reversed([1,2,3])) -> [3,2,1]
# iter(x)     -> get an iterator from an iterable
# next(it)    -> pull next item from iterator: next(iter([5,6])) -> 5
# slice(a,b)  -> make a slice object: "hello"[slice(1,3)] -> "el"
# all(iter)   -> True if ALL items truthy: all([1,1,0]) -> False
# any(iter)   -> True if ANY item truthy:  any([0,0,1]) -> True

# ---------- Input / Output ----------
# print(...)  -> write to console (sep, end, file, flush options)
# input(...)  -> read a line from the user as a string
# open(file)  -> open a file for reading/writing
# format(x)   -> format a value: format(0.5, ".0%") -> '50%'
# help(x)     -> show documentation of an object
# breakpoint()-> drop into the debugger (pdb) at that line
# exec(str)   -> run a string as Python code
# eval(str)   -> evaluate a string as an expression: eval("2+3") -> 5

# ---------- Objects / Classes / OOP ----------
# type(x)     -> type of x: type(5) -> <class 'int'>
# id(x)       -> unique identity number of an object
# object()    -> base of all classes
# isinstance(x, type)  -> x is an instance? isinstance(5, int) -> True
# issubclass(A, B)     -> A is subclass of B? True/False
# dir(x)      -> list attributes/methods of x: dir("abc")
# vars(x)     -> dict of an object's __dict__ attributes
# getattr(obj, "name")    -> read attribute by name (string)
# setattr(obj, "name", v) -> set attribute by name (string)
# hasattr(obj, "name")    -> does attribute exist? True/False
# delattr(obj, "name")    -> delete an attribute by name
# callable(x) -> can x be called? callable(print) -> True
# super()     -> get parent class reference inside a subclass
# property()  -> make a getter/setter/deleter for an attribute
# staticmethod() -> mark a method as static (no self)
# classmethod()  -> mark a method as class-level (cls instead of self)
# globals()   -> dict of global variables in current scope
# locals()    -> dict of local variables in current scope

# ---------- Memory / Advanced ----------
# memoryview(x) -> memory view of bytes/bytearray (no copy)
# aiter()     -> async version of iter()
# anext()     -> async version of next()
# __import__("os") -> import a module by its name as a string

# NOTE: This is the complete list of Python 3.12 built-in FUNCTIONS.
# There are also built-in EXCEPTIONS (ValueError, KeyError...)
# and built-in CONSTANTS (True, False, None, __name__).
# Don't memorize - keep this file as a lookup reference.
