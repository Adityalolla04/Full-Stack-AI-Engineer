"""
Control Flow and Functions

This module covers how Python executes code conditionally and how to organize code with functions:
- if, elif, else statements
- for and while loops
- break, continue, and else with loops
- Function definition, parameters, return values
- Scope and variable lifetime
- *args and **kwargs
- Lambda functions and default parameters
"""

# ============================================================================
# 1. IF, ELIF, ELSE STATEMENTS
# ============================================================================

print("\n" + "="*70)
print("1. CONDITIONAL STATEMENTS - if, elif, else")
print("="*70)

# Simple if statement
print("\n--- Simple if Statement ---")
age = 18
if age >= 18:
    print(f"{age} years old - You are an adult")

# if-else statement
print("\n--- if-else Statement ---")
temperature = 15
if temperature > 20:
    print("It's warm")
else:
    print("It's cold")

# if-elif-else statement
print("\n--- if-elif-else Statement ---")
score = 75
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Score: {score}, Grade: {grade}")

# Nested if statements
print("\n--- Nested if Statements ---")
user_age = 25
has_license = True
if user_age >= 18:
    if has_license:
        print("You can drive a car")
    else:
        print("Get a driver's license first")
else:
    print("You are too young to drive")

# Ternary operator (conditional expression)
print("\n--- Ternary Operator ---")
age = 16
status = "adult" if age >= 18 else "minor"
print(f"Age {age}: {status}")

# Multiple conditions
print("\n--- Multiple Conditions ---")
x, y = 10, 5
if x > 0 and y > 0:
    print(f"Both {x} and {y} are positive")

if x > 0 or y < 0:
    print(f"Either {x} is positive or {y} is negative")

if not (x == 0):
    print(f"{x} is not zero")


# ============================================================================
# 2. FOR LOOPS
# ============================================================================

print("\n" + "="*70)
print("2. FOR LOOPS")
print("="*70)

# Basic for loop with range
print("\n--- Basic for Loop with range() ---")
for i in range(5):
    print(f"Iteration {i}")

# Range with start, stop, step
print("\n--- range() with Start, Stop, Step ---")
print("range(1, 6):", list(range(1, 6)))
print("range(0, 10, 2):", list(range(0, 10, 2)))
print("range(10, 0, -1):", list(range(10, 0, -1)))

# Loop over strings
print("\n--- Loop over String ---")
text = "Python"
for char in text:
    print(f"  {char}", end=" ")
print()

# Loop over list
print("\n--- Loop over List ---")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"  {fruit}")

# Loop over dictionary
print("\n--- Loop over Dictionary ---")
person = {"name": "Alice", "age": 25, "city": "NYC"}
for key, value in person.items():
    print(f"  {key}: {value}")

# Enumerate for index and value
print("\n--- Using enumerate() ---")
items = ["a", "b", "c"]
for index, value in enumerate(items):
    print(f"  Index {index}: {value}")

# Nested loops
print("\n--- Nested Loops ---")
print("Multiplication table (2x3 to 3x3):")
for i in range(2, 4):
    for j in range(3, 4):
        print(f"  {i} × {j} = {i*j}")

# For-else construct
print("\n--- for-else Construct ---")
for i in range(3):
    print(f"  Loop iteration {i}")
else:
    print("  Loop completed normally")


# ============================================================================
# 3. WHILE LOOPS
# ============================================================================

print("\n" + "="*70)
print("3. WHILE LOOPS")
print("="*70)

# Basic while loop
print("\n--- Basic while Loop ---")
counter = 0
while counter < 3:
    print(f"  Counter: {counter}")
    counter += 1

# While with condition
print("\n--- while Loop with Condition ---")
num = 5
while num > 0:
    print(f"  Countdown: {num}")
    num -= 1

# While-else construct
print("\n--- while-else Construct ---")
x = 0
while x < 3:
    print(f"  x = {x}")
    x += 1
else:
    print("  while condition became False, else executed")

# Infinite loop with break
print("\n--- Infinite Loop with Break ---")
count = 0
while True:
    if count == 2:
        print("  Breaking out of loop")
        break
    print(f"  Count: {count}")
    count += 1


# ============================================================================
# 4. BREAK AND CONTINUE
# ============================================================================

print("\n" + "="*70)
print("4. BREAK AND CONTINUE STATEMENTS")
print("="*70)

# break statement
print("\n--- break Statement ---")
for i in range(10):
    if i == 5:
        print(f"  Found 5, breaking loop")
        break
    print(f"  {i}")

# continue statement
print("\n--- continue Statement ---")
for i in range(5):
    if i == 2:
        print(f"  Skipping {i}")
        continue
    print(f"  {i}")

# Break in nested loop
print("\n--- break in Nested Loop ---")
found = False
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            print(f"  Found at ({i}, {j})")
            found = True
            break
    if found:
        break


# ============================================================================
# 5. FUNCTION DEFINITION AND CALLING
# ============================================================================

print("\n" + "="*70)
print("5. FUNCTION DEFINITION AND CALLING")
print("="*70)

# Simple function
print("\n--- Simple Function ---")

def greet():
    """A simple greeting function."""
    print("  Hello, World!")

greet()

# Function with parameters
print("\n--- Function with Parameters ---")

def greet_person(name):
    """Greet a specific person."""
    print(f"  Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

# Function with return value
print("\n--- Function with Return Value ---")

def add(a, b):
    """Add two numbers and return result."""
    return a + b

result = add(5, 3)
print(f"  add(5, 3) = {result}")

# Function with multiple return values
print("\n--- Multiple Return Values ---")

def get_min_max(numbers):
    """Return both minimum and maximum values."""
    return min(numbers), max(numbers)

nums = [3, 1, 4, 1, 5, 9]
minimum, maximum = get_min_max(nums)
print(f"  Numbers: {nums}")
print(f"  Min: {minimum}, Max: {maximum}")

# Function with default parameters
print("\n--- Default Parameters ---")

def introduce(name, age=25, city="Unknown"):
    """Introduce a person with optional parameters."""
    print(f"  Name: {name}, Age: {age}, City: {city}")

introduce("Alice")
introduce("Bob", 30)
introduce("Charlie", 28, "NYC")

# Keyword arguments
print("\n--- Keyword Arguments ---")
introduce(name="Diana", city="LA", age=26)
introduce("Eve", city="Boston")

# Function with *args
print("\n--- *args for Variable Arguments ---")

def sum_all(*args):
    """Sum all provided arguments."""
    total = sum(args)
    return total

print(f"  sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"  sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")

# Function with **kwargs
print("\n--- **kwargs for Named Arguments ---")

def print_info(**kwargs):
    """Print key-value pairs."""
    for key, value in kwargs.items():
        print(f"    {key}: {value}")

print("  Calling print_info(name='Alice', age=25, city='NYC'):")
print_info(name='Alice', age=25, city='NYC')

# Combining positional, *args, and **kwargs
print("\n--- Combining All Parameter Types ---")

def full_function(pos, *args, **kwargs):
    """Function with all parameter types."""
    print(f"  Positional: {pos}")
    print(f"  *args: {args}")
    print(f"  **kwargs: {kwargs}")

full_function(1, 2, 3, 4, name='Alice', age=25)


# ============================================================================
# 6. SCOPE AND VARIABLE LIFETIME
# ============================================================================

print("\n" + "="*70)
print("6. SCOPE AND VARIABLE LIFETIME")
print("="*70)

# Global variable
print("\n--- Global Variable ---")
global_var = "I am global"

def show_global():
    print(f"  Inside function: {global_var}")

print(f"  Outside function: {global_var}")
show_global()

# Local variable
print("\n--- Local Variable ---")

def local_scope():
    local_var = "I am local"
    print(f"  Inside function: {local_var}")

local_scope()
# print(local_var)  # This would cause NameError

# Global keyword
print("\n--- global Keyword ---")
counter = 0

def increment():
    global counter
    counter += 1
    print(f"  Counter inside function: {counter}")

print(f"  Counter before: {counter}")
increment()
print(f"  Counter after: {counter}")

# Function-level scope
print("\n--- Function-Level Scope ---")

def outer():
    x = "outer"
    
    def inner():
        x = "inner"  # Local to inner()
        print(f"    inner x: {x}")
    
    inner()
    print(f"  outer x: {x}")

outer()

# Nonlocal keyword
print("\n--- nonlocal Keyword ---")

def outer_func():
    x = "outer"
    
    def inner_func():
        nonlocal x
        x = "modified"
        print(f"    inner: {x}")
    
    inner_func()
    print(f"  outer: {x}")

outer_func()


# ============================================================================
# 7. LAMBDA FUNCTIONS
# ============================================================================

print("\n" + "="*70)
print("7. LAMBDA FUNCTIONS (Anonymous Functions)")
print("="*70)

# Basic lambda
print("\n--- Basic Lambda ---")
square = lambda x: x ** 2
print(f"  lambda x: x**2 applied to 5: {square(5)}")

# Lambda with multiple parameters
print("\n--- Lambda with Multiple Parameters ---")
add = lambda x, y: x + y
print(f"  lambda x, y: x+y applied to (3, 5): {add(3, 5)}")

# Lambda with map()
print("\n--- Lambda with map() ---")
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"  Original: {numbers}")
print(f"  Squared: {squared}")

# Lambda with filter()
print("\n--- Lambda with filter() ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"  Original: {numbers}")
print(f"  Evens: {evens}")

# Lambda with sorted()
print("\n--- Lambda with sorted() ---")
people = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
sorted_by_age = sorted(people, key=lambda x: x[1])
print(f"  Original: {people}")
print(f"  Sorted by age: {sorted_by_age}")


# ============================================================================
# 8. HIGHER-ORDER FUNCTIONS
# ============================================================================

print("\n" + "="*70)
print("8. HIGHER-ORDER FUNCTIONS")
print("="*70)

# Function that takes function as parameter
print("\n--- Function Taking Function as Parameter ---")

def apply_operation(a, b, operation):
    """Apply operation to a and b."""
    return operation(a, b)

print(f"  apply_operation(10, 5, lambda x, y: x + y) = {apply_operation(10, 5, lambda x, y: x + y)}")
print(f"  apply_operation(10, 5, lambda x, y: x - y) = {apply_operation(10, 5, lambda x, y: x - y)}")
print(f"  apply_operation(10, 5, lambda x, y: x * y) = {apply_operation(10, 5, lambda x, y: x * y)}")

# Function that returns function
print("\n--- Function Returning Function ---")

def multiplier(factor):
    """Return a function that multiplies by factor."""
    def multiply(x):
        return x * factor
    return multiply

double = multiplier(2)
triple = multiplier(3)
print(f"  double(5) = {double(5)}")
print(f"  triple(5) = {triple(5)}")


# ============================================================================
# 9. RECURSION
# ============================================================================

print("\n" + "="*70)
print("9. RECURSION")
print("="*70)

# Simple recursion - factorial
print("\n--- Factorial (Recursion) ---")

def factorial(n):
    """Calculate factorial using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"  factorial(5) = {factorial(5)}")
print(f"  factorial(10) = {factorial(10)}")

# Fibonacci recursion
print("\n--- Fibonacci (Recursion) ---")

def fibonacci(n):
    """Calculate nth Fibonacci number using recursion."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"  fibonacci(6) = {fibonacci(6)}")
print(f"  fibonacci(10) = {fibonacci(10)}")

# Recursion with memoization (optimization)
print("\n--- Fibonacci with Memoization ---")

def fibonacci_memo(n, memo={}):
    """Calculate Fibonacci with memoization for efficiency."""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

print(f"  fibonacci_memo(20) = {fibonacci_memo(20)}")


# ============================================================================
# 10. DECORATORS INTRODUCTION
# ============================================================================

print("\n" + "="*70)
print("10. DECORATORS INTRODUCTION")
print("="*70)

# Simple decorator
print("\n--- Simple Decorator ---")

def my_decorator(func):
    """A simple decorator that wraps a function."""
    def wrapper(*args, **kwargs):
        print(f"  Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"  {func.__name__} finished")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"    Hello, {name}!")
    return "said hello"

say_hello("Alice")


# ============================================================================
# 11. PRACTICE EXERCISES
# ============================================================================

print("\n" + "="*70)
print("11. PRACTICE EXERCISES")
print("="*70)

# Exercise 1: FizzBuzz
print("\n--- Exercise 1: FizzBuzz ---")

def fizzbuzz(n):
    """Classic FizzBuzz problem."""
    for i in range(1, n + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        print(f"  {output if output else i}", end=" ")
    print()

fizzbuzz(15)

# Exercise 2: Prime number checker
print("\n--- Exercise 2: Prime Number Checker ---")

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [n for n in range(20) if is_prime(n)]
print(f"  Primes less than 20: {primes}")

# Exercise 3: List processing
print("\n--- Exercise 3: List Processing ---")

def process_list(numbers):
    """Filter, transform, and sort list."""
    # Filter even numbers
    evens = [n for n in numbers if n % 2 == 0]
    # Square them
    squared = [n ** 2 for n in evens]
    # Sort descending
    sorted_desc = sorted(squared, reverse=True)
    return sorted_desc

result = process_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"  Result: {result}")

# Exercise 4: String manipulation
print("\n--- Exercise 4: String Manipulation ---")

def reverse_string(s):
    """Reverse a string recursively."""
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

test_str = "Python"
print(f"  Original: {test_str}")
print(f"  Reversed: {reverse_string(test_str)}")

# Exercise 5: Function composition
print("\n--- Exercise 5: Function Composition ---")

def compose(f, g):
    """Compose two functions."""
    return lambda x: f(g(x))

double = lambda x: x * 2
add_one = lambda x: x + 1

f = compose(double, add_one)  # (x + 1) * 2
print(f"  compose(double, add_one)(5) = {f(5)}")  # (5+1)*2 = 12

print("\n" + "="*70)
print("END OF CONTROL FLOW AND FUNCTIONS")
print("="*70)
