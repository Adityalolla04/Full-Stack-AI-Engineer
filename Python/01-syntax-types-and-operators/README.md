# Syntax, Types, and Operators

[Back to Python](../README.md)

## In Simple Words

Python is a dynamically-typed language where everything is an object with a type. Understanding types and operators is fundamental to writing correct Python code.

## Core Concepts

### 1. **Numeric Types**
- **int**: Integer numbers (positive, negative, zero)
  - Python 3 integers have unlimited precision
  - Examples: `42`, `-100`, `0`
  - Use `type(value)` to check
  
- **float**: Decimal numbers
  - Floating-point representation (IEEE 754 standard)
  - May have precision issues due to binary representation
  - Examples: `3.14`, `-2.5`, `1e-3` (scientific notation)
  
- **complex**: Complex numbers with real and imaginary parts
  - Format: `real + imagj`
  - Examples: `3 + 4j`, `1j` (imaginary unit)
  - Useful for advanced mathematics and engineering calculations

### 2. **String Types and Operations**
- **String basics**
  - Single quotes: `'Hello'`, Double quotes: `"Hello"`
  - Triple quotes for multi-line: `"""text"""`
  - Strings are immutable sequences

- **String operations**
  - Concatenation: `"Hello" + " " + "World"`
  - Repetition: `"Ha" * 3` → `"HaHaHa"`
  - Indexing: `text[0]` (first char), `text[-1]` (last char)
  - Slicing: `text[1:4]`, `text[:3]`, `text[2:]`, `text[::2]` (every 2nd char)
  - Length: `len(text)`

- **String methods**
  - Case: `.upper()`, `.lower()`, `.title()`
  - Whitespace: `.strip()`, `.lstrip()`, `.rstrip()`
  - Search: `.find()`, `.count()`, `.startswith()`, `.endswith()`
  - Modify: `.replace()`, `.split()`, `.join()`
  - Format: `.format()` method, f-strings

- **String formatting**
  - f-strings (recommended): `f"Name: {name}, Age: {age}"`
  - `.format()` method: `"Name: {}, Age: {}".format(name, age)`
  - % formatting (older): `"Name: %s, Age: %d" % (name, age)`

### 3. **Boolean Type**
- **True and False**: Boolean literals represent logic values
  - `bool(True)` and `bool(False)` are type objects
  - Results from comparison and logical operations

- **Comparison operators**
  - Equality: `==` (value equality), `!=` (not equal)
  - Relational: `<`, `>`, `<=`, `>=`
  - Chained comparisons: `a < b < c` (more readable than `a < b and b < c`)

- **Logical operators**
  - `and`: Both conditions must be true (short-circuit evaluation)
  - `or`: At least one condition must be true (short-circuit evaluation)
  - `not`: Negation of boolean value

- **Truthiness**: Values that evaluate to True/False in boolean context
  - **Falsy values**: `0`, `0.0`, `""`, `[]`, `{}`, `None`, `False`
  - **Truthy values**: Any non-zero number, non-empty string, non-empty collection, `True`
  - Used in `if` statements and `while` loops

### 4. **None Type**
- **None**: Special singleton value representing absence of value
  - Different from `0`, `False`, or empty string
  - Default return value of functions without explicit return
  - Used to indicate "no value" or uninitialized state
  - `bool(None)` evaluates to `False`

### 5. **Identity vs. Equality**
- **Equality (`==`, `!=`)**: Checks if values are the same
  - Example: `[1, 2] == [1, 2]` → `True`

- **Identity (`is`, `is not`)**: Checks if objects are the same in memory
  - Example: `a = [1, 2]; b = [1, 2]; a is b` → `False` (different objects)
  - `a = [1, 2]; b = a; a is b` → `True` (same object reference)
  - Integer caching: `-5` to `256` are cached by Python for performance

- **When to use**
  - Use `==` for value comparison (most common)
  - Use `is` when comparing with `None`, `True`, `False`, or checking object identity

### 6. **Type Conversion**
- **int()**: Convert to integer
  - From float: `int(3.9)` → `3` (truncates decimal)
  - From string: `int("42")` → `42`
  - From boolean: `int(True)` → `1`, `int(False)` → `0`

- **float()**: Convert to float
  - From int: `float(5)` → `5.0`
  - From string: `float("3.14")` → `3.14`
  - Special values: `float('inf')`, `float('-inf')`, `float('nan')`

- **str()**: Convert to string
  - From number: `str(42)` → `"42"`
  - From boolean: `str(True)` → `"True"`
  - Most types can be converted to string representation

- **bool()**: Convert to boolean
  - Falsy values convert to `False`: `0`, `0.0`, `""`, `[]`, `{}`, `None`
  - Truthy values convert to `True`: non-zero numbers, non-empty strings, non-empty collections

- **Decimal**: For precise decimal arithmetic (avoid float precision issues)
  - Use `from decimal import Decimal`
  - `Decimal('2.765')` preserves exact decimal representation

### 7. **Mutability**
- **Immutable types**: Cannot be changed after creation
  - int, float, string, tuple, frozenset, bool, None
  - Any operation creates a new object
  - Safer for function arguments (no unexpected side effects)

- **Mutable types**: Can be changed in place
  - list, dict, set, bytearray
  - Operations may modify the object
  - Need careful handling in functions

### 8. **Variables and Scope**
- **Variable assignment**: Name binding to object
  - `x = 42` - binds name `x` to integer object `42`
  - Variables are just references, not containers

- **Multiple assignment**: Assign multiple values at once
  - `x, y, z = 1, 2, 3`
  - Useful for swapping: `a, b = b, a`

- **Augmented assignment**: Shorthand operators
  - `x += 5` is equivalent to `x = x + 5`
  - Also: `-=`, `*=`, `/=`, `//=`, `%=`, `**=`

### 9. **Built-in Functions for Numeric Operations**
- **Rounding and math**
  - `round(3.7)` → `4` (banker's rounding to nearest even)
  - `round(3.141, 2)` → `3.14` (specify decimal places)
  - `abs(-7)` → `7` (absolute value)
  - `pow(2, 3)` → `8` (exponentiation)
  - `pow(2, 3, 5)` → `3` (modular exponentiation: 2³ mod 5)

- **Aggregation**
  - `min(2, 3, 4)` → `2` (minimum value)
  - `max(2, 3, 4)` → `4` (maximum value)
  - Works with lists, tuples, or individual arguments

- **Math module** (import required)
  - `math.ceil(3.2)` → `4` (round up)
  - `math.floor(3.9)` → `3` (round down)
  - `math.sqrt(16)` → `4.0` (square root)
  - `math.pi`, `math.e` (mathematical constants)

### 10. **Membership Operators**
- **in**: Check if element exists in sequence/collection
  - `"apple" in ["apple", "banana"]` → `True`
  - `"Py" in "Python"` → `True` (substring check)

- **not in**: Opposite of `in`
  - `"grape" not in ["apple", "banana"]` → `True`

### 11. **Type Checking**
- **type()**: Get exact type of object
  - `type(42)` → `<class 'int'>`
  - Returns the type object itself

- **isinstance()**: Check if object is instance of class/type
  - `isinstance(42, int)` → `True`
  - Preferred over `type()` for inheritance compatibility
  - Multiple types: `isinstance(42, (int, float))` → `True`

## Common Mistakes

1. **Using `==` for object identity**: Use `is` only for singleton checks (None, True, False)
2. **Confusing float precision**: `0.1 + 0.2 != 0.3` (use `Decimal` for precise arithmetic)
3. **Expecting mutable default arguments**: Default arguments are evaluated once at function definition
4. **Type comparison with `type()`**: Use `isinstance()` for better practice
5. **String concatenation in loops**: Creates new string each time (inefficient)
6. **Assuming integer division**: `5 / 2` → `2.5` (float), use `//` for integer division
7. **Modifying object while iterating**: Can cause skipped/unexpected iterations

## Practice Exercises

1. **Type Conversions**: Demonstrate 5 different type conversions with examples
2. **String Operations**: Implement string reversal, palindrome checker, character counting
3. **Comparison Logic**: Create functions using multiple comparison operators
4. **Temperature Conversion**: Write function to convert Celsius to Fahrenheit and vice versa
5. **Number Operations**: Implement GCD (greatest common divisor), factorization
6. **Identity vs Equality**: Create examples showing difference between `==` and `is`
7. **Boolean Logic**: Build functions using `and`, `or`, `not` operators

## Reference Implementation

Run `syntax-types-operators.py` to see comprehensive examples of all concepts covered above.

## Recall Checklist

- [ ] Can explain immutability vs mutability with examples
- [ ] Can distinguish between `==` and `is` operators
- [ ] Can demonstrate type conversion with edge cases
- [ ] Can use string slicing and methods correctly
- [ ] Can explain truthiness and falsy values
- [ ] Can write functions with proper parameter handling
- [ ] Can use built-in functions (round, abs, min, max, pow)
- [ ] Can identify common pitfalls in numeric operations

## Resources

- [Python Official Type System](https://docs.python.org/3/library/stdtypes.html)
- [AlgoMaster Python Roadmap](https://algomaster.io/roadmaps/python)
- [PEP 8 - Python Style Guide](https://pep8.org/)
