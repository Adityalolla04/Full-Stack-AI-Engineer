# Strings, Files, and Exceptions

[Back to Python](../README.md)

## In Simple Words

Text processing is fundamental. File I/O requires careful resource management. Exceptions allow programs to handle unexpected situations gracefully.

## Core Concepts

### 1. **String Methods and Operations**
- **Case**: `.upper()`, `.lower()`, `.title()`, `.capitalize()`, `.swapcase()`
- **Whitespace**: `.strip()`, `.lstrip()`, `.rstrip()`, `.split()`, `.splitlines()`
- **Search**: `.find(sub)`, `.count(sub)`, `.startswith(pre)`, `.endswith(suf)`, `.index(sub)`
- **Replace**: `.replace(old, new)`, `.translate()` (for multiple)
- **Join**: `separator.join(iterable)` - efficient concatenation
- **Formatting**: `.format()`, f-strings (f"value: {x}")
- **Check type**: `.isdigit()`, `.isalpha()`, `.isalnum()`, `.isspace()`

### 2. **String Encoding/Decoding**
- **Bytes vs Strings**:
  - String: text, human-readable
  - Bytes: binary data, machine-readable

- **Encoding** (string → bytes):
  - `"hello".encode("utf-8")` → `b'hello'`
  - Default: UTF-8 (recommended)
  - Other: ASCII, latin-1, utf-16

- **Decoding** (bytes → string):
  - `b'hello'.decode("utf-8")` → `"hello"`
  - Must know correct encoding

- **Common encodings**:
  - UTF-8: Universal, handles all Unicode
  - ASCII: English only, 7-bit
  - Latin-1: Western European
  - UTF-16: Fixed-width, less common

### 3. **File I/O Basics**
- **Opening files**: `open(filename, mode)`
  - 'r': Read (default)
  - 'w': Write (overwrites)
  - 'a': Append
  - 'x': Create (fails if exists)
  - '+': Read and write
  - 'b': Binary mode (e.g., 'rb', 'wb')

- **File operations**:
  - `.read()`: Read entire file as string
  - `.readline()`: Read one line
  - `.readlines()`: Read all lines as list
  - `.write(text)`: Write text
  - `.writelines(list)`: Write multiple lines
  - `.seek(position)`: Move file pointer
  - `.tell()`: Get current position

- **File methods**:
  - `.close()`: Close file (important!)
  - `.flush()`: Write buffered data
  - `.isatty()`: Check if interactive

### 4. **Context Managers (with statement)**
- **Purpose**: Automatic resource cleanup
  - Opens resource on enter
  - Closes resource on exit (even if error)
  - No need to remember `.close()`

- **Syntax**: `with open(file) as f:`
  - Code inside with block can use f
  - After block, f automatically closes

- **Benefits**:
  - Exception-safe
  - Cleaner code
  - Ensures cleanup happens

- **Custom context managers**:
  - Implement `__enter__()` and `__exit__()`
  - Used for resource management

### 5. **Reading Files**
- **Read entire file**:
  ```python
  with open('file.txt', 'r') as f:
      content = f.read()  # String
  ```

- **Read line by line**:
  ```python
  with open('file.txt', 'r') as f:
      for line in f:  # Efficient, doesn't load entire file
          process(line)
  ```

- **Read all lines**:
  ```python
  with open('file.txt', 'r') as f:
      lines = f.readlines()  # List of strings
  ```

### 6. **Writing Files**
- **Write mode** (overwrites):
  ```python
  with open('file.txt', 'w') as f:
      f.write("Hello, World!")
  ```

- **Append mode** (adds to end):
  ```python
  with open('file.txt', 'a') as f:
      f.write("\nNew line")
  ```

- **Write multiple lines**:
  ```python
  lines = ["line1\n", "line2\n", "line3\n"]
  with open('file.txt', 'w') as f:
      f.writelines(lines)
  ```

### 7. **Exception Handling**
- **try-except block**: Catch and handle errors
  ```python
  try:
      risky_code()
  except SpecificError as e:
      handle_error(e)
  ```

- **Exception types** (most common):
  - `ValueError`: Invalid value for operation
  - `TypeError`: Wrong type
  - `KeyError`: Dictionary key not found
  - `IndexError`: List index out of range
  - `FileNotFoundError`: File doesn't exist
  - `IOError`: Input/output operation fails
  - `ZeroDivisionError`: Division by zero
  - `AttributeError`: Attribute doesn't exist
  - `NameError`: Variable not defined

- **Multiple except blocks**:
  ```python
  try:
      code()
  except FileNotFoundError:
      print("File not found")
  except ValueError:
      print("Invalid value")
  except Exception:  # Catch all
      print("Something went wrong")
  ```

- **Bare except** (don't use):
  - `except:` catches everything including KeyboardInterrupt
  - Use `except Exception:` instead

### 8. **try-except-finally**
- **finally block**: Always runs (cleanup code)
  ```python
  try:
      file = open('file.txt')
      process(file)
  except FileNotFoundError:
      print("File not found")
  finally:
      file.close()  # Always runs
  ```

- **Common pattern with context manager** (preferred):
  ```python
  with open('file.txt') as file:
      process(file)  # Cleanup automatic
  ```

- **else block**: Runs if no exception
  ```python
  try:
      risky()
  except SpecificError:
      handle_error()
  else:
      process_success()  # Only if no error
  finally:
      cleanup()
  ```

### 9. **Raising Exceptions**
- **Raise errors**:
  ```python
  if x < 0:
      raise ValueError("x must be positive")
  ```

- **Re-raise exceptions**:
  ```python
  try:
      code()
  except SomeError:
      log_error()
      raise  # Re-raise same exception
  ```

- **Custom exceptions**:
  ```python
  class CustomError(Exception):
      pass
  
  raise CustomError("message")
  ```

### 10. **Best Practices**
- **Be specific**: Catch specific exceptions, not all
- **Use context managers**: Always use `with` for file I/O
- **Handle close to raising**: Catch exceptions near where they occur
- **Log errors**: Record error details for debugging
- **Don't silence errors**: At least log or re-raise
- **Clean up resources**: Use finally or with statement
- **Validate input**: Check before processing
- **Meaningful messages**: Exception messages should help debugging

## Common Mistakes

1. **Not closing files**: Use `with` statement always
2. **Catching too broadly**: Don't catch all exceptions
3. **Not distinguishing errors**: Each error needs appropriate handling
4. **Modifying string in place**: Strings are immutable, need reassignment
5. **Wrong encoding**: Specify encoding when opening files
6. **Not using context managers**: Manual close() is error-prone
7. **Silencing errors**: Don't catch exceptions without handling
8. **File mode confusion**: Remember 'w' overwrites, 'a' appends

## Practice Exercises

1. **String manipulation**: Implement text preprocessing functions
2. **File reading**: Read CSV/JSON and parse data
3. **File writing**: Create formatted output files
4. **Exception handling**: Build error-resistant file processor
5. **Encoding issues**: Handle different character encodings
6. **Custom exceptions**: Create domain-specific error types
7. **Context managers**: Build custom resource managers
8. **Robust I/O**: Handle missing files, corrupt data, disk full

## Reference Implementation

Run `strings-files-exceptions.py` to see comprehensive examples and exercises.

## Recall Checklist

- [ ] Common string methods and their uses
- [ ] Encoding and decoding strings
- [ ] File modes (r, w, a, b)
- [ ] Reading files (read, readline, readlines)
- [ ] Writing files safely
- [ ] with statement for resource management
- [ ] try-except-finally pattern
- [ ] Common exception types
- [ ] Raising custom exceptions

## Resources

- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python File I/O](https://docs.python.org/3/tutorial/inputoutput.html)
- [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [AlgoMaster Python Roadmap](https://algomaster.io/roadmaps/python)
