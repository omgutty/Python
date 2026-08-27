# 171_Modules_Overview.py
# Topic: Python's Standard Library - a reference of built-in modules
#
# A MODULE is just a .py file with functions/classes you can import.
# A PACKAGE is a folder of modules (importable with dots, e.g. os.path).
# These below are ALL built into Python - no pip install needed.
# This file does not run anything; it is a study reference.

# ---------- Operating System & Files ----------
# os          -> OS interaction: os.name, os.getcwd(), os.listdir(), os.mkdir()
# sys         -> interpreter & command-line: sys.argv, sys.exit(), sys.version
# pathlib     -> modern, clean path handling: Path("a/b") / "c.txt"
# shutil      -> copy/move/delete files: shutil.copy(), shutil.rmtree()
# glob        -> find files by pattern: glob.glob("*.txt")
# subprocess  -> run other programs from Python
# tempfile    -> create temporary files/folders

# ---------- Data Types & Math ----------
# math        -> math.sqrt(), math.pi, math.floor()
# random      -> random.randint(), random.choice(), random.shuffle()
# statistics  -> mean, median, mode of a list of numbers
# decimal     -> exact decimal arithmetic (money, no float rounding)
# fractions   -> rational numbers (1/3 exactly)
# datetime    -> dates & time: datetime.now(), timedelta
# time        -> time.time(), time.sleep(), time.strftime()
# calendar    -> calendar functions (month, weekday, leap years)

# ---------- Text & Strings ----------
# string      -> constants like string.ascii_letters, string.digits
# re          -> regular expressions: re.search(), re.findall(), re.sub()
# textwrap    -> wrap/indent text
# difflib     -> compare sequences, find differences

# ---------- Collections & Utilities ----------
# collections -> special containers: Counter, defaultdict, deque, namedtuple
# itertools   -> looping tools: permutations, combinations, chain, count
# functools   -> higher-order functions: reduce, lru_cache, partial
# heapq       -> priority queues
# array       -> compact arrays (like list but memory-efficient)
# bisect      -> binary search on sorted lists

# ---------- JSON / Data Exchange ----------
# json        -> json.dumps(), json.loads() (read/write JSON)
# csv         -> read/write CSV files
# sqlite3     -> built-in database (SQLite)
# xml         -> parse XML documents
# pickle      -> save/load Python objects to a file
# configparser-> read .ini config files

# ---------- Web & Networking ----------
# urllib      -> fetch URLs: urllib.request.urlopen()
# http        -> HTTP server/client modules
# socket      -> low-level networking
# smtplib     -> send emails
# email       -> parse/build emails

# ---------- Running & Interacting ----------
# argparse    -> parse command-line arguments (flags like --name)
# logging     -> professional log messages instead of print()
# traceback   -> print/format exception tracebacks
# warnings    -> control warning messages
# pdb         -> built-in debugger

# ---------- OOP Support (what you are using now) ----------
# abc         -> ABC, abstractmethod (abstract base classes)
# enum        -> Enum (named constant groups)
# dataclasses -> @dataclass (auto-generate __init__ etc.)
# typing      -> type hints: List, Dict, Optional, Union
# inspect     -> examine live objects/classes/functions

# ---------- Misc / Fun ----------
# turtle      -> draw with a turtle (learning graphics)
# tkinter     -> build desktop GUI apps
# webbrowser  -> open a URL in the browser
# antigravity -> Easter egg: opens xkcd comic

# How to use any of them:
#   import os
#   os.getcwd()
#
#   from datetime import datetime
#   datetime.now()
