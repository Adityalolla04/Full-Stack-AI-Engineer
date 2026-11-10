# Collections and Comprehensions

[Back to Python](../README.md)

## In Simple Words

Python provides powerful built-in data structures (lists, tuples, dicts, sets) and elegant syntax (comprehensions) for creating and transforming collections.

## Core Concepts

### 1. **Lists - Mutable Ordered Sequences**
- **Creating lists**: `[1, 2, 3]`, `list()`, `[x for x in range(5)]`
  - Mutable: can add, remove, modify elements
  - Ordered: maintain insertion order
  - Allow duplicates and mixed types

- **Indexing and slicing**:
  - Index: `list[0]` (first), `list[-1]` (last)
  - Slice: `list[1:3]` (elements 1-2), `list[:3]` (first 3), `list[2:]` (from 2 onward)
  - Step: `list[::2]` (every 2nd), `list[::-1]` (reversed)

- **Mutating methods**:
  - `append(x)`: Add at end
  - `extend(iterable)`: Add multiple elements
  - `insert(i, x)`: Add at specific index
  - `remove(x)`: Remove first occurrence
  - `pop()`: Remove and return last, `pop(i)`: at index i
  - `sort()`: Sort in place, `reverse()`: Reverse in place
  - `clear()`: Remove all elements

- **Query methods**:
  - `index(x)`: Find first position
  - `count(x)`: Count occurrences
  - `copy()`: Create shallow copy

### 2. **Tuples - Immutable Ordered Sequences**
- **Creating tuples**: `(1, 2, 3)`, `tuple([1, 2, 3])`, `(1,)` (single item needs comma)
  - Immutable: cannot change after creation
  - Hashable: can be dictionary keys or set elements
  - Ordered: maintain insertion order

- **Indexing and slicing**: Same as lists

- **Methods**: `index(x)`, `count(x)` (limited methods)

- **Unpacking**: Assign multiple values
  - `x, y = (1, 2)` or even `x, y = [1, 2]`
  - Swapping: `x, y = y, x`
  - Extended unpacking: `a, *b, c = [1, 2, 3, 4, 5]`

### 3. **Dictionaries - Key-Value Pairs**
- **Creating dicts**: `{"a": 1, "b": 2}`, `dict(a=1, b=2)`, `{k: v for ...}`
  - Mutable: add, remove, modify entries
  - Keys must be hashable; values can be anything
  - Ordered (Python 3.7+): maintain insertion order

- **Accessing**:
  - `dict[key]`: Get value (raises KeyError if missing)
  - `dict.get(key, default)`: Get with default fallback

- **Modifying**:
  - `dict[key] = value`: Add or update
  - `dict.update(other)`: Merge
  - `del dict[key]`: Remove
  - `dict.pop(key)`: Remove and return

- **Iteration**:
  - `for key in dict:` - iterate keys
  - `for key, value in dict.items():` - iterate pairs
  - `for value in dict.values():` - iterate values

### 4. **Sets - Unique Unordered Collections**
- **Creating sets**: `{1, 2, 3}`, `set([1, 2, 2, 3])` (removes duplicates)
  - Mutable: add and remove elements
  - Unordered: no positional access
  - Unique elements only
  - Empty set: `set()` (not `{}`)

- **Set operations** (mathematical):
  - Union: `a | b` - all elements
  - Intersection: `a & b` - common elements
  - Difference: `a - b` - in a but not b
  - Symmetric difference: `a ^ b` - in either but not both

- **Membership test**: `x in set` (O(1) lookup)

- **Methods**:
  - `add(x)`: Add element
  - `update(iterable)`: Add multiple
  - `discard(x)`: Remove if exists
  - `remove(x)`: Remove (raises KeyError if missing)

### 5. **List Comprehensions**
- **Basic syntax**: `[expression for item in iterable]`
  - Example: `[x**2 for x in range(5)]` → `[0, 1, 4, 9, 16]`

- **With filtering**: `[expression for item in iterable if condition]`
  - Example: `[x for x in range(10) if x % 2 == 0]`

- **Transformation + filter**: `[transform(x) for x in iterable if condition]`
  - Example: `[x**2 for x in range(10) if x % 2 == 0]`

- **Nested comprehensions**: `[expr for x in iter1 for y in iter2]`
  - Creates combinations with filtering

### 6. **Dictionary Comprehensions**
- **Syntax**: `{key_expr: value_expr for item in iterable}`
  - Example: `{x: x**2 for x in range(5)}`

- **From list of tuples**: `{k: v for k, v in items}`

- **With filtering**: `{k: v for k, v in items if condition}`

### 7. **Set Comprehensions**
- **Syntax**: `{expression for item in iterable}`
  - Automatically removes duplicates
  - Example: `{x**2 for x in range(10)}`

### 8. **zip() and Unpacking**
- **zip() function**: Combine iterables into tuples
  - `zip([1, 2], ['a', 'b'])` → `[(1, 'a'), (2, 'b')]`
  - Stops at shortest iterable

- **Parallel iteration**: `for num, letter in zip(numbers, letters):`

- **Unzipping**: `letters, numbers = zip(*list_of_tuples)`

- **Extended unpacking** (star operator):
  - `first, *middle, last = [1, 2, 3, 4, 5]`
  - `first` = 1, `middle` = [2, 3, 4], `last` = 5

## Performance Characteristics

- **List lookup**: O(n) - slow for large lists
- **Tuple lookup**: O(n) - same as list, but immutable
- **Dictionary lookup**: O(1) average - very fast
- **Set lookup**: O(1) average - very fast
- **Comprehensions**: Generally faster than equivalent loops

## Common Mistakes

1. **Mutable defaults in functions**: `def f(x=[]): x.append(1)` - shared!
2. **Modifying collection while iterating**: Can skip elements
3. **Empty set syntax**: `set()` not `{}` (latter is empty dict)
4. **Single-tuple comma**: `(1)` is int, `(1,)` is tuple
5. **Shallow copy issue**: `list.copy()` doesn't copy nested lists
6. **Dictionary key error**: Use `.get()` for safe access
7. **Tuple as dict key only if hashable**: Can't use lists as keys
8. **Set membership only for hashable**: Sets reject lists/dicts

## Practice Exercises

1. **List operations**: Filter, transform, sort collections
2. **Tuple unpacking**: Extract values elegantly
3. **Dict building**: Create dicts from various sources
4. **Set operations**: Find common elements, unique items
5. **Comprehensions**: Write compact list/dict/set comprehensions
6. **Data transformation**: Convert between collection types
7. **Nested structures**: Work with lists of dicts, dicts of lists
8. **Choose right structure**: Performance vs. functionality

## Reference Implementation

Run `collections-comprehensions.py` to see comprehensive examples and exercises.

## Recall Checklist

- [ ] Create and manipulate lists, tuples, dicts, sets
- [ ] Index and slice sequences (including negative indices)
- [ ] Understand mutability vs immutability
- [ ] Use list/dict/set comprehensions
- [ ] Iterate over collections (keys, values, items)
- [ ] Use zip() and unpacking
- [ ] Choose appropriate collection type for use case
- [ ] Understand performance (O(1) vs O(n) lookup)

## Resources

- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Collections Module](https://docs.python.org/3/library/collections.html)
- [AlgoMaster Python Roadmap](https://algomaster.io/roadmaps/python)
