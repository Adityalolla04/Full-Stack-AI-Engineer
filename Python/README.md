# Python

This folder is a set of short lessons that move from the basics to everyday Python tools. Each numbered folder has a `README.md` for the topic and a runnable `.py` file with examples. Try changing the values and running the file again; that is often the quickest way to see what a concept does.

## Lessons

| # | Topic | Lesson |
|---|---|---|
| 01 | Syntax, types, and operators | [Notes](01-syntax-types-and-operators/README.md) · [Examples](01-syntax-types-and-operators/syntax-types-operators.py) |
| 02 | Control flow and functions | [Notes](02-control-flow-and-functions/README.md) · [Examples](02-control-flow-and-functions/control-flow-functions.py) |
| 03 | Collections and comprehensions | [Notes](03-collections-and-comprehensions/README.md) · [Examples](03-collections-and-comprehensions/collections-comprehensions.py) |
| 04 | Strings, files, and exceptions | [Notes](04-strings-files-and-exceptions/README.md) · [Examples](04-strings-files-and-exceptions/strings-files-exceptions.py) |
| 05 | OOP and dataclasses | [Notes](05-oop-and-dataclasses/README.md) · [Examples](05-oop-and-dataclasses/oop-dataclasses.py) |
| 06 | Modules, packages, and environments | [Notes](06-modules-packages-and-environments/README.md) · [Examples](06-modules-packages-and-environments/modules-packages-environments.py) |
| 07 | Iterators, generators, and context managers | [Notes](07-iterators-generators-and-context-managers/README.md) · [Examples](07-iterators-generators-and-context-managers/iterators-generators-context-managers.py) |
| 08 | Decorators and functional tools | [Notes](08-decorators-and-functional-tools/README.md) · [Examples](08-decorators-and-functional-tools/decorators-functional-tools.py) |
| 09 | Typing, testing, and debugging | [Notes](09-typing-testing-and-debugging/README.md) · [Examples](09-typing-testing-and-debugging/typing-testing-debugging.py) |
| 10 | Async, concurrency, and multiprocessing | [Notes](10-async-concurrency-and-multiprocessing/README.md) · [Examples](10-async-concurrency-and-multiprocessing/async-concurrency-multiprocessing.py) |
| 11 | NumPy and pandas | [Notes](11-numpy-and-pandas/README.md) · [Examples](11-numpy-and-pandas/numpy-pandas.py) |
| 12 | Logging, configuration, and reproducibility | [Notes](12-logging-configuration-and-reproducibility/README.md) · [Examples](12-logging-configuration-and-reproducibility/logging-configuration-reproducibility.py) |

## Running a lesson

From the repository root, run a file with Python. For example:

```powershell
python .\Python\01-syntax-types-and-operators\syntax-types-operators.py
```

The first ten lessons use the standard library. Lessons 11 and 12 also need NumPy; lesson 11 needs pandas as well:

```powershell
python -m pip install numpy pandas
```

The examples are meant to be read and edited. They are not a test suite, so run one lesson at a time and follow any prompts printed by that file.
