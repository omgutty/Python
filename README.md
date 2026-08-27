# AI 3x Blueprint - Python

Hands-on Python practice that builds the fundamentals **step by step** — from `print()` to OOP, modules, file I/O, and pytest — with one goal in mind: **build AI agents with Python**.

Every chapter is a self-contained set of lab scripts, each demonstrating one concept. The path ends where the real work begins: a working **CrewAI agent** in `chapter_12_CrewAI`.

## Project Structure

```
Python/
├── chapter_11_Python_Learning/         # The full Python learning path (21 exercise chapters)
│   ├── ex_01_Python_Basics/            # print(), comments
│   ├── ex_02_Keywords_Identifier_Variables/  # keywords, identifiers, variables, math
│   ├── ex_03_Literals/                 # literals, data types, input, strings
│   ├── ex_04_Operators/                # arithmetic, comparison, logical, ternary, membership
│   ├── ex_05_Condition_Loops/          # if / elif / else
│   ├── ex_06_Switch_Match/             # match-case (Python switch)
│   ├── ex_07_Loops/                    # for / while, break, pass
│   ├── ex_08_Functions/                # functions: params, returns, *args, defaults
│   ├── ex_09_Functions_Scopes/         # local/global scope, inner functions
│   ├── ex_10_Decortors/                # decorators
│   ├── ex_11_TypeConversion/           # int(), str(), float(), ...
│   ├── ex_12_Lambda_Exp/               # lambda expressions
│   ├── ex_13_LIST/                     # lists + methods (pop, ...)
│   ├── ex_14_Tuple/                    # tuples
│   ├── ex_15_SET_MAP_DICT/             # sets, set operations, frozenset
│   ├── ex_16_MAP_Filters/              # map() and filter()
│   ├── ex_17_Dict/                     # dictionaries, nesting, dict IQs
│   ├── ex_18_OOPs_Python/              # OOP: class → constructor → inheritance → abstraction
│   ├── ex_19_Package/                  # modules & packages, __init__.py, imports
│   ├── ex_20_Collections_FileIO/       # collections, os, file I/O, csv, env vars
│   ├── ex_21_PyTest/                   # pytest basics, markers, assert
│   ├── Task/                           # daily practice & challenge programs
│   └── autoweave/                      # Playwright browser-automation tests
├── chapter_12_CrewAI/                  # First AI agent: CrewAI test-analyst agent
└── linkedin_post.md                    # Learning-in-public posts
```

## Chapter-by-Chapter Overview

### ex_01 - ex_14: The Fundamentals
The foundation chapters cover printing, keywords, variables, literals, operators, conditions, `match`, loops, functions, scope, decorators, type conversion, lambdas, lists, and tuples. Each `LabXXX_Topic.py` is a small, runnable script for one concept. See the per-chapter README in [chapter_11_Python_Learning/README.md](chapter_11_Python_Learning/README.md) for the full lab tables.

### ex_15_SET_MAP_DICT — Sets
| Lab | Topic |
|-----|-------|
| `102.py` | Sets - the basics (unique items, dedupe) |
| `103_SET.py` | Sets - full tour (add/remove, union, intersection, difference) |
| `104_Set_Advance.py` | set() from a list, len(), iteration, add() |
| `105_Extra.py` | Set comprehensions + frozenset |

### ex_16_MAP_Filters — map() & filter()
| Lab | Topic |
|-----|-------|
| `106.py` | `filter()` - keep even numbers |
| `107_Lab.py` | `filter()` + lambda - keep only "PASS" results |
| `108.py` | `filter()` - remove empty strings |
| `109_Map.py` | `map()` - square every number |
| `110_Map2.py` | `map()` - uppercase strings |
| `111_Map_IQ.py` | `map()` + lambda - convert ms to seconds |

### ex_17_Dict — Dictionaries
| Lab | Topic |
|-----|-------|
| `112_Dict.py` | Dict basics: read/write/delete/loop/`in` |
| `113_Dict2.py` | Duplicate-key gotcha (last value wins) |
| `114_Dict_IQ.py` | Nested dicts inside a list |
| `115_DictIQ2.py` | List of dicts, deeper nested access |
| `116_Dict_Imp.py` | `dict(zip())` + merging dicts |
| `117_IQ.py` | Character frequency counter (interview Q) |
| `118_IQ.py` | Dict equality (order-independent) |
| `119_Count_Vowel.py` | Count vowels in a string |

### ex_18_OOPs_Python — Object-Oriented Programming
The OOP chapter is split into 10 sub-topics, in learning order:

| Sub-folder | Topic | Labs |
|------------|-------|------|
| `01_Class_Object` | Class blueprint, attributes, methods, objects | 120, 122 |
| `02_Constructor` | `__init__`, parameterized constructor, user-input constructor | 123–128 |
| `03_Instance_Variable` | Global vs class vs local scope | 129 |
| `04_Encapsulation` | public/protected/private, name mangling, dotenv credentials | 130–136 |
| `05_Inheritance` | Single, multiple, multilevel, hierarchical, hybrid, MRO | 130–136 |
| `06_Polymorphism` | Method overloading (defaults), method overriding | 137–142 |
| `07_Abstraction` | `abc.ABC`, `@abstractmethod`, abstract chains | 143–147 |
| `08_Static` | Class attributes, `@staticmethod`, `@classmethod` | 148–154 |
| `09_Exceptions` | Error types, try/except/else/finally, raise, custom exceptions | 153–169 |
| `10_Modules` | Modules reference, built-in functions reference, image prompt | 170–173 |

**Key concepts you will master here:**
- **Constructor** — `__init__` runs automatically on object creation; `self` is the instance, passed automatically.
- **Encapsulation** — `_name` (protected) vs `__name` (private, name-mangled to `_Class__name`); hiding data and giving controlled access via methods.
- **Inheritance** — a child reuses a parent's methods/attributes; MRO resolves which method wins with multiple parents.
- **Polymorphism** — overloading is simulated with default parameters (last definition wins); overriding lets children replace parent methods.
- **Abstraction** — abstract classes define *rules* (`@abstractmethod`) that children must implement; abstract classes cannot be instantiated.
- **Static & class methods** — `@staticmethod` needs no `self` (call on class name); `@classmethod` receives `cls`.
- **Exceptions** — `try`/`except`/`else`/`finally`, raising errors, custom exception classes.

### ex_19_Package — Modules & Packages
| File | Topic |
|------|-------|
| `170.py` | Import from a package (`from package import ...`) + a single module |
| `package/` | Folder marked by `__init__.py` (the package) |
| `package/util_module.py` | Module 1 inside the package |
| `package/util_module2.py` | Module 2 inside the package (same function name, separate file) |
| `mymodule.py` | A standalone single module (`import mymodule`) |

### ex_20_Collections_FileIO — Collections, OS & Files
| File | Topic |
|------|-------|
| `171.py` | `collections`: Counter, defaultdict |
| `172_Main.py` | `if __name__ == '__main__'` entry-point pattern |
| `173_Usage.py` | `__name__` guard with multiple functions |
| `174_OS.py` | `os.getcwd()`, `os.path.join()`, reading a file |
| `175_File.py` | Reading a text file |
| `176_Env.py` | Environment variables with python-dotenv |
| `177.py` | `with open()` - safe file reading + FileNotFoundError |
| `178.py` | Reading CSV with the `csv` module |
| `179.py` | Reading CSV with pandas |

### ex_21_PyTest — Testing
| File | Topic |
|------|-------|
| `179.py` | Testing intro: Expected Result == Actual Result |
| `test_180.py` | pytest markers (`@pytest.mark.smoke` / `reg`) |
| `test_181.py` | Passing vs intentionally failing assertions |
| `PyTest_Cheatsheet.md` | pytest quick reference |

### Task — Daily Practice
Daily practice files that lock in each concept: calculators, grade/quotient-remainder challenges, `print()` signature practice, conditions, loops, functions, lambda, decorators, sets, dict frequency, OOP practice (class, constructor, encapsulation, inheritance, polymorphism, abstraction, static, exceptions, modules).

### autoweave — Playwright Browser Automation
End-to-end UI tests (login flow) with Playwright + pytest. See [autoweave/README.md](chapter_11_Python_Learning/autoweave/README.md) for setup and run instructions.

## chapter_12_CrewAI — First AI Agent

| File | Topic |
|------|-------|
| `01_test_analyst_Agent.py` | A CrewAI agent that acts as a senior QA analyst - given a feature, it produces 5-10 test cases |

**The CrewAI flow this script demonstrates:**
1. **Set up the brain** - the LLM (Groq `gpt-oss-120b` via an OpenAI-compatible endpoint, credentials from `.env`)
2. **Define the agent** - role, goal, backstory
3. **Give the task** - description + expected output
4. **Build the crew** - agents + tasks together
5. **Kick off** - `crew.kickoff()` runs the agent

This is the payoff of the whole Python path: classes, functions, `os`/`dotenv` environment handling, and modular code are exactly what agent development uses.

## Getting Started

### Prerequisites

- Python 3.x (this repo uses a venv at `chapter_11_Python_Learning/.venv`)
- `python-dotenv` (already installed in the venv) for the env-variable labs
- `pandas` / `requests` for specific labs (ex_20, ex_18 exceptions)
- `crewai` + `python-dotenv` + a Groq API key for `chapter_12_CrewAI`
- `uv`, `pytest`, `playwright` + Chromium for the `autoweave` tests

### Running the exercises

Use the project venv's Python (the `python` on PATH is the Windows Store stub):

```powershell
# from the repo root
& .\chapter_11_Python_Learning\.venv\Scripts\python.exe chapter_11_Python_Learning\ex_18_OOPs_Python\01_Class_Object\120_Class.py
& .\chapter_11_Python_Learning\.venv\Scripts\python.exe chapter_11_Python_Learning\ex_16_MAP_Filters\109_Map.py
```

Or with the venv activated:

```powershell
.\chapter_11_Python_Learning\.venv\Scripts\Activate.ps1
python chapter_11_Python_Learning\ex_18_OOPs_Python\09_Exceptions\160.py
```

Some labs prompt for input (`input()`) - type your values and press Enter. A few dotenv labs read a `.env` file next to the script (`VWO_USERNAME` / `VWO_PASSWORD` style credentials).

### Running the tests

```powershell
& .\chapter_11_Python_Learning\.venv\Scripts\python.exe -m pytest chapter_11_Python_Learning\ex_21_PyTest
```

## Learning Path

1. **ex_01-ex_03** - printing, keywords, variables, literals, data types, user input.
2. **ex_04-ex_07** - operators, conditions, `match`, loops.
3. **ex_08-ex_12** - functions, scope, decorators, type conversion, lambdas.
4. **ex_13-ex_17** - lists, tuples, sets, map/filter, dicts.
5. **ex_18** - full OOP: classes → constructors → encapsulation → inheritance → polymorphism → abstraction → static → exceptions.
6. **ex_19-ex_21** - modules/packages, file I/O & collections, pytest.
7. **chapter_12_CrewAI** - build your first AI agent with CrewAI.

Every step builds toward the same goal: **AI agents**. Classes are how agents hold state, functions are the tools they call, environment variables are how they get API keys, and tests verify their output.

## License

All content is for personal learning purposes.
