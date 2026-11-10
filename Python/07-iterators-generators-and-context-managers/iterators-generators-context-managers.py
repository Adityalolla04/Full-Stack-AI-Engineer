"""
Iterators, Generators, and Context Managers - Advanced Iteration

This module covers advanced iteration and resource management in Python:
- Iterators (__iter__, __next__)
- Generator functions (yield)
- Generator expressions
- Lazy evaluation
- Context managers (with statement, __enter__, __exit__)
- Creating custom context managers
- with statement for resource management
"""

import time

# ============================================================================
# 1. ITERATORS AND THE ITERATION PROTOCOL
# ============================================================================

print("\n" + "="*70)
print("1. ITERATORS AND THE ITERATION PROTOCOL")
print("="*70)

print("\n--- Understanding Iterables and Iterators ---")
print("""
Iterable: An object that has __iter__() method
Iterator: An object that has __iter__() and __next__() methods

for loop does:
1. Calls iter() on the iterable (calls __iter__())
2. Gets an iterator object
3. Repeatedly calls next() (calls __next__())
4. Catches StopIteration to end the loop
""")

print("\n--- Using iter() and next() ---")
numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)
print(f"Original list: {numbers}")
print(f"Iterator object: {iterator}")

print("Using next():")
print(f"  next(): {next(iterator)}")
print(f"  next(): {next(iterator)}")
print(f"  next(): {next(iterator)}")

# The rest with a loop
remaining = []
for num in iterator:
    remaining.append(num)
print(f"Remaining: {remaining}")

print("\n--- Custom Iterator Class ---")

class CountUp:
    """Custom iterator that counts from start to end"""
    
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        """Called when iteration starts"""
        return self
    
    def __next__(self):
        """Called for each iteration"""
        if self.current <= self.end:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

print("Counting from 1 to 5:")
counter = CountUp(1, 5)
for num in counter:
    print(f"  {num}")

# ============================================================================
# 2. GENERATOR FUNCTIONS
# ============================================================================

print("\n" + "="*70)
print("2. GENERATOR FUNCTIONS")
print("="*70)

print("\n--- Basic Generator ---")

def simple_generator():
    """A simple generator function using yield"""
    print("  Generator started")
    yield 1
    print("  After first yield")
    yield 2
    print("  After second yield")
    yield 3
    print("  After third yield")

print("Creating generator:")
gen = simple_generator()
print(f"Generator object: {gen}")

print("\nIterating through generator:")
for value in gen:
    print(f"  Received: {value}")

print("\n--- Generator with Return ---")

def countdown(n):
    """Countdown generator with return value"""
    while n > 0:
        yield n
        n -= 1
    return "Countdown complete!"

print("Countdown from 3:")
for num in countdown(3):
    print(f"  {num}")

print("\n--- Fibonacci Generator ---")

def fibonacci(max_count):
    """Generate Fibonacci sequence"""
    a, b = 0, 1
    count = 0
    while count < max_count:
        yield a
        a, b = b, a + b
        count += 1

print("Fibonacci sequence (first 8 numbers):")
for fib in fibonacci(8):
    print(f"  {fib}", end=" ")
print()

print("\n--- Generator with Input (send method) ---")

def echo_generator():
    """Generator that echoes back values received via send()"""
    while True:
        received = yield
        if received is not None:
            print(f"  Received: {received}")

gen = echo_generator()
next(gen)  # Prime the generator
gen.send("Hello")
gen.send("World")
gen.send("Python")

print("\n--- Generator Performance ---")

def large_range(n):
    """Generator version of range"""
    i = 0
    while i < n:
        yield i
        i += 1

print("Comparing list vs generator:")
print(f"list(range(5)): {list(range(5))}")
print(f"gen = large_range(5): created generator object")
print(f"list(gen): {list(large_range(5))}")

# ============================================================================
# 3. GENERATOR EXPRESSIONS
# ============================================================================

print("\n" + "="*70)
print("3. GENERATOR EXPRESSIONS")
print("="*70)

print("\n--- Generator vs List Comprehension ---")

# List comprehension - creates entire list in memory
list_comp = [x**2 for x in range(5)]
print(f"List comprehension: {list_comp}")
print(f"Type: {type(list_comp)}")

# Generator expression - creates one value at a time
gen_expr = (x**2 for x in range(5))
print(f"Generator expression: {gen_expr}")
print(f"Type: {type(gen_expr)}")

print("\nValues from generator expression:")
for value in gen_expr:
    print(f"  {value}")

print("\n--- Generator Expression Syntax ---")

# With filtering
even_squares = (x**2 for x in range(10) if x % 2 == 0)
print(f"Even squares (1-10): {list(even_squares)}")

# With transformation
uppercase = (word.upper() for word in ["hello", "world", "python"])
print(f"Uppercase: {list(uppercase)}")

# ============================================================================
# 4. LAZY EVALUATION
# ============================================================================

print("\n" + "="*70)
print("4. LAZY EVALUATION")
print("="*70)

print("\n--- Lazy vs Eager Evaluation ---")

def print_and_yield(n):
    """Generator that prints when value is yielded"""
    for i in range(n):
        print(f"    Yielding {i}")
        yield i

print("List comprehension (eager - processes all immediately):")
print("Creating list...")
lazy_list = [x for x in print_and_yield(3)]
print(f"List created: {lazy_list}")

print("\nGenerator expression (lazy - processes on demand):")
print("Creating generator...")
lazy_gen = (x for x in print_and_yield(3))
print("Generator created (nothing printed yet)")
print("Iterating:")
result = list(lazy_gen)
print(f"Generator consumed: {result}")

print("\n--- Memory Efficiency ---")

def process_large_file_generator(filename):
    """Simulate reading a large file line by line"""
    print(f"  Generator for {filename} created")
    for i in range(100000):
        yield f"Line {i}: Some data"

print("With generator (memory efficient):")
gen = process_large_file_generator("large_file.txt")
print(f"Generator created: {gen}")
# Only consume what we need
print("First 3 lines:")
for i, line in enumerate(gen):
    if i >= 3:
        break
    print(f"  {line}")

# ============================================================================
# 5. CONTEXT MANAGERS
# ============================================================================

print("\n" + "="*70)
print("5. CONTEXT MANAGERS")
print("="*70)

print("\n--- File Context Manager ---")
print("The 'with' statement automatically handles file closing:")

# Create a test file
with open("context_test.txt", "w") as f:
    f.write("Context manager example\n")
    f.write("Automatic resource management\n")

# Read it back
print("Reading file with context manager:")
with open("context_test.txt", "r") as f:
    content = f.read()
    print(f"Content:\n{content}")

print("File is automatically closed after 'with' block")

print("\n--- Context Manager Protocol ---")
print("""
Context managers use two magic methods:
- __enter__(): Called when entering 'with' block
- __exit__(): Called when exiting 'with' block (even on exception)
""")

print("\n--- Custom Context Manager Class ---")

class Timer:
    """Context manager that measures time"""
    
    def __init__(self, name):
        self.name = name
        self.start_time = None
    
    def __enter__(self):
        """Called when entering with block"""
        self.start_time = time.time()
        print(f"Timer '{self.name}' started")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting with block"""
        elapsed = time.time() - self.start_time
        print(f"Timer '{self.name}' stopped: {elapsed:.4f} seconds")
        return False  # Don't suppress exceptions

print("Using custom Timer context manager:")
with Timer("Loop"):
    total = 0
    for i in range(1000000):
        total += i

print("\n--- Exception Handling in Context Managers ---")

class FileManager:
    """Custom file manager with error handling"""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print(f"Opened {self.filename}")
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Exception occurred: {exc_type.__name__}: {exc_val}")
        self.file.close()
        print(f"Closed {self.filename}")
        return False  # Propagate exceptions

print("Using custom FileManager:")
try:
    with FileManager("context_test.txt", "r") as f:
        print(f"File content preview: {f.readline().strip()}")
except Exception as e:
    print(f"Error: {e}")

# ============================================================================
# 6. GENERATOR-BASED CONTEXT MANAGERS
# ============================================================================

print("\n" + "="*70)
print("6. GENERATOR-BASED CONTEXT MANAGERS")
print("="*70)

from contextlib import contextmanager

print("\n--- Using @contextmanager Decorator ---")

@contextmanager
def simple_timer(name):
    """Context manager using generator"""
    print(f"Starting {name}")
    start = time.time()
    try:
        yield  # This is where the with block code runs
    finally:
        elapsed = time.time() - start
        print(f"Finished {name} ({elapsed:.4f} seconds)")

print("Using generator-based context manager:")
with simple_timer("Data Processing"):
    total = sum(range(100000))
    print(f"  Calculated sum: {total}")

print("\n--- Context Manager with Return Value ---")

@contextmanager
def database_connection(db_name):
    """Simulate database connection"""
    print(f"Connecting to {db_name}")
    connection = {"db": db_name, "status": "connected"}
    try:
        yield connection
    finally:
        connection["status"] = "disconnected"
        print(f"Disconnected from {db_name}")

print("Using database context manager:")
with database_connection("mydb") as conn:
    print(f"  Connection: {conn}")
    print(f"  Running query...")

# ============================================================================
# 7. CHAINING CONTEXT MANAGERS
# ============================================================================

print("\n" + "="*70)
print("7. CHAINING CONTEXT MANAGERS")
print("="*70)

print("\n--- Multiple Context Managers ---")

print("Using multiple 'with' statements:")
with open("file1.txt", "w") as f1:
    with open("file2.txt", "w") as f2:
        f1.write("File 1")
        f2.write("File 2")
        print("  Both files open")

print("\nUsing single 'with' statement (Python 3.1+):")
with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
    f1.write("File 1")
    f2.write("File 2")
    print("  Both files open in single with statement")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n" + "="*70)
print("PRACTICE EXERCISES")
print("="*70)

print("""
1. Custom Iterator - Fibonacci:
   - Create FibonacciIterator class
   - Implement __iter__ and __next__
   - Should produce Fibonacci numbers
   - Test with for loop and next()

2. Generator Functions:
   - Create prime_generator() that yields prime numbers
   - Create file_lines_generator() that reads file line by line
   - Create infinite_counter() that yields numbers infinitely
   - Use generators to process large datasets

3. Generator Expressions:
   - Convert list comprehensions to generator expressions
   - Create generator that filters even numbers
   - Create generator that transforms strings to uppercase
   - Compare memory usage of list vs generator

4. Custom Context Manager:
   - Create DatabaseConnection context manager
   - Implement automatic connection opening/closing
   - Handle connection errors gracefully
   - Support with statement usage
   - Track connection statistics

5. Resource Management:
   - Create context manager for temporary files
   - Create context manager for logging
   - Create context manager that captures exceptions
   - Combine multiple context managers
   - Test exception handling in __exit__
""")

# Cleanup
import os
for f in ["context_test.txt", "file1.txt", "file2.txt"]:
    if os.path.exists(f):
        os.remove(f)

print("\n" + "="*70)
print("Module completed successfully!")
print("="*70)
