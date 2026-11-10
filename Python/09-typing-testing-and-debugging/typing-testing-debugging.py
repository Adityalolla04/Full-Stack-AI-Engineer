"""
Typing, Testing, and Debugging - Code Quality and Maintenance

This module covers type hints, testing strategies, and debugging techniques:
- Type hints and annotations
- Type checking with mypy concept
- pytest basics and assertions
- Test organization
- Debugging with print and pdb
- Logging basics
- Error handling and debugging
"""

import logging
import sys
from typing import List, Dict, Optional, Union, Tuple, Callable
from unittest import TestCase, main

# ============================================================================
# 1. TYPE HINTS AND ANNOTATIONS
# ============================================================================

print("\n" + "="*70)
print("1. TYPE HINTS AND ANNOTATIONS")
print("="*70)

print("\n--- Basic Type Hints ---")

def greet(name: str) -> str:
    """Function with type hints"""
    return f"Hello, {name}!"

result: str = greet("Alice")
print(f"greet('Alice'): {result}")
print(f"Function annotations: {greet.__annotations__}")

print("\n--- Type Hints with Built-in Types ---")

def add(a: int, b: int) -> int:
    """Add two integers"""
    return a + b

def concatenate(s1: str, s2: str) -> str:
    """Concatenate strings"""
    return s1 + s2

def divide(a: float, b: float) -> float:
    """Divide two floats"""
    return a / b

print(f"add(5, 3): {add(5, 3)}")
print(f"concatenate('Hello', ' World'): {concatenate('Hello', ' World')}")
print(f"divide(10, 3): {divide(10, 3)}")

print("\n--- Collection Type Hints ---")

def process_numbers(numbers: List[int]) -> int:
    """Process a list of integers"""
    return sum(numbers)

def get_person_info(person: Dict[str, Union[str, int]]) -> str:
    """Get person info from dictionary"""
    return f"{person['name']}, age {person['age']}"

def pair_sum(pair: Tuple[int, int]) -> int:
    """Sum a tuple of two integers"""
    return pair[0] + pair[1]

print(f"process_numbers([1, 2, 3, 4]): {process_numbers([1, 2, 3, 4])}")

person: Dict[str, Union[str, int]] = {"name": "Alice", "age": 30}
print(f"get_person_info(person): {get_person_info(person)}")
print(f"pair_sum((3, 4)): {pair_sum((3, 4))}")

print("\n--- Optional Type Hints ---")

def find_user(user_id: int) -> Optional[str]:
    """Find user by ID, returning name or None"""
    users = {1: "Alice", 2: "Bob", 3: "Charlie"}
    return users.get(user_id)

found_user = find_user(2)
print(f"find_user(2): {found_user}")
print(f"find_user(999): {find_user(999)}")

print("\n--- Callable Type Hints ---")

def apply_function(func: Callable[[int], int], value: int) -> int:
    """Apply a function to a value"""
    return func(value)

def square(x: int) -> int:
    return x ** 2

print(f"apply_function(square, 5): {apply_function(square, 5)}")

print("\n--- Complex Type Hints ---")

def process_data(data: Dict[str, List[int]]) -> Dict[str, float]:
    """Process data dictionary and return averages"""
    result: Dict[str, float] = {}
    for key, values in data.items():
        result[key] = sum(values) / len(values)
    return result

test_data: Dict[str, List[int]] = {
    "scores1": [85, 90, 78],
    "scores2": [92, 88, 95]
}
averages = process_data(test_data)
print(f"Averages: {averages}")

# ============================================================================
# 2. TYPE CHECKING WITH MYPY
# ============================================================================

print("\n" + "="*70)
print("2. TYPE CHECKING WITH MYPY")
print("="*70)

print("""
mypy is a static type checker for Python.

Installation:
  pip install mypy

Usage:
  mypy filename.py           # Check file
  mypy .                     # Check entire project
  mypy --strict filename.py  # Strict checking

Type checking can catch errors before runtime:
- Type mismatches
- Missing attributes
- None type errors
- Argument count errors

Example issues mypy can catch:
  def add(a: int, b: int) -> int:
      return a + b
  
  result = add("5", "3")  # mypy error: str not compatible with int
  result2: str = add(5, 3)  # mypy error: int not compatible with str
""")

print("\n--- Type Comments (Pre-3.5) ---")
print("""
Before Python 3.5, type hints were in comments:
  
  def add(a, b):
      # type: (int, int) -> int
      return a + b
  
Modern way (Python 3.5+):
  
  def add(a: int, b: int) -> int:
      return a + b
""")

# ============================================================================
# 3. TESTING BASICS WITH PYTEST
# ============================================================================

print("\n" + "="*70)
print("3. TESTING BASICS WITH PYTEST")
print("="*70)

print("""
pytest is a testing framework for Python.

Installation:
  pip install pytest

Running tests:
  pytest                     # Run all tests
  pytest test_file.py        # Run specific file
  pytest test_file.py::test_function  # Run specific test
  pytest -v                  # Verbose output
  pytest -s                  # Show print statements

Test file structure:
  # test_module.py
  
  def test_add():
      assert add(2, 3) == 5
  
  def test_divide_by_zero():
      with pytest.raises(ZeroDivisionError):
          divide(5, 0)

Test patterns:
  - Arrange: Setup test data
  - Act: Execute function
  - Assert: Check results
""")

print("\n--- Simple Test Examples ---")

# Functions to test
def add_numbers(a: int, b: int) -> int:
    return a + b

def multiply_numbers(a: int, b: int) -> int:
    return a * b

def is_even(n: int) -> bool:
    return n % 2 == 0

def reverse_string(s: str) -> str:
    return s[::-1]

# Test demonstrations (without pytest runner)
print("Test demonstrations (manual assertions):")
assert add_numbers(2, 3) == 5, "add_numbers test failed"
print("✓ add_numbers(2, 3) == 5")

assert multiply_numbers(3, 4) == 12, "multiply_numbers test failed"
print("✓ multiply_numbers(3, 4) == 12")

assert is_even(4) == True, "is_even(4) test failed"
print("✓ is_even(4) == True")

assert is_even(5) == False, "is_even(5) test failed"
print("✓ is_even(5) == False")

assert reverse_string("hello") == "olleh", "reverse_string test failed"
print("✓ reverse_string('hello') == 'olleh'")

# ============================================================================
# 4. DEBUGGING WITH PRINT AND PDB
# ============================================================================

print("\n" + "="*70)
print("4. DEBUGGING WITH PRINT AND PDB")
print("="*70)

print("\n--- Debug Printing ---")

def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate discounted price with debug printing"""
    print(f"[DEBUG] Input: price={price}, discount_percent={discount_percent}")
    
    discount_amount = price * (discount_percent / 100)
    print(f"[DEBUG] Discount amount: {discount_amount}")
    
    final_price = price - discount_amount
    print(f"[DEBUG] Final price: {final_price}")
    
    return final_price

print("Testing calculate_discount:")
result = calculate_discount(100, 20)
print(f"Result: ${result}\n")

print("\n--- Using Python Debugger (pdb) ---")
print("""
pdb is Python's built-in debugger.

Using pdb:

Method 1: Set breakpoint in code
  import pdb
  pdb.set_trace()

Method 2: Use breakpoint() (Python 3.7+)
  breakpoint()

Method 3: Run script with debugger
  python -m pdb script.py

Common pdb commands:
  l or list      - List source code
  n or next      - Execute next line
  s or step      - Step into function
  c or continue  - Continue execution
  p variable     - Print variable value
  pp locals()    - Pretty-print local variables
  h or help      - Show help
  q or quit      - Quit debugger

Example:
  def buggy_function(x):
      result = x * 2
      breakpoint()  # Debugger stops here
      result += 10
      return result
""")

# ============================================================================
# 5. LOGGING BASICS
# ============================================================================

print("\n" + "="*70)
print("5. LOGGING BASICS")
print("="*70)

print("\n--- Logging Levels ---")
print("""
Logging levels (from least to most severe):
  DEBUG (10): Detailed info for debugging
  INFO (20): Confirmations that things work
  WARNING (30): Warning messages for potential issues
  ERROR (40): Error messages for problems
  CRITICAL (50): Critical messages for serious errors
""")

print("\n--- Basic Logging Setup ---")

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

print("Testing logging levels:")
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")

print("\n--- Logging in Functions ---")

def risky_operation(value: int) -> int:
    """Function with logging"""
    logger.info(f"Starting risky_operation with value={value}")
    
    if value < 0:
        logger.warning(f"Negative value provided: {value}")
        return 0
    
    try:
        result = 100 / value
        logger.debug(f"Calculation result: {result}")
        return int(result)
    except ZeroDivisionError:
        logger.error("Division by zero attempted")
        return -1

print("Testing logged function:")
print(f"risky_operation(5): {risky_operation(5)}")
print(f"risky_operation(-5): {risky_operation(-5)}")
print(f"risky_operation(0): {risky_operation(0)}")

# ============================================================================
# 6. ASSERTION AND ERROR HANDLING
# ============================================================================

print("\n" + "="*70)
print("6. ASSERTION AND ERROR HANDLING")
print("="*70)

print("\n--- Using Assertions ---")

def validate_age(age: int) -> bool:
    """Validate age using assertions"""
    assert age >= 0, "Age cannot be negative"
    assert age <= 150, "Age cannot exceed 150"
    assert isinstance(age, int), "Age must be an integer"
    return True

print("Testing assertions:")
try:
    validate_age(30)
    print("✓ validate_age(30) passed")
except AssertionError as e:
    print(f"✗ Assertion failed: {e}")

try:
    validate_age(-5)
except AssertionError as e:
    print(f"✗ Assertion caught: {e}")

print("\n--- Debugging with Exceptions ---")

def process_list(items: List[int]) -> float:
    """Process list with debugging"""
    logger.info(f"Processing list with {len(items)} items")
    
    if not items:
        raise ValueError("List cannot be empty")
    
    try:
        average = sum(items) / len(items)
        logger.info(f"Average calculated: {average}")
        return average
    except TypeError as e:
        logger.error(f"Type error processing list: {e}")
        raise

print("Testing process_list:")
try:
    result = process_list([1, 2, 3, 4, 5])
    print(f"Average: {result}")
except Exception as e:
    print(f"Error: {e}")

# ============================================================================
# 7. TEST ORGANIZATION
# ============================================================================

print("\n" + "="*70)
print("7. TEST ORGANIZATION")
print("="*70)

print("""
Test Project Structure:

project/
├── src/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
├── tests/
│   ├── __init__.py
│   ├── test_module1.py
│   ├── test_module2.py
│   └── fixtures/
│       └── sample_data.py
├── pytest.ini
└── setup.py

conftest.py file:
- Shared fixtures and configuration
- Available to all tests
- Automatically discovered by pytest

Fixture example:
  @pytest.fixture
  def sample_data():
      return {"key": "value"}
  
  def test_something(sample_data):
      assert sample_data["key"] == "value"

Test naming conventions:
- Test files: test_*.py or *_test.py
- Test functions: test_*
- Test classes: Test*
""")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n" + "="*70)
print("PRACTICE EXERCISES")
print("="*70)

print("""
1. Type Hints Exercise:
   - Add type hints to existing functions
   - Use Optional for nullable returns
   - Use Union for multiple types
   - Create custom types using TypeVar
   - Annotate class methods and properties

2. Writing Tests:
   - Write test functions for calculator operations
   - Test edge cases and error conditions
   - Use assertions for validation
   - Test exception raising
   - Organize tests in classes

3. Debugging Exercise:
   - Write a buggy function
   - Add debug print statements
   - Use assertions to catch errors
   - Document debugging process
   - Show how pdb would be used

4. Logging Implementation:
   - Setup logging configuration
   - Add logging to existing functions
   - Use different log levels appropriately
   - Create custom logger instances
   - Log to both console and file

5. Comprehensive Testing Suite:
   - Create a module with multiple functions
   - Write comprehensive test suite
   - Include positive and negative tests
   - Test error handling
   - Test edge cases
   - Add logging to track test execution
""")

print("\n" + "="*70)
print("Module completed successfully!")
print("="*70)
