"""
Collections and Comprehensions

This module covers Python's built-in data structures and efficient ways to create and manipulate them:
- Lists: creation, indexing, methods
- Tuples: immutable sequences
- Dictionaries: key-value pairs
- Sets: unique unordered collections
- List comprehensions, dict comprehensions, set comprehensions
- Unpacking and zip()
"""

# ============================================================================
# 1. LISTS
# ============================================================================

print("\n" + "="*70)
print("1. LISTS - Mutable Ordered Collections")
print("="*70)

# Creating lists
print("\n--- Creating Lists ---")
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "text", 3.14, True, None]
nested = [[1, 2], [3, 4], [5, 6]]

print(f"Empty list: {empty_list}")
print(f"Numbers: {numbers}")
print(f"Mixed types: {mixed}")
print(f"Nested: {nested}")

# Indexing and slicing
print("\n--- Indexing and Slicing ---")
items = ['a', 'b', 'c', 'd', 'e']
print(f"List: {items}")
print(f"items[0]: {items[0]}")
print(f"items[-1]: {items[-1]}")
print(f"items[1:3]: {items[1:3]}")
print(f"items[:3]: {items[:3]}")
print(f"items[2:]: {items[2:]}")
print(f"items[::2]: {items[::2]}")  # every 2nd element
print(f"items[::-1]: {items[::-1]}")  # reversed

# List methods
print("\n--- List Methods ---")
nums = [3, 1, 4, 1, 5, 9]
print(f"Original: {nums}")

# append
nums_copy = nums.copy()
nums_copy.append(2)
print(f"After append(2): {nums_copy}")

# extend
nums_copy = nums.copy()
nums_copy.extend([10, 11])
print(f"After extend([10, 11]): {nums_copy}")

# insert
nums_copy = nums.copy()
nums_copy.insert(2, 99)
print(f"After insert(2, 99): {nums_copy}")

# remove
nums_copy = nums.copy()
nums_copy.remove(1)  # removes first occurrence
print(f"After remove(1): {nums_copy}")

# pop
nums_copy = nums.copy()
popped = nums_copy.pop()  # removes last element
print(f"After pop(): {nums_copy}, popped: {popped}")

nums_copy = nums.copy()
popped = nums_copy.pop(0)  # removes first element
print(f"After pop(0): {nums_copy}, popped: {popped}")

# index and count
print(f"nums.index(1): {nums.index(1)}")
print(f"nums.count(1): {nums.count(1)}")

# sort and reverse
nums_copy = nums.copy()
nums_copy.sort()
print(f"After sort(): {nums_copy}")

nums_copy = nums.copy()
nums_copy.reverse()
print(f"After reverse(): {nums_copy}")

# sorted (returns new list) and reversed (returns iterator)
print(f"sorted(nums): {sorted(nums)}")
print(f"sorted(nums, reverse=True): {sorted(nums, reverse=True)}")


# ============================================================================
# 2. TUPLES
# ============================================================================

print("\n" + "="*70)
print("2. TUPLES - Immutable Ordered Collections")
print("="*70)

# Creating tuples
print("\n--- Creating Tuples ---")
empty_tuple = ()
single_item = (1,)  # comma required for single item
numbers = (1, 2, 3, 4, 5)
mixed = (1, "text", 3.14, True)
nested = ((1, 2), (3, 4), (5, 6))

print(f"Empty tuple: {empty_tuple}")
print(f"Single item: {single_item}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")

# Indexing and slicing
print("\n--- Indexing and Slicing ---")
items = ('a', 'b', 'c', 'd', 'e')
print(f"Tuple: {items}")
print(f"items[0]: {items[0]}")
print(f"items[-1]: {items[-1]}")
print(f"items[1:4]: {items[1:4]}")

# Tuple methods
print("\n--- Tuple Methods ---")
nums = (1, 2, 3, 2, 1, 2)
print(f"nums: {nums}")
print(f"nums.count(2): {nums.count(2)}")
print(f"nums.index(3): {nums.index(3)}")

# Tuple unpacking
print("\n--- Tuple Unpacking ---")
point = (3, 5)
x, y = point
print(f"point: {point}")
print(f"x, y = point: x={x}, y={y}")

a, b, c = (1, 2, 3)
print(f"a, b, c = (1, 2, 3): a={a}, b={b}, c={c}")

# Swapping with tuples
print("\n--- Swapping with Tuples ---")
a, b = 10, 20
print(f"Before: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")


# ============================================================================
# 3. DICTIONARIES
# ============================================================================

print("\n" + "="*70)
print("3. DICTIONARIES - Key-Value Pairs")
print("="*70)

# Creating dictionaries
print("\n--- Creating Dictionaries ---")
empty_dict = {}
student = {"name": "Alice", "age": 25, "grade": "A"}
person = dict(name="Bob", age=30, city="NYC")

print(f"Empty dict: {empty_dict}")
print(f"Student: {student}")
print(f"Person: {person}")

# Accessing values
print("\n--- Accessing Values ---")
print(f"student['name']: {student['name']}")
print(f"student.get('age'): {student.get('age')}")
print(f"student.get('phone', 'N/A'): {student.get('phone', 'N/A')}")  # default

# Adding and updating
print("\n--- Adding and Updating ---")
data = {"a": 1, "b": 2}
print(f"Original: {data}")

data["c"] = 3  # add new key
print(f"After adding 'c': {data}")

data["a"] = 10  # update existing
print(f"After updating 'a': {data}")

data.update({"d": 4, "e": 5})  # update multiple
print(f"After update(): {data}")

# Deleting
print("\n--- Deleting ---")
data = {"a": 1, "b": 2, "c": 3}
del data["b"]
print(f"After del data['b']: {data}")

popped = data.pop("a")
print(f"After pop('a'): {data}, popped value: {popped}")

# Dictionary methods
print("\n--- Dictionary Methods ---")
person = {"name": "Charlie", "age": 28, "city": "Boston"}
print(f"person.keys(): {list(person.keys())}")
print(f"person.values(): {list(person.values())}")
print(f"person.items(): {list(person.items())}")

# Iteration
print("\n--- Dictionary Iteration ---")
for key, value in person.items():
    print(f"  {key}: {value}")

print("Keys:")
for key in person:
    print(f"  {key}")


# ============================================================================
# 4. SETS
# ============================================================================

print("\n" + "="*70)
print("4. SETS - Unique Unordered Collections")
print("="*70)

# Creating sets
print("\n--- Creating Sets ---")
empty_set = set()
numbers = {1, 2, 3, 4, 5}
mixed = {1, "text", 3.14}
from_list = set([1, 2, 2, 3, 3, 3])

print(f"Empty set: {empty_set}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")
print(f"From list [1, 2, 2, 3, 3, 3]: {from_list}")

# Set operations
print("\n--- Set Operations ---")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"a: {a}, b: {b}")
print(f"a | b (union): {a | b}")  # or a.union(b)
print(f"a & b (intersection): {a & b}")  # or a.intersection(b)
print(f"a - b (difference): {a - b}")  # or a.difference(b)
print(f"a ^ b (symmetric difference): {a ^ b}")  # or a.symmetric_difference(b)

# Set methods
print("\n--- Set Methods ---")
s = {1, 2, 3}
print(f"Original: {s}")

s.add(4)
print(f"After add(4): {s}")

s.update({5, 6})
print(f"After update({{5, 6}}): {s}")

s.discard(2)
print(f"After discard(2): {s}")

# Membership test
print("\n--- Membership Test ---")
s = {1, 2, 3, 4, 5}
print(f"3 in s: {3 in s}")
print(f"10 in s: {10 in s}")


# ============================================================================
# 5. LIST COMPREHENSIONS
# ============================================================================

print("\n" + "="*70)
print("5. LIST COMPREHENSIONS")
print("="*70)

# Simple list comprehension
print("\n--- Simple List Comprehension ---")
squares = [x ** 2 for x in range(5)]
print(f"[x ** 2 for x in range(5)]: {squares}")

# With filter (if condition)
print("\n--- List Comprehension with Filter ---")
evens = [x for x in range(10) if x % 2 == 0]
print(f"[x for x in range(10) if x % 2 == 0]: {evens}")

# Transformation and filter
print("\n--- Transform and Filter ---")
result = [x ** 2 for x in range(10) if x % 2 == 0]
print(f"[x ** 2 for x in range(10) if x % 2 == 0]: {result}")

# Nested list comprehension
print("\n--- Nested List Comprehension ---")
pairs = [(x, y) for x in range(3) for y in range(3) if x != y]
print(f"[(x, y) for x in range(3) for y in range(3) if x != y]:")
print(f"  {pairs}")

# String processing
print("\n--- String Processing ---")
words = ["python", "is", "awesome"]
caps = [word.upper() for word in words]
print(f"Words: {words}")
print(f"Capitalized: {caps}")

lengths = [len(word) for word in words]
print(f"Lengths: {lengths}")


# ============================================================================
# 6. DICTIONARY COMPREHENSIONS
# ============================================================================

print("\n" + "="*70)
print("6. DICTIONARY COMPREHENSIONS")
print("="*70)

# Simple dict comprehension
print("\n--- Simple Dict Comprehension ---")
squares_dict = {x: x ** 2 for x in range(5)}
print(f"{{x: x ** 2 for x in range(5)}}: {squares_dict}")

# From list of tuples
print("\n--- From List of Tuples ---")
pairs = [("a", 1), ("b", 2), ("c", 3)]
dict_from_pairs = {k: v for k, v in pairs}
print(f"Pairs: {pairs}")
print(f"Dict: {dict_from_pairs}")

# With filter
print("\n--- Dict Comprehension with Filter ---")
numbers = range(10)
even_squares = {x: x ** 2 for x in numbers if x % 2 == 0}
print(f"{{x: x ** 2 for x in range(10) if x % 2 == 0}}: {even_squares}")

# From existing dict
print("\n--- Transform Existing Dict ---")
original = {"a": 1, "b": 2, "c": 3}
doubled = {k: v * 2 for k, v in original.items()}
print(f"Original: {original}")
print(f"Doubled: {doubled}")


# ============================================================================
# 7. SET COMPREHENSIONS
# ============================================================================

print("\n" + "="*70)
print("7. SET COMPREHENSIONS")
print("="*70)

# Simple set comprehension
print("\n--- Simple Set Comprehension ---")
squares_set = {x ** 2 for x in range(5)}
print(f"{{x ** 2 for x in range(5)}}: {squares_set}")

# Removing duplicates
print("\n--- Removing Duplicates ---")
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = {x for x in numbers}
print(f"Numbers: {numbers}")
print(f"Unique: {unique}")

# With filter
print("\n--- Set Comprehension with Filter ---")
odd_squares = {x ** 2 for x in range(10) if x % 2 == 1}
print(f"{{x ** 2 for x in range(10) if x % 2 == 1}}: {odd_squares}")


# ============================================================================
# 8. ZIP AND UNPACKING
# ============================================================================

print("\n" + "="*70)
print("8. ZIP AND UNPACKING")
print("="*70)

# zip function
print("\n--- zip() Function ---")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 28]
cities = ["NYC", "LA", "Boston"]

zipped = list(zip(names, ages))
print(f"names: {names}")
print(f"ages: {ages}")
print(f"zip(names, ages): {zipped}")

# Multiple sequences
print("\n--- zip() with Multiple Sequences ---")
zipped_all = list(zip(names, ages, cities))
print(f"zip(names, ages, cities): {zipped_all}")

# Unzipping
print("\n--- Unzipping ---")
pairs = [("a", 1), ("b", 2), ("c", 3)]
letters, numbers = zip(*pairs)
print(f"pairs: {pairs}")
print(f"After zip(*pairs):")
print(f"  letters: {letters}")
print(f"  numbers: {numbers}")

# Star unpacking
print("\n--- Star Unpacking (*) ---")
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(f"numbers: {numbers}")
print(f"first, *middle, last = numbers")
print(f"  first: {first}")
print(f"  middle: {middle}")
print(f"  last: {last}")


# ============================================================================
# 9. PRACTICE EXERCISES
# ============================================================================

print("\n" + "="*70)
print("9. PRACTICE EXERCISES")
print("="*70)

# Exercise 1: List operations
print("\n--- Exercise 1: List Operations ---")

def analyze_list(lst):
    """Analyze a list."""
    return {
        "length": len(lst),
        "sum": sum(lst) if all(isinstance(x, (int, float)) for x in lst) else None,
        "max": max(lst) if all(isinstance(x, (int, float)) for x in lst) else None,
        "min": min(lst) if all(isinstance(x, (int, float)) for x in lst) else None,
        "unique": len(set(lst))
    }

nums = [1, 2, 2, 3, 3, 3, 4, 5]
print(f"List: {nums}")
print(f"Analysis: {analyze_list(nums)}")

# Exercise 2: Dict operations
print("\n--- Exercise 2: Dict Operations ---")

def group_by_length(words):
    """Group words by their length."""
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = []
        result[length].append(word)
    return result

words = ["apple", "pie", "python", "code", "data", "ai"]
print(f"Words: {words}")
print(f"Grouped by length: {group_by_length(words)}")

# Exercise 3: Set operations
print("\n--- Exercise 3: Set Operations ---")

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
set1, set2 = set(list1), set(list2)

print(f"List1: {list1}, List2: {list2}")
print(f"Common: {set1 & set2}")
print(f"Only in list1: {set1 - set2}")
print(f"Only in list2: {set2 - set1}")
print(f"Either or both: {set1 | set2}")

# Exercise 4: Complex comprehension
print("\n--- Exercise 4: Complex Comprehension ---")

students = [
    {"name": "Alice", "scores": [85, 90, 88]},
    {"name": "Bob", "scores": [75, 80, 78]},
    {"name": "Charlie", "scores": [95, 92, 98]}
]

avg_scores = {
    student["name"]: sum(student["scores"]) / len(student["scores"])
    for student in students
}
print(f"Student average scores: {avg_scores}")

print("\n" + "="*70)
print("END OF COLLECTIONS AND COMPREHENSIONS")
print("="*70)
