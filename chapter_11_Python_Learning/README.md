# Python Learning - Chapter 11

A hands-on collection of Python practice exercises covering the fundamentals — from basic `print` statements to operators, conditionals, loops, functions, decorators, data structures, **full OOP**, modules, file I/O, and pytest. Each exercise is a self-contained lab script that demonstrates a specific concept, plus daily challenge tasks and browser-automation tests.

The end goal: **build AI agents with Python**. These exercises lay the Python foundation that agent development builds on.

## Project Structure

```
chapter_11_Python_Learning/
├── ex_01_Python_Basics/                  # Printing, comments, and the basics
├── ex_02_Keywords_Identifier_Variables/  # Keywords, identifiers, variables, math
├── ex_03_Literals/                       # Literals, data types, user input, strings
├── ex_04_Operators/                      # Arithmetic, comparison, logical, ternary, membership
├── ex_05_Condition_Loops/                # if / elif / else conditions
├── ex_06_Switch_Match/                   # match-case (Python switch)
├── ex_07_Loops/                          # for / while loops, break, pass
├── ex_08_Functions/                      # Functions: parameters, returns, *args, defaults
├── ex_09_Functions_Scopes/               # Local variables, inner functions, scope
├── ex_10_Decortors/                      # Decorators
├── ex_11_TypeConversion/                 # Type conversion (int, str, float, ...)
├── ex_12_Lambda_Exp/                     # Lambda expressions
├── ex_13_LIST/                           # Lists and methods (pop, ...)
├── ex_14_Tuple/                          # Tuples
├── ex_15_SET_MAP_DICT/                   # Sets: dedupe, operations, frozenset
├── ex_16_MAP_Filters/                    # map() and filter()
├── ex_17_Dict/                           # Dictionaries: nesting, merging, IQs
├── ex_18_OOPs_Python/                    # OOP: classes, constructor, inheritance,
│                                         #   encapsulation, polymorphism, abstraction,
│                                         #   static methods, exceptions, modules
├── ex_19_Package/                        # Modules & packages, __init__.py
├── ex_20_Collections_FileIO/             # collections, os, file I/O, csv, env vars
├── ex_21_PyTest/                         # pytest: assert, markers, test files
├── Task/                                 # Daily challenge tasks & practice
└── autoweave/                            # Playwright browser-automation tests
```

## Exercises Overview

### ex_01_Python_Basics
| Lab | Topic |
|-----|-------|
| `Lab001_Hello.py` | First `print()` statements with multiple arguments |
| `Lab002_Comment.py` | Comments in Python |
| `Lab003_Print.py` | More `print()` usage |
| `Practice_1.py` | Practice file (empty, ready for exercises) |

### ex_02_Keywords_Identifier_Variables
| Lab | Topic |
|-----|-------|
| `Lab004_Keyword.py` | Python keywords |
| `Lab005_Variable_Part1.py` | Variables - part 1 |
| `Lab006_Identifier.py` | Identifiers |
| `Lab007_Variables_Names.py` | Naming variables |
| `Lab008_Dynamically_typed.py` | Dynamic typing |
| `Lab009_Identifier_Rule.py` | Identifier rules |
| `Lab010_maths.py` | Arithmetic operations |
| `Lab011_IQ_BODMAS.py` | Operator precedence (BODMAS) |
| `Lab012_Multiple_Variables.py` | Assigning multiple variables |
| `Lab013_Multiple_Prints.py` | Multiple print statements |
| `Lab014_Math_Functions.py` | Built-in math functions |
| `Lab015_IQ.py` | Mixed expression quiz |
| `rules_for_identifier.md` | Identifier rules reference |

### ex_03_Literals
| Lab | Topic |
|-----|-------|
| `Lab016_Literals.py` | Literals |
| `Lab017_Multi_Comment.py` | Multi-line comments |
| `Lab018_Multi_Comments.py` | Multi-line comments - continued |
| `Lab019_Data_Type.py` | Data types |
| `Lab020_BuiltIn_Functions.py` | Built-in functions |
| `Lab021_UserInput.py` | Taking user input |
| `Lab022_User_Input_Sum_Of_Two_numbers.py` | Sum of two numbers from input |
| `Lab023_Strings.py` | Strings and `input()` |
| `Lab024_Strings_conversion.py` | String type conversion |
| `Lab025_Strings2.py` | String concatenation |
| `Lab026_Literals.py` | Literals by base (binary, octal, hex) |
| `Lab027_Escape_Char.py` | Escape sequences |
| `Lab028_String_Double_Single_Diff.py` | Single vs double quotes, raw strings |
| `Lab029_Task1.py` | Task: 3-number calculator |
| `Lab030_Task2.py` | Task: quotient and remainder |

### ex_04_Operators
| Lab | Topic |
|-----|-------|
| `Lab031_Arth_Op.py` | Arithmetic operators |
| `Lab032_Comparision_Op.py` | Comparison operators |
| `Lab033_Logic_Operator.py` | Logical operators |
| `Lab034_Operators_P2.py` | Operators practice |
| `Lab035_Operators_P4.py` | Operators practice |
| `Lab036_Operators_Comparsion.py` | Comparison operators practice |
| `Lab037_Operators_Logical.py` | Logical operators practice |
| `Lab038_Operators_Example.py` | Operator examples |
| `Lab039_Operators_P8.py` | Operators practice |
| `Lab040_Operators_P9.py` | Operators practice |
| `Lab040_Ternary_Operator.py` | Ternary operator |
| `Lab041_User_Input_Ternary_Operators.py` | User input + ternary |
| `Lab042_Memership_Operator.py` | Membership operators (`in`, `not in`) |

### ex_05_Condition_Loops
| Lab | Topic |
|-----|-------|
| `Lab043_IF_Condition.py` | `if` condition |
| `Lab044_ELSEIF.py` | `elif` chains |
| `Lab046_if_else_elif.py` | `if` / `else` / `elif` |
| `src/ex_05_Condition_Loops/Lab043_IF_Condition_Optimized.py` | Optimized `if` example |

### ex_06_Switch_Match
| Lab | Topic |
|-----|-------|
| `LabSwitch01.py` | `match` statement |
| `LabSwitch02.py` | `match` statement practice |

### ex_07_Loops
| Lab | Topic |
|-----|-------|
| `Lab048_Loop.py` | Loops intro |
| `Lab050_For_Looops.py` | `for` loops |
| `Lab051_For_While.py` | `for` vs `while` |
| `Lab054_IQ.py` | Loop quiz |
| `Lab055_For_Break.py` | `break` in loops |
| `Lab056_pass.py` | `pass` statement |
| `Lab058.py` | Loop practice |
| `Lab059.py` | Loop practice |

### ex_08_Functions
| Lab | Topic |
|-----|-------|
| `Lab060_Built_In.py` | Built-in functions |
| `Lab061_Example_Functions.py` | Function examples |
| `Lab062_Example_Functions.py` | Function examples |
| `Lab063_Function_Parameter.py` | Function parameters |
| `Lab064_Type3_Function_return.py` | Functions with return |
| `Lab065_Function_Default_Parameter.py` | Default parameters |
| `Lab066_Functions_Return_Multiple_Values.py` | Returning multiple values |
| `Lab067_Functions_Keyword_Arg.py` | Keyword arguments |
| `Lab068_User_Input_Pass_Function.py` | User input + functions |
| `Lab069_Functions_Types.py` | Function types |
| `Lab071_IQ.py` | Function quiz |
| `Lab072_Infinite_Args.py` | `*args` (infinite arguments) |
| `Lab073_Real_Args.py` | Real-world argument patterns |
| `LabIQ02.py` | Function quiz 2 |

### ex_09_Functions_Scopes
| Lab | Topic |
|-----|-------|
| `Lab075_Local_Variable.py` | Local variables |
| `Lab076.py` | Scope practice |
| `Lab077_Local_Var.py` | Local variable scoping |
| `Lab078_Inner_Functions.py` | Inner (nested) functions |

### ex_10_Decortors
| Lab | Topic |
|-----|-------|
| `Lab079_Decortors.py` | Decorators |
| `Lab080_Decor.py` | Decorator practice |
| `Lab081.py` | Decorator practice |
| `Lab082.py` | Decorator practice |
| `Lab083.py` | Decorator practice |

### ex_11_TypeConversion
| Lab | Topic |
|-----|-------|
| `Lab087_Type_Conversion.py` | Type conversion (`int()`, `str()`, `float()`) |

### ex_12_Lambda_Exp
| Lab | Topic |
|-----|-------|
| `Lab090.py` | Lambda expressions |
| `Lab091_Lambda.py` | Lambda practice |
| `Lab094_User_Input_ODD_Even.py` | Odd/even with user input |

### ex_13_LIST
| Lab | Topic |
|-----|-------|
| `Lab096_List.py` | Lists |
| `Lab097.py` | List practice |
| `Lab098_POP.py` | `list.pop()` |

### ex_14_Tuple
| Lab | Topic |
|-----|-------|
| `Lab099_Tuple.py` | Tuples |
| `Lab100_Tuple.py` | Tuple practice |
| `Lab101.py` | Tuple practice |

### ex_15_SET_MAP_DICT
| Lab | Topic |
|-----|-------|
| `102.py` | Sets - the basics (unique items) |
| `103_SET.py` | Set operations: add/remove, union, intersection, difference |
| `104_Set_Advance.py` | set() from a list, len(), iteration, add() |
| `105_Extra.py` | Set comprehension + frozenset |

### ex_16_MAP_Filters
| Lab | Topic |
|-----|-------|
| `106.py` | `filter()` - keep even numbers |
| `107_Lab.py` | `filter()` + lambda - keep "PASS" results |
| `108.py` | `filter()` - drop empty strings |
| `109_Map.py` | `map()` - square each number |
| `110_Map2.py` | `map()` - uppercase names |
| `111_Map_IQ.py` | `map()` + lambda - ms to seconds |

### ex_17_Dict
| Lab | Topic |
|-----|-------|
| `112_Dict.py` | Dict basics: read/write/delete/loop/in |
| `113_Dict2.py` | Duplicate-key gotcha (last value wins) |
| `114_Dict_IQ.py` | Nested dicts in a list |
| `115_DictIQ2.py` | Deeper nested access |
| `116_Dict_Imp.py` | `dict(zip())` + merge with `|` |
| `117_IQ.py` | Character frequency counter |
| `118_IQ.py` | Dict equality (order-independent) |
| `119_Count_Vowel.py` | Count vowels in a string |

### ex_18_OOPs_Python
The full OOP journey in 10 sub-topics:

| Sub-folder | Topic | Labs |
|------------|-------|------|
| `01_Class_Object` | Class blueprint, attributes, methods, objects | 120, 122 |
| `02_Constructor` | `__init__`, parameterized & user-input constructors | 123–128 |
| `03_Instance_Variable` | Global vs class vs local variable scope | 129 |
| `04_Encapsulation` | public/protected/private, name mangling, dotenv | 130–136 |
| `05_Inheritance` | Single, multiple, multilevel, hierarchical, hybrid, MRO | 130–136 |
| `06_Polymorphism` | Method overloading (defaults) & overriding | 137–142 |
| `07_Abstraction` | `abc.ABC`, `@abstractmethod`, abstract chains | 143–147 |
| `08_Static` | Class attributes, `@staticmethod`, `@classmethod` | 148–154 |
| `09_Exceptions` | Error types, try/except/else/finally, raise, custom | 153–169 |
| `10_Modules` | Modules & built-in function references, image prompt | 170–173 |

**Key OOP concepts:** the `self` parameter (auto-injected), `__init__` constructors, name mangling (`_Class__private`), MRO for multiple inheritance, last-definition-wins overloading, abstract rules children must implement, static vs instance methods, and full exception handling.

### ex_19_Package
| File | Topic |
|------|-------|
| `170.py` | Import from a package + a single module |
| `package/__init__.py` | Marks the folder as a package |
| `package/util_module.py` | Module inside the package |
| `package/util_module2.py` | Second module (same fn name, no clash) |
| `mymodule.py` | Standalone single module |

### ex_20_Collections_FileIO
| Lab | Topic |
|-----|-------|
| `171.py` | `collections`: Counter, defaultdict |
| `172_Main.py` | `if __name__ == '__main__'` pattern |
| `173_Usage.py` | `__name__` guard with multiple functions |
| `174_OS.py` | `os.getcwd()`, `os.path.join()`, file read |
| `175_File.py` | Reading a text file |
| `176_Env.py` | Environment variables (python-dotenv) |
| `177.py` | `with open()` safe reading |
| `178.py` | Reading CSV with `csv` module |
| `179.py` | Reading CSV with pandas |

### ex_21_PyTest
| File | Topic |
|------|-------|
| `179.py` | Testing intro: Expected Result == Actual Result |
| `test_180.py` | pytest markers (`smoke`, `reg`) |
| `test_181.py` | Passing vs failing assertions |
| `PyTest_Cheatsheet.md` | pytest quick reference |

### Task (Daily Challenges & Practice)
| File | Topic |
|------|-------|
| `task1.py` | 3-number calculator (add, sub, mul, div) |
| `task2.py` | Quotient and remainder (`//`, `%`) |
| `task3.py` | Grade calculator (A–F) |
| `task4.py` | Sum of 3 numbers with defaults (100, 200, 300) |
| `task.py` | Empty task template |
| `Practice_1.py` | `print()` practice (`sep`, `end`) |
| `Practice_Keyword.py` | Keywords and `print()` full signature |
| `Practice_conditions.py` | Conditions: `if/else` + `match-case` |
| `practice_operators.py` | Operators practice |
| `practice_loop.py` | `for`/`while` loops, `range()`, even numbers |
| `practice_function.py` | Functions practice |
| `practice_function_2.py` | Global vs local scope (`UnboundLocalError`) |
| `practice_function_3.py` | Functions with default parameters |
| `variable.py` | Variables, complex numbers, type juggling |
| `set_map.py` | Sets, `filter()` vs `map()` |
| `setpractice.py` | Set practice + non-repeating characters |
| `decorator.py` | Decorators - wrapper, `@` syntax, chaining |
| `lambda.py` | Lambda expressions vs regular functions |
| `dictPracti.py` | Dict practice |
| `map.py` | `filter()`/`map()` practice |
| `brackets.py` | `[]` vs `()` vs `{}` study reference |
| `IQ.py` | Character frequency counter |
| `module_os.py` | `os` module basics |
| `class.py`, `classpractice.py`, `classpractice2.py` | Class & object practice |
| `oops.py`, `constructor.py`, `user_inoutpracticeclass.py` | Constructor practice |
| `encap.py`, `encap2.py` | Encapsulation + dotenv login |
| `inhirit.py`, `poly.py`, `abstract.py`, `abs2.py`, `static.py` | Inheritance, polymorphism, abstraction, static methods |
| `exception.py` | try/except/else/finally practice |
| `.env` | Credentials for the dotenv practice scripts |

### autoweave (Playwright Browser Automation)
| File | Topic |
|------|-------|
| `loginHR.py` | End-to-end login flow test (Playwright + pytest) |

See [autoweave/README.md](autoweave/README.md) for full setup (venv, Playwright Chromium install, run commands) and troubleshooting.

## Getting Started

### Prerequisites

- Python 3.x installed
- The project venv lives at `chapter_11_Python_Learning/.venv` (contains python-dotenv)
- `pandas` and `requests` for specific labs in ex_20 / ex_18
- The `autoweave` tests additionally need `uv`, `pytest`, `playwright` and the Chromium browser — see [autoweave/README.md](autoweave/README.md).

### Running the exercises

From the `chapter_11_Python_Learning` directory, run any lab with the venv Python:

```powershell
.\\.venv\Scripts\python.exe ex_01_Python_Basics\Lab001_Hello.py
.\\.venv\Scripts\python.exe ex_16_MAP_Filters\109_Map.py
.\\.venv\Scripts\python.exe ex_18_OOPs_Python\02_Constructor\124_DC.py
.\\.venv\Scripts\python.exe Task\task1.py
```

Some exercises (e.g. `Lab021`, `Lab022`, `Lab023`, `Task/task1.py`) prompt for input — type your values and press Enter when prompted.

### Running the pytest labs

```powershell
.\\.venv\Scripts\python.exe -m pytest ex_21_PyTest
```

## Learning Path

1. Start with **ex_01** to get comfortable with `print()` and comments.
2. Move to **ex_02** and **ex_03** for keywords, identifiers, variables, literals, data types, and user input.
3. Practice operators (**ex_04**), then make decisions with conditionals (**ex_05**) and `match` (**ex_06**).
4. Automate repetition with loops (**ex_07**).
5. Reuse logic with functions (**ex_08**), understand scopes (**ex_09**), and decorate functions (**ex_10**).
6. Convert types (**ex_11**) and write concise logic with lambdas (**ex_12**).
7. Organize data with lists (**ex_13**), tuples (**ex_14**), sets (**ex_15**), map/filter (**ex_16**), and dicts (**ex_17**).
8. Learn **full OOP** in **ex_18** — classes, constructors, encapsulation, inheritance, polymorphism, abstraction, static methods, exceptions.
9. Structure code with modules & packages (**ex_19**), work with files and env vars (**ex_20**), and verify code with pytest (**ex_21**).
10. Solidify each topic with the daily **Task** challenges.
11. Apply it all to real browser automation with **autoweave** (Playwright).
12. Build your first **AI agent** in `chapter_12_CrewAI` (in the repo root).

This path builds the Python foundation for building **AI agents** — variables, functions, and control flow are the same building blocks agents use to process input, make decisions, and take actions.

## Contributing

This is a learning repository. If you'd like to add exercises or improve existing ones, feel free to add lab files following the existing `LabXXX_Topic.py` naming convention.

## License

All content is for personal learning purposes.
