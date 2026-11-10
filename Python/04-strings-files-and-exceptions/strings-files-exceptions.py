"""
Strings, Files, and Exceptions - Core Python Concepts

This module covers essential Python concepts for data handling and error management:
- String methods and operations (upper, lower, split, join, strip, replace, find, format)
- String encoding/decoding (utf-8, ASCII)
- Working with files (open, read, write, append, close, context manager)
- File operations (readlines, writelines, seek, tell)
- Exception handling (try-except-finally, custom exceptions)
- Exception types (ValueError, TypeError, FileNotFoundError, etc.)
"""

import os

# ============================================================================
# 1. STRING METHODS AND OPERATIONS
# ============================================================================

print("\n" + "="*70)
print("1. STRING METHODS AND OPERATIONS")
print("="*70)

# Case conversion methods
print("\n--- Case Conversion ---")
text = "Python Programming is FUN"
print(f"Original: {text}")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Title: {text.title()}")
print(f"Capitalize: {text.capitalize()}")
print(f"Swapcase: {text.swapcase()}")

# String splitting and joining
print("\n--- Split and Join ---")
sentence = "Python is awesome and powerful"
print(f"Original: {sentence}")

words = sentence.split()
print(f"Split by spaces: {words}")

csv_data = "apple,banana,orange,mango"
fruits = csv_data.split(",")
print(f"Split by comma: {fruits}")

# Join method
print(f"Join with ' | ': {' | '.join(fruits)}")
print(f"Join with '-': {'-'.join(['2024', '11', '07'])}")

# Strip, lstrip, rstrip
print("\n--- Strip Methods ---")
padded_text = "   Hello World   "
print(f"Original: '{padded_text}'")
print(f"Strip: '{padded_text.strip()}'")
print(f"Lstrip: '{padded_text.lstrip()}'")
print(f"Rstrip: '{padded_text.rstrip()}'")

# Custom strip character
custom_pad = "###Python###"
print(f"Original: '{custom_pad}'")
print(f"Strip '#': '{custom_pad.strip('#')}'")

# Replace method
print("\n--- Replace Method ---")
text_to_replace = "Hello World, Hello Universe"
print(f"Original: {text_to_replace}")
print(f"Replace 'Hello' with 'Hi': {text_to_replace.replace('Hello', 'Hi')}")
print(f"Replace 'Hello' with 'Hi' (first 1 occurrence): {text_to_replace.replace('Hello', 'Hi', 1)}")

# Find and index methods
print("\n--- Find and Index Methods ---")
text_search = "Python is great, Python is powerful"
print(f"Text: {text_search}")
print(f"Find 'Python': {text_search.find('Python')}")
print(f"Find 'is': {text_search.find('is')}")
print(f"Find 'Java': {text_search.find('Java')} (not found, returns -1)")
print(f"Count 'Python': {text_search.count('Python')}")

# String formatting
print("\n--- String Formatting ---")
name = "Aditya"
age = 25
score = 92.5

# f-strings (modern way)
print(f"Name: {name}, Age: {age}, Score: {score}")
print(f"Score with 2 decimals: {score:.2f}")
print(f"Integer formatting: {age:05d} (zero-padded)")

# .format() method
print("Using .format(): {}, {}, {}".format(name, age, score))
print("Named format: Name={n}, Age={a}".format(n=name, a=age))

# % formatting (older way)
print("Old style: %s, %d, %.1f" % (name, age, score))

# String methods for checking
print("\n--- String Checking Methods ---")
test1 = "12345"
test2 = "Hello123"
test3 = "HELLO"
print(f"'{test1}'.isdigit(): {test1.isdigit()}")
print(f"'{test2}'.isdigit(): {test2.isdigit()}")
print(f"'{test3}'.isupper(): {test3.isupper()}")
print(f"'{test3}'.islower(): {test3.islower()}")
print(f"'   '.isspace(): {'   '.isspace()}")
print(f"'{test1}'.isalnum(): {test1.isalnum()}")

# ============================================================================
# 2. STRING ENCODING AND DECODING
# ============================================================================

print("\n" + "="*70)
print("2. STRING ENCODING AND DECODING")
print("="*70)

# UTF-8 encoding
print("\n--- UTF-8 Encoding ---")
text_utf8 = "Hello, 世界, नमस्ते"
print(f"Original string: {text_utf8}")

encoded = text_utf8.encode('utf-8')
print(f"Encoded to UTF-8 bytes: {encoded}")
print(f"Type: {type(encoded)}")

decoded = encoded.decode('utf-8')
print(f"Decoded back: {decoded}")

# ASCII encoding (limited)
print("\n--- ASCII Encoding ---")
ascii_text = "Hello World"
print(f"Original: {ascii_text}")
encoded_ascii = ascii_text.encode('ascii')
print(f"ASCII encoded: {encoded_ascii}")
decoded_ascii = encoded_ascii.decode('ascii')
print(f"Decoded: {decoded_ascii}")

# Different encodings
print("\n--- Different Encodings ---")
multilingual = "Python"
for encoding in ['utf-8', 'ascii', 'latin-1']:
    try:
        encoded = multilingual.encode(encoding)
        print(f"{encoding}: {encoded}")
    except UnicodeEncodeError as e:
        print(f"{encoding}: Error - {e}")

# ============================================================================
# 3. FILE OPERATIONS
# ============================================================================

print("\n" + "="*70)
print("3. FILE OPERATIONS")
print("="*70)

# Create a test file for demonstration
test_file = "test_file.txt"
test_file_append = "test_append.txt"
test_file_lines = "test_lines.txt"

# Writing to files
print("\n--- Writing to Files ---")
print("Writing to file...")
with open(test_file, 'w') as f:
    f.write("Hello, World!\n")
    f.write("This is a test file.\n")
    f.write("Python file operations are useful.\n")
print(f"Data written to {test_file}")

# Reading from files
print("\n--- Reading from Files ---")
with open(test_file, 'r') as f:
    content = f.read()
    print(f"Content:\n{content}")

# Reading line by line
print("\n--- Reading Line by Line ---")
with open(test_file, 'r') as f:
    for line_num, line in enumerate(f, 1):
        print(f"Line {line_num}: {line.rstrip()}")

# Readline vs readlines
print("\n--- Readline vs Readlines ---")
with open(test_file, 'r') as f:
    first_line = f.readline()
    print(f"First line (readline): {first_line.rstrip()}")

with open(test_file, 'r') as f:
    all_lines = f.readlines()
    print(f"All lines (readlines): {all_lines}")

# Appending to files
print("\n--- Appending to Files ---")
print("Appending to file...")
with open(test_file, 'a') as f:
    f.write("This line was appended.\n")
print(f"Data appended to {test_file}")

with open(test_file, 'r') as f:
    print(f"Updated content:\n{f.read()}")

# File seek and tell
print("\n--- File Seek and Tell ---")
with open(test_file, 'r') as f:
    print(f"Current position: {f.tell()}")
    first_part = f.read(5)
    print(f"Read 5 characters: '{first_part}'")
    print(f"Current position: {f.tell()}")
    
    f.seek(0)  # Go back to beginning
    print(f"After seek(0): position = {f.tell()}")
    first_line = f.readline()
    print(f"First line: {first_line.rstrip()}")

# File modes
print("\n--- File Modes ---")
print("File modes:")
print("  'r': Read (default)")
print("  'w': Write (creates or truncates)")
print("  'a': Append (adds to end)")
print("  'x': Exclusive creation (fails if exists)")
print("  'b': Binary mode (combine with others: 'rb', 'wb')")
print("  '+': Read and write (combine: 'r+', 'w+', 'a+')")

# ============================================================================
# 4. EXCEPTION HANDLING
# ============================================================================

print("\n" + "="*70)
print("4. EXCEPTION HANDLING")
print("="*70)

# Basic try-except
print("\n--- Basic Try-Except ---")
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"{a} / {b} = {result}")
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero")
    except TypeError:
        print(f"Error: Invalid operand types for division")

divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(10, "two")

# Multiple exceptions
print("\n--- Multiple Exception Handling ---")
def process_data(data):
    try:
        number = int(data)
        result = 100 / number
        print(f"Result: {result}")
    except ValueError:
        print(f"Error: '{data}' is not a valid integer")
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero")

process_data("42")
process_data("not_a_number")
process_data("0")

# Try-except-else
print("\n--- Try-Except-Else ---")
def calculate_average(scores):
    try:
        average = sum(scores) / len(scores)
    except ZeroDivisionError:
        print("Error: Cannot calculate average of empty list")
    except TypeError:
        print("Error: Invalid data type in scores")
    else:
        print(f"Average: {average:.2f}")

calculate_average([85, 90, 78, 92])
calculate_average([])
calculate_average([85, "ninety"])

# Try-except-finally
print("\n--- Try-Except-Finally ---")
def read_and_process(filename):
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
        print(f"File content length: {len(content)} characters")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    finally:
        if file:
            file.close()
            print("File closed in finally block")

read_and_process(test_file)
read_and_process("nonexistent_file.txt")

# Raising exceptions
print("\n--- Raising Exceptions ---")
def validate_age(age):
    try:
        age = int(age)
        if age < 0:
            raise ValueError("Age cannot be negative")
        if age > 150:
            raise ValueError("Age seems unrealistic")
        print(f"Valid age: {age}")
    except ValueError as e:
        print(f"Error: {e}")

validate_age("25")
validate_age("-5")
validate_age("200")

# Custom exceptions
print("\n--- Custom Exceptions ---")
class InsufficientFundsError(Exception):
    """Raised when account balance is insufficient"""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"Cannot withdraw ${amount}. Balance: ${self.balance}")
        self.balance -= amount
        print(f"Withdrawn: ${amount}. New balance: ${self.balance}")

account = BankAccount(100)
try:
    account.withdraw(50)
    account.withdraw(100)
except InsufficientFundsError as e:
    print(f"Error: {e}")

# Exception hierarchy
print("\n--- Exception Hierarchy ---")
try:
    # Various exceptions
    x = [1, 2, 3]
    print(x[10])  # IndexError
except Exception as e:
    print(f"Caught exception: {type(e).__name__}: {e}")

# ============================================================================
# 5. COMMON EXCEPTION TYPES
# ============================================================================

print("\n" + "="*70)
print("5. COMMON EXCEPTION TYPES")
print("="*70)

print("""
Common Exception Types:
- ValueError: Invalid value for a function
- TypeError: Invalid type for an operation
- IndexError: Index out of range
- KeyError: Key not found in dictionary
- FileNotFoundError: File doesn't exist
- ZeroDivisionError: Division by zero
- AttributeError: Attribute doesn't exist
- NameError: Variable not defined
- RuntimeError: General runtime error
- ImportError: Module import failed
""")

# Demonstrating various exceptions
print("\n--- Exception Type Examples ---")

# ValueError
try:
    int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

# TypeError
try:
    "string" + 5
except TypeError as e:
    print(f"TypeError: {e}")

# IndexError
try:
    lst = [1, 2, 3]
    lst[5]
except IndexError as e:
    print(f"IndexError: {e}")

# KeyError
try:
    d = {'name': 'John'}
    d['age']
except KeyError as e:
    print(f"KeyError: {e}")

# AttributeError
try:
    "hello".nonexistent_method()
except AttributeError as e:
    print(f"AttributeError: {e}")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n" + "="*70)
print("PRACTICE EXERCISES")
print("="*70)

print("""
1. String Manipulation Exercise:
   Create a function that takes a sentence and returns:
   - The sentence in uppercase
   - The sentence in lowercase
   - The sentence with words reversed
   - Word count
   
2. File Processing Exercise:
   Create a function that reads a file and returns:
   - Total number of lines
   - Total number of words
   - Total number of characters
   - Average word length
   
3. Exception Handling Exercise:
   Create a function that reads a CSV file and converts data to integers.
   Handle cases where:
   - File doesn't exist
   - Data is not a valid integer
   - Empty lines exist
   
4. Email Validation Exercise:
   Create a function that validates an email address:
   - Must contain exactly one '@'
   - Must have at least one character before '@'
   - Must have a domain (at least one character after '@')
   - Raise custom InvalidEmailError for invalid emails
   
5. File Encryption Exercise:
   Create functions to:
   - Read a text file
   - Encode it (shift each character by a fixed amount)
   - Write encoded data to a new file
   - Read and decode the file
   - Handle encoding/decoding errors
""")

# Cleanup: Remove test files
print("\n--- Cleaning up test files ---")
for filename in [test_file, test_file_append, test_file_lines]:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Removed {filename}")

print("\n" + "="*70)
print("Module completed successfully!")
print("="*70)
