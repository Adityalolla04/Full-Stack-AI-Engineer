"""
Decorators and Functional Tools - Advanced Function Programming

This module covers decorators and functional programming patterns in Python:
- Decorator basics and syntax
- Decorators with arguments
- Stacking decorators
- functools module (wraps, lru_cache)
- map, filter, reduce
- zip and enumerate
- Partial functions
- Closures and scope
"""

import functools
from functools import wraps, lru_cache, partial, reduce
import time

# ============================================================================
# 1. CLOSURES AND SCOPE
# ============================================================================

print("\n" + "="*70)
print("1. CLOSURES AND SCOPE")
print("="*70)

print("\n--- Understanding Closures ---")
print("""
A closure is a function that captures variables from its enclosing scope.
The enclosed function has access to variables in the outer function.
""")

def outer_function(x):
    """Outer function that creates a closure"""
    print(f"outer_function called with x={x}")
    
    def inner_function(y):
        """Inner function that captures x from outer scope"""
        print(f"  inner_function called with y={y}")
        return x + y
    
    return inner_function

add_five = outer_function(5)
print(f"Created closure: {add_five}")
print(f"Calling add_five(3): {add_five(3)}")
print(f"Calling add_five(7): {add_five(7)}")

print("\n--- Closure with Mutable State ---")

def create_multiplier(factor):
    """Create a multiplier function with captured factor"""
    def multiply(x):
        return x * factor
    return multiply

times_3 = create_multiplier(3)
times_10 = create_multiplier(10)

print(f"times_3(5): {times_3(5)}")
print(f"times_10(5): {times_10(5)}")

# ============================================================================
# 2. DECORATOR BASICS
# ============================================================================

print("\n" + "="*70)
print("2. DECORATOR BASICS")
print("="*70)

print("\n--- Simple Decorator ---")

def my_decorator(func):
    """A simple decorator that wraps a function"""
    def wrapper():
        print("  Something before the function call")
        result = func()
        print("  Something after the function call")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("  Hello!")
    return "hello"

print("Calling decorated function:")
result = say_hello()
print(f"Return value: {result}")

print("\n--- Decorator Without @ Syntax ---")

def greet():
    print("  Greetings!")

decorated_greet = my_decorator(greet)
print("Calling manually decorated function:")
decorated_greet()

print("\n--- Decorator with Arguments ---")

def my_function_with_args(func):
    """Decorator for functions that take arguments"""
    def wrapper(*args, **kwargs):
        print(f"  Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"  Function returned: {result}")
        return result
    return wrapper

@my_function_with_args
def add(a, b):
    return a + b

@my_function_with_args
def greet_person(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print("Calling decorated functions with arguments:")
add(3, 5)
greet_person("Alice", greeting="Hi")

# ============================================================================
# 3. FUNCTOOLS.WRAPS
# ============================================================================

print("\n" + "="*70)
print("3. FUNCTOOLS.WRAPS")
print("="*70)

print("\n--- Problem: Lost Function Metadata ---")

def bad_decorator(func):
    """Decorator without wraps - loses metadata"""
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def original_function():
    """This is the original function's docstring"""
    pass

print(f"Function name: {original_function.__name__}")
print(f"Function doc: {original_function.__doc__}")

print("\n--- Solution: Using @wraps ---")

def good_decorator(func):
    """Decorator with wraps - preserves metadata"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        return func(*args, **kwargs)
    return wrapper

@good_decorator
def improved_function():
    """This is the improved function's docstring"""
    pass

print(f"Function name: {improved_function.__name__}")
print(f"Function doc: {improved_function.__doc__}")

# ============================================================================
# 4. PRACTICAL DECORATORS
# ============================================================================

print("\n" + "="*70)
print("4. PRACTICAL DECORATORS")
print("="*70)

print("\n--- Timing Decorator ---")

def timer_decorator(func):
    """Decorator that measures execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"  {func.__name__} took {elapsed:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(0.1)
    return "Done!"

print("Calling timed function:")
slow_function()

print("\n--- Validation Decorator ---")

def require_positive(func):
    """Decorator that validates arguments are positive"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Arguments must be positive, got {arg}")
        return func(*args, **kwargs)
    return wrapper

@require_positive
def calculate_square_root(n):
    return n ** 0.5

print("Calling validated function:")
print(f"calculate_square_root(9): {calculate_square_root(9)}")
try:
    calculate_square_root(-9)
except ValueError as e:
    print(f"Error: {e}")

print("\n--- Memoization Decorator ---")

def memoize(func):
    """Decorator that caches function results"""
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
            print(f"  Computed {func.__name__}{args}")
        else:
            print(f"  Retrieved from cache {func.__name__}{args}")
        return cache[args]
    
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("Computing Fibonacci numbers (with memoization):")
print(f"fibonacci(5): {fibonacci(5)}")
print(f"fibonacci(5) again: {fibonacci(5)}")

# ============================================================================
# 5. DECORATORS WITH ARGUMENTS
# ============================================================================

print("\n" + "="*70)
print("5. DECORATORS WITH ARGUMENTS")
print("="*70)

print("\n--- Decorator Factory ---")

def repeat(times):
    """Decorator factory that repeats function execution"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(times=3)
def say_greeting():
    return "Hello!"

print("Using decorator with arguments:")
results = say_greeting()
print(f"Results: {results}")

print("\n--- Decorator with Optional Arguments ---")

def log_calls(prefix="LOG", level="INFO"):
    """Decorator with optional arguments"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{prefix}:{level}] Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_calls(prefix="DEBUG")
def debug_function():
    return "Debugging"

@log_calls()
def info_function():
    return "Info"

print("Calling decorated functions:")
debug_function()
info_function()

# ============================================================================
# 6. STACKING DECORATORS
# ============================================================================

print("\n" + "="*70)
print("6. STACKING DECORATORS")
print("="*70)

print("\n--- Multiple Decorators ---")

def decorator_a(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("  A: Before")
        result = func(*args, **kwargs)
        print("  A: After")
        return result
    return wrapper

def decorator_b(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("    B: Before")
        result = func(*args, **kwargs)
        print("    B: After")
        return result
    return wrapper

@decorator_a
@decorator_b
def stacked_function():
    print("      Function execution")
    return "Done"

print("Calling function with stacked decorators:")
print("Decorators are applied bottom-to-top:")
stacked_function()

# ============================================================================
# 7. FUNCTOOLS.LRU_CACHE
# ============================================================================

print("\n" + "="*70)
print("7. FUNCTOOLS.LRU_CACHE")
print("="*70)

print("\n--- LRU Cache for Performance ---")

@lru_cache(maxsize=32)
def fibonacci_cached(n):
    """Fibonacci with LRU cache"""
    if n < 2:
        return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)

print("Computing Fibonacci with LRU cache:")
start = time.time()
result = fibonacci_cached(30)
elapsed = time.time() - start
print(f"fibonacci_cached(30): {result} ({elapsed:.4f} seconds)")

print(f"Cache info: {fibonacci_cached.cache_info()}")

# Clear cache
fibonacci_cached.cache_clear()
print(f"Cache cleared: {fibonacci_cached.cache_info()}")

# ============================================================================
# 8. MAP, FILTER, REDUCE
# ============================================================================

print("\n" + "="*70)
print("8. MAP, FILTER, REDUCE")
print("="*70)

print("\n--- map() Function ---")
print("map(function, iterable) applies function to each item")

numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(f"Original: {numbers}")
print(f"Squared: {list(squared)}")

# Using function
def double(x):
    return x * 2

doubled = list(map(double, numbers))
print(f"Doubled: {doubled}")

print("\n--- filter() Function ---")
print("filter(function, iterable) keeps items where function returns True")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Numbers: {numbers}")
print(f"Evens: {evens}")

def is_greater_than_5(x):
    return x > 5

greater_than_5 = list(filter(is_greater_than_5, numbers))
print(f"Greater than 5: {greater_than_5}")

print("\n--- reduce() Function ---")
print("reduce(function, iterable) accumulates values")

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"Numbers: {numbers}")
print(f"Product: {product}")

strings = ["Hello", " ", "World"]
concatenated = reduce(lambda x, y: x + y, strings)
print(f"Concatenated: {concatenated}")

# ============================================================================
# 9. ZIP AND ENUMERATE
# ============================================================================

print("\n" + "="*70)
print("9. ZIP AND ENUMERATE")
print("="*70)

print("\n--- zip() Function ---")

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

print("Using zip to combine iterables:")
for name, age, city in zip(names, ages, cities):
    print(f"  {name}: {age} years old, from {city}")

print("\n--- enumerate() Function ---")

fruits = ["apple", "banana", "cherry"]
print("Using enumerate to get index and value:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

print("\nEnumerate with start parameter:")
for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}: {fruit}")

# ============================================================================
# 10. PARTIAL FUNCTIONS
# ============================================================================

print("\n" + "="*70)
print("10. PARTIAL FUNCTIONS")
print("="*70)

print("\n--- Using functools.partial ---")

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print("Original function: power(base, exponent)")
print(f"power(2, 3): {power(2, 3)}")
print(f"power(2, 8): {power(2, 8)}")

print("\nUsing partial:")
print(f"square(5): {square(5)}")
print(f"cube(3): {cube(3)}")

print("\n--- Practical Example ---")

from functools import partial

def multiply(x, y):
    return x * y

times_three = partial(multiply, 3)
print(f"times_three(10): {times_three(10)}")

# Using with map
numbers = [1, 2, 3, 4, 5]
tripled = list(map(times_three, numbers))
print(f"Triple each number: {tripled}")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n" + "="*70)
print("PRACTICE EXERCISES")
print("="*70)

print("""
1. Decorator for Function Caching:
   - Create a caching decorator similar to lru_cache
   - Allow custom cache size
   - Implement cache statistics
   - Use with recursive functions

2. Decorator for Rate Limiting:
   - Create a decorator that limits function calls per second
   - Track call times
   - Raise exception or wait if limit exceeded
   - Use with API-like functions

3. Chaining Decorators:
   - Create decorators for logging, timing, and validation
   - Stack them on a single function
   - Show execution order
   - Test with different stacking orders

4. Functional Programming Exercise:
   - Use map to convert list of temperatures
   - Use filter to find values meeting criteria
   - Use reduce to calculate statistics
   - Combine with lambda functions

5. Custom Partial Functions:
   - Create specialized functions using partial
   - Apply to mathematical operations
   - Use with higher-order functions
   - Compare with lambda functions
""")

print("\n" + "="*70)
print("Module completed successfully!")
print("="*70)
