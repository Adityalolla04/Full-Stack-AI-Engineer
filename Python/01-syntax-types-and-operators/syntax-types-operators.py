"""
Syntax, Types, and Operators - Python Fundamentals

This module covers the foundations of Python programming:
- Numeric types (int, float, complex)
- String types and operations
- Boolean logic and None
- Operators (arithmetic, comparison, logical, identity, membership)
- Type conversion and checking
- Mutability and identity
"""

# ============================================================================
# 1. NUMERIC TYPES - int, float, complex
# ============================================================================

print("\n" + "="*70)
print("1. NUMERIC TYPES")
print("="*70)

# Integer type
print("\n--- Integer Type ---")
integer_num = 42
print(f"Value: {integer_num}, Type: {type(integer_num)}")
print(f"Operations: 5 + 3 = {5 + 3}")
print(f"Operations: 10 - 4 = {10 - 4}")
print(f"Operations: 7 * 6 = {7 * 6}")
print(f"Operations: 20 / 4 = {20 / 4}")
print(f"Integer division: 20 // 3 = {20 // 3}")
print(f"Modulo: 20 % 3 = {20 % 3}")
print(f"Power: 2 ** 8 = {2 ** 8}")

# Float type
print("\n--- Float Type ---")
float_num = 3.14
print(f"Value: {float_num}, Type: {type(float_num)}")
print(f"Decimal operations: 3.5 + 2.5 = {3.5 + 2.5}")
print(f"Mixed arithmetic: 5 + 2.5 = {5 + 2.5}, Result type: {type(5 + 2.5)}")

# Temperature conversion example
degree_celsius_1 = 26.0
fahrenheit_1 = 9 / 5 * degree_celsius_1 + 32
print(f"\nTemperature conversion: {degree_celsius_1}°C = {fahrenheit_1}°F")

degree_celsius_2 = 35.0
fahrenheit_2 = 9 / 5 * degree_celsius_2 + 32
print(f"Temperature conversion: {degree_celsius_2}°C = {fahrenheit_2}°F")

# Complex type
print("\n--- Complex Type ---")
complex_num = 3 + 4j
print(f"Value: {complex_num}, Type: {type(complex_num)}")
print(f"Real part: {complex_num.real}, Imaginary part: {complex_num.imag}")
print(f"Conjugate: {complex_num.conjugate()}")


# ============================================================================
# 2. STRING TYPES AND OPERATIONS
# ============================================================================

print("\n" + "="*70)
print("2. STRING TYPES AND OPERATIONS")
print("="*70)

# String basics
print("\n--- String Basics ---")
single_quote = 'Aditya'
double_quote = "Karthik"
triple_quote = """Multi-line
string example
in Python"""

print(f"Single quoted: {single_quote}, Type: {type(single_quote)}")
print(f"Double quoted: {double_quote}, Type: {type(double_quote)}")
print(f"Triple quoted (multi-line):\n{triple_quote}")

# String operations
print("\n--- String Operations ---")
str1 = "Hello"
str2 = "World"
concatenated = str1 + " " + str2
print(f"Concatenation: '{str1}' + ' ' + '{str2}' = '{concatenated}'")

repeated = "Ha" * 3
print(f"Repetition: 'Ha' * 3 = '{repeated}'")

# String indexing and slicing
print("\n--- String Indexing and Slicing ---")
text = "Python"
print(f"String: {text}")
print(f"First character (index 0): {text[0]}")
print(f"Last character (index -1): {text[-1]}")
print(f"Slice [1:4]: {text[1:4]}")
print(f"Slice [:3]: {text[:3]}")
print(f"Slice [2:]: {text[2:]}")

# String methods
print("\n--- String Methods ---")
test_str = "  Python Programming  "
print(f"Original: '{test_str}'")
print(f"Uppercase: '{test_str.upper()}'")
print(f"Lowercase: '{test_str.lower()}'")
print(f"Strip whitespace: '{test_str.strip()}'")
print(f"Replace 'Python' with 'Java': '{test_str.replace('Python', 'Java')}'")
print(f"Split by space: {test_str.split()}")

# String formatting
print("\n--- String Formatting ---")
name = "Alice"
age = 25
height = 5.6

# f-string (modern)
print(f"f-string: {name} is {age} years old and {height}m tall")

# format method
print("format(): {} is {} years old and {}m tall".format(name, age, height))

# % formatting
print("String formatting: %s is %d years old" % (name, age))


# ============================================================================
# 3. BOOLEAN TYPE AND TRUTHINESS
# ============================================================================

print("\n" + "="*70)
print("3. BOOLEAN TYPE AND TRUTHINESS")
print("="*70)

# Boolean values
print("\n--- Boolean Basics ---")
true_val = True
false_val = False
print(f"True: {true_val}, Type: {type(true_val)}")
print(f"False: {false_val}, Type: {type(false_val)}")

# Boolean operations
print("\n--- Boolean Operations ---")
x, y = 5, 10
print(f"x = {x}, y = {y}")
print(f"x < y: {x < y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x > y: {x > y}")
print(f"x <= y: {x <= y}")
print(f"x >= y: {x >= y}")

# Logical operators
print("\n--- Logical Operators ---")
a, b = True, False
print(f"a = {a}, b = {b}")
print(f"a and b: {a and b}")
print(f"a or b: {a or b}")
print(f"not a: {not a}")
print(f"(a and b) or (not b): {(a and b) or (not b)}")

# Truthiness - values that evaluate to True/False
print("\n--- Truthiness of Values ---")
print(f"bool(0): {bool(0)} (False)")
print(f"bool(1): {bool(1)} (True)")
print(f"bool(''): {bool('')} (False - empty string)")
print(f"bool('text'): {bool('text')} (True - non-empty string)")
print(f"bool([]): {bool([])} (False - empty list)")
print(f"bool([1, 2]): {bool([1, 2])} (True - non-empty list)")
print(f"bool(None): {bool(None)} (False - None)")


# ============================================================================
# 4. NONE TYPE
# ============================================================================

print("\n" + "="*70)
print("4. NONE TYPE")
print("="*70)

print("\n--- None Type ---")
nothing = None
print(f"Value: {nothing}, Type: {type(nothing)}")
print(f"bool(None): {bool(nothing)}")

def function_without_return():
    x = 10
    # No explicit return

result = function_without_return()
print(f"\nFunction with no return statement returns: {result}, Type: {type(result)}")


# ============================================================================
# 5. COMPARISON OPERATORS
# ============================================================================

print("\n" + "="*70)
print("5. COMPARISON OPERATORS")
print("="*70)

day_temp = 3
night_temp = 10
temp_diff = abs(day_temp - night_temp)

print(f"\nDay temperature: {day_temp}°C")
print(f"Night temperature: {night_temp}°C")
print(f"Absolute difference: |{day_temp} - {night_temp}| = {temp_diff}")

# Comparison examples
print("\n--- Comparisons ---")
print(f"9 - 3 = {9 - 3}")
print(f"abs(-7) = {abs(-7)}")
print(f"abs(-7) + abs(3.3) = {abs(-7) + abs(3.3)}")


# ============================================================================
# 6. BUILT-IN FUNCTIONS FOR NUMERIC OPERATIONS
# ============================================================================

print("\n" + "="*70)
print("6. BUILT-IN FUNCTIONS")
print("="*70)

# round() function
print("\n--- round() Function ---")
print(f"round(3.8) = {round(3.8)}")
print(f"round(3.3) = {round(3.3)}")
print(f"round(3.5) = {round(3.5)}")
print(f"round(4.5) = {round(4.5)}")
print(f"round(3.141592653, 2) = {round(3.141592653, 2)}")
print("Note: Python uses 'banker\'s rounding' (round to nearest even)")

# math module functions
print("\n--- math Module Functions ---")
import math
print(f"math.ceil(3.2) = {math.ceil(3.2)}")
print(f"math.floor(3.9) = {math.floor(3.9)}")
print(f"math.sqrt(16) = {math.sqrt(16)}")

# abs() function
print("\n--- abs() Function ---")
print(f"abs(-7) = {abs(-7)}")
print(f"abs(7) = {abs(7)}")
print(f"abs(-3.5) = {abs(-3.5)}")

# min() and max()
print("\n--- min() and max() Functions ---")
print(f"min(2, 3, 4) = {min(2, 3, 4)}")
print(f"max(2, 3, 4) = {max(2, 3, 4)}")
print(f"max(2, -3, min(4, 7), -5) = {max(2, -3, min(4, 7), -5)}")

# pow() function
print("\n--- pow() Function ---")
print(f"pow(4, 4) = {pow(4, 4)}")
print(f"pow(2, 4) = {pow(2, 4)}")
print(f"pow(2, 4, 3) = {pow(2, 4, 3)} (modular exponentiation: 2^4 mod 3)")


# ============================================================================
# 7. TYPE CONVERSION
# ============================================================================

print("\n" + "="*70)
print("7. TYPE CONVERSION")
print("="*70)

# int() conversion
print("\n--- int() Conversion ---")
print(f"int(3.9) = {int(3.9)} (truncates decimal)")
print(f"int('42') = {int('42')} (string to int)")
print(f"int(True) = {int(True)}")
print(f"int(False) = {int(False)}")

# float() conversion
print("\n--- float() Conversion ---")
print(f"float(5) = {float(5)}")
print(f"float('3.14') = {float('3.14')}")
print(f"float('inf') = {float('inf')}")

# str() conversion
print("\n--- str() Conversion ---")
print(f"str(42) = '{str(42)}'")
print(f"str(3.14) = '{str(3.14)}'")
print(f"str(True) = '{str(True)}'")

# bool() conversion
print("\n--- bool() Conversion ---")
print(f"bool(1) = {bool(1)}")
print(f"bool(0) = {bool(0)}")
print(f"bool('text') = {bool('text')}")
print(f"bool('') = {bool('')}")

# Decimal type for precision
print("\n--- Decimal Type (for precision) ---")
from decimal import Decimal
print(f"float(2.765) = {2.765}")
print(f"Decimal('2.765') = {Decimal('2.765')}")
print(f"float(3.165) = {3.165}")
print(f"Decimal('3.165') = {Decimal('3.165')}")


# ============================================================================
# 8. IDENTITY VS EQUALITY
# ============================================================================

print("\n" + "="*70)
print("8. IDENTITY VS EQUALITY")
print("="*70)

# Identity operators: is, is not
print("\n--- Identity Operators (is, is not) ---")
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = {a}")
print(f"b = {b}")
print(f"c = a = {c}")
print(f"\na == b: {a == b} (value equality)")
print(f"a is b: {a is b} (same object in memory)")
print(f"a is c: {a is c} (same object in memory)")
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")
print(f"id(c) = {id(c)}")

# Integer caching
print("\n--- Integer Caching ---")
x = 256
y = 256
print(f"x = 256, y = 256")
print(f"x is y: {x is y} (True - Python caches small integers)")

x = 257
y = 257
print(f"x = 257, y = 257")
print(f"x is y: {x is y} (May be False - outside cache range)")


# ============================================================================
# 9. VARIABLES AND ASSIGNMENT
# ============================================================================

print("\n" + "="*70)
print("9. VARIABLES AND ASSIGNMENT")
print("="*70)

# Variable assignment
print("\n--- Variable Assignment ---")
difference = 20
double = 2 * difference
print(f"difference = {difference}")
print(f"double = 2 * difference = {double}")

# Reassignment and scope
print("\n--- Variable Reassignment ---")
difference = 5
print(f"After reassignment: difference = {difference}")
print(f"double (unchanged from previous assignment) = {double}")

# Multiple assignment
print("\n--- Multiple Assignment ---")
x, y, z = 1, 2, 3
print(f"x, y, z = 1, 2, 3")
print(f"x = {x}, y = {y}, z = {z}")

# Swapping variables
print("\n--- Variable Swapping ---")
a, b = 10, 20
print(f"Before swap: a = {a}, b = {b}")
a, b = b, a
print(f"After swap: a = {a}, b = {b}")

# Augmented assignment
print("\n--- Augmented Assignment ---")
num = 5
print(f"num = {num}")
num += 3
print(f"num += 3 → num = {num}")
num -= 2
print(f"num -= 2 → num = {num}")
num *= 2
print(f"num *= 2 → num = {num}")
num //= 3
print(f"num //= 3 → num = {num}")


# ============================================================================
# 10. MEMBERSHIP OPERATORS
# ============================================================================

print("\n" + "="*70)
print("10. MEMBERSHIP OPERATORS")
print("="*70)

# in and not in
print("\n--- Membership Operators (in, not in) ---")
fruits = ['apple', 'banana', 'orange']
print(f"fruits = {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")

text = "Python"
print(f"\ntext = '{text}'")
print(f"'Py' in text: {'Py' in text}")
print(f"'Java' in text: {'Java' in text}")


# ============================================================================
# 11. FUNCTIONS AND SCOPE
# ============================================================================

print("\n" + "="*70)
print("11. FUNCTIONS AND SCOPE")
print("="*70)

# Function definition and return
print("\n--- Function Definition ---")

def convert_celsius_to_fahrenheit(degree_in_celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    return 9 / 5 * degree_in_celsius + 32

temp_f = convert_celsius_to_fahrenheit(0)
print(f"0°C = {temp_f}°F")
temp_f = convert_celsius_to_fahrenheit(100)
print(f"100°C = {temp_f}°F")

# Function with local variables
print("\n--- Function with Local Variables ---")

def quadratic(a, b, c, x):
    """Calculate quadratic function: ax² + bx + c"""
    first = a * x ** 2
    second = b * x
    third = c
    return first + second + third

result = quadratic(2, 3, 4, 0.5)
print(f"quadratic(2, 3, 4, 0.5) = {result}")

# Function returning None
print("\n--- Function Returning None ---")

def f(x):
    x = x * 3

result = f(3)
print(f"f(3) returns: {result}")
print(f"Type: {type(result)}")

# Function with multiple parameters
print("\n--- Function with Multiple Parameters ---")

def calculate_power(base, exponent):
    """Calculate base raised to exponent."""
    return base ** exponent

print(f"calculate_power(2, 3) = {calculate_power(2, 3)}")
print(f"calculate_power(5, 2) = {calculate_power(5, 2)}")

# Default parameters
print("\n--- Default Parameters ---")

def greet(name, greeting="Hello"):
    """Greet someone with optional custom greeting."""
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))


# ============================================================================
# 12. TYPE CHECKING
# ============================================================================

print("\n" + "="*70)
print("12. TYPE CHECKING")
print("="*70)

# Using type()
print("\n--- Using type() ---")
values = [42, 3.14, "text", True, None, [1, 2, 3]]
for val in values:
    print(f"type({val!r}) = {type(val).__name__}")

# Using isinstance()
print("\n--- Using isinstance() ---")
value = 42
print(f"isinstance({value}, int): {isinstance(value, int)}")
print(f"isinstance({value}, float): {isinstance(value, float)}")
print(f"isinstance({value}, (int, float)): {isinstance(value, (int, float))}")

value = 3.14
print(f"isinstance({value}, (int, float)): {isinstance(value, (int, float))}")


# ============================================================================
# 13. PRACTICE EXERCISES
# ============================================================================

print("\n" + "="*70)
print("13. PRACTICE EXERCISES")
print("="*70)

# Exercise 1: Temperature conversion
print("\n--- Exercise 1: Temperature Conversions ---")

def celsius_to_fahrenheit(celsius):
    return (9/5 * celsius) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (5/9 * (fahrenheit - 32))

temps_c = [0, 25, 100, -40]
print("Celsius to Fahrenheit:")
for c in temps_c:
    f = celsius_to_fahrenheit(c)
    print(f"  {c}°C = {f}°F")

# Exercise 2: Number operations
print("\n--- Exercise 2: Number Operations ---")

def gcd(a, b):
    """Find greatest common divisor."""
    while b:
        a, b = b, a % b
    return a

print(f"GCD(48, 18) = {gcd(48, 18)}")
print(f"GCD(100, 50) = {gcd(100, 50)}")

# Exercise 3: String operations
print("\n--- Exercise 3: String Operations ---")

def is_palindrome(s):
    """Check if string is palindrome."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(f"is_palindrome('racecar'): {is_palindrome('racecar')}")
print(f"is_palindrome('A man a plan a canal Panama'): {is_palindrome('A man a plan a canal Panama')}")
print(f"is_palindrome('hello'): {is_palindrome('hello')}")

# Exercise 4: Type conversions
print("\n--- Exercise 4: Type Conversions ---")

def convert_to_int(value):
    """Safely convert value to int."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

print(f"convert_to_int('42'): {convert_to_int('42')}")
print(f"convert_to_int('3.14'): {convert_to_int('3.14')}")
print(f"convert_to_int('abc'): {convert_to_int('abc')}")
print(f"convert_to_int(True): {convert_to_int(True)}")

print("\n" + "="*70)
print("END OF SYNTAX, TYPES, AND OPERATORS")
print("="*70)
