# Python - Complete Learning Path

A comprehensive guide to Python programming from fundamentals to advanced topics.

## Overview

This learning path covers 12 essential Python concepts, each with:
- **README.md**: Detailed bullet-point notes for quick reference
- **{concept_name}.py**: Runnable Python file with comprehensive examples and practice exercises
- **practice/**: Space for your own implementation and experiments

## Concept Index

1. **[Syntax, Types, and Operators](01-syntax-types-and-operators/README.md)**
   - Numeric types (int, float, complex)
   - Strings and string operations
   - Boolean logic and None
   - Type conversion and checking
   - Identity vs equality
   - File: `syntax-types-operators.py`

2. **[Control Flow and Functions](02-control-flow-and-functions/README.md)**
   - if-elif-else statements
   - for and while loops
   - break and continue
   - Function definition and parameters
   - Scope and variable lifetime
   - Lambda and higher-order functions
   - Recursion and decorators
   - File: `control-flow-functions.py`

3. **[Collections and Comprehensions](03-collections-and-comprehensions/README.md)**
   - Lists (mutable, ordered)
   - Tuples (immutable, ordered)
   - Dictionaries (key-value pairs)
   - Sets (unique, unordered)
   - Comprehensions (list, dict, set)
   - zip() and unpacking
   - File: `collections-comprehensions.py`

4. **[Strings, Files, and Exceptions](04-strings-files-and-exceptions/README.md)**
   - String methods and operations
   - String encoding/decoding
   - File I/O (read, write, append)
   - Context managers (with statement)
   - Exception handling (try-except-finally)
   - Custom exceptions
   - File: `strings-files-exceptions.py`

5. **[OOP and Dataclasses](05-oop-and-dataclasses/README.md)**
   - Class definition and initialization
   - Instance and class variables
   - Methods (instance, class, static)
   - Inheritance and polymorphism
   - Encapsulation (public, private)
   - Magic methods (__init__, __str__, etc.)
   - Properties and dataclasses
   - File: `oop-dataclasses.py`

6. **[Modules, Packages, and Environments](06-modules-packages-and-environments/README.md)**
   - Importing modules and packages
   - Creating and using modules
   - Package structure (__init__.py)
   - Built-in modules (os, sys, pathlib)
   - Module vs script behavior
   - Virtual environments
   - pip and package management
   - File: `modules-packages-environments.py`

7. **[Iterators, Generators, and Context Managers](07-iterators-generators-and-context-managers/README.md)**
   - Iterators (__iter__, __next__)
   - Generator functions (yield)
   - Generator expressions
   - Lazy evaluation
   - Context managers (with, __enter__, __exit__)
   - Resource management
   - File: `iterators-generators-context-managers.py`

8. **[Decorators and Functional Tools](08-decorators-and-functional-tools/README.md)**
   - Decorator basics and syntax
   - Decorators with arguments
   - Stacking decorators
   - functools (wraps, lru_cache)
   - map(), filter(), reduce()
   - Partial functions
   - Closures
   - File: `decorators-functional-tools.py`

9. **[Typing, Testing, and Debugging](09-typing-testing-and-debugging/README.md)**
   - Type hints and annotations
   - Type checking concepts
   - pytest basics and assertions
   - Test organization
   - Debugging with print, logging, pdb
   - Error handling
   - File: `typing-testing-debugging.py`

10. **[Async, Concurrency, and Multiprocessing](10-async-concurrency-and-multiprocessing/README.md)**
    - Threading basics
    - Locks and synchronization
    - Multiprocessing
    - async/await syntax
    - Concurrency patterns
    - Performance considerations
    - File: `async-concurrency-multiprocessing.py`

11. **[NumPy and Pandas](11-numpy-and-pandas/README.md)**
    - NumPy arrays and operations
    - Array indexing and slicing
    - Mathematical operations
    - Pandas Series and DataFrames
    - Reading and writing data
    - Data manipulation and filtering
    - GroupBy operations
    - File: `numpy-pandas.py`

12. **[Logging, Configuration, and Reproducibility](12-logging-configuration-and-reproducibility/README.md)**
    - Logging levels and handlers
    - Configuration (basicConfig, config files)
    - Random seed and reproducibility
    - Environment variables
    - Configuration management (.env, .yaml)
    - Reproducible code patterns
    - File: `logging-configuration-reproducibility.py`

## How to Use This Learning Path

### Study Method

1. **Read the README.md** for your concept
   - Understand core concepts
   - Review bullet points
   - Check recall checklist

2. **Run the Python file** (e.g., `syntax-types-operators.py`)
   - See practical examples
   - Understand how concepts work
   - Review practice exercises

3. **Implement your own** in the practice folder
   - Write code without looking at examples
   - Create your own exercises
   - Test your understanding

4. **Revisit at intervals** - 1 day, 7 days, 30 days
   - Re-read notes from memory
   - Redo exercises
   - Explain concepts to others

### Success Criteria

You've mastered a concept when you can:
- [ ] Explain it in your own words
- [ ] Identify when to use it
- [ ] Write working code without reference
- [ ] Explain edge cases and limitations
- [ ] Teach it to someone else

## Running Examples

Each concept file is standalone and runnable:

```bash
python 01-syntax-types-and-operators/syntax-types-operators.py
python 02-control-flow-and-functions/control-flow-functions.py
# ... etc
```

All examples use `print()` statements to show output, making it easy to:
- Trace execution
- Understand function behavior
- See comparison results
- Debug your understanding

## Learning Progression

**Fundamentals** (Start here)
- Concept 1: Syntax, Types, and Operators
- Concept 2: Control Flow and Functions
- Concept 3: Collections and Comprehensions

**Intermediate** (Core Python)
- Concept 4: Strings, Files, and Exceptions
- Concept 5: OOP and Dataclasses
- Concept 6: Modules, Packages, and Environments

**Advanced** (Python Mastery)
- Concept 7: Iterators, Generators, and Context Managers
- Concept 8: Decorators and Functional Tools
- Concept 9: Typing, Testing, and Debugging
- Concept 10: Async, Concurrency, and Multiprocessing

**Specialized** (Domain-Specific)
- Concept 11: NumPy and Pandas (Data Science)
- Concept 12: Logging, Configuration, Reproducibility (Production Code)

## Common Learning Mistakes

1. **Reading without practicing**: Passive reading doesn't build skills
2. **Skipping fundamentals**: Later concepts depend on earlier ones
3. **Not doing practice exercises**: Coding is the only way to learn
4. **Memorizing instead of understanding**: Focus on why, not what
5. **Ignoring edge cases**: Real code must handle boundary conditions
6. **Not testing your code**: Testing reveals misunderstandings
7. **Leaving gaps**: Go back and master concepts you skipped
8. **Comparing your progress to others**: Progress is personal

## Python Version

All examples are written for **Python 3.8+** and use modern syntax:
- f-strings (Python 3.6+)
- Type hints (Python 3.5+)
- Walrus operator (Python 3.8+)
- Match statements (Python 3.10+)

## Additional Resources

- **Official Python**: [docs.python.org](https://docs.python.org/3/)
- **Style Guide**: [PEP 8](https://pep8.org/)
- **Type Hints**: [PEP 484](https://www.python.org/dev/peps/pep-0484/)
- **Design Patterns**: [Design Patterns in Python](https://refactoring.guru/design-patterns/python)
- **Best Practices**: [Real Python](https://realpython.com/)

## Contributing

If you find errors or have suggestions:
1. Test thoroughly
2. Add examples for clarity
3. Update both .py file and README
4. Maintain consistent style and formatting

## Your Existing Practice Material

- Original notebooks are preserved in `practice/existing/` folders
- Refer to [EXISTING-WORK.md](EXISTING-WORK.md) for coverage details
- Use as reference or revision material
