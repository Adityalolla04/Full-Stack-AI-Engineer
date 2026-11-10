# Control Flow and Functions

[Back to Python](../README.md)

## In Simple Words

Control flow determines which code runs and in what order. Functions organize code into reusable, testable blocks.

## Core Concepts

### 1. **Conditional Statements**
- **if statement**: Execute code only if condition is True
  - Example: `if age >= 18: print("Adult")`
  - Condition must be boolean or truthy/falsy

- **if-else statement**: Choose between two code paths
  - Example: `if x > 0: print("positive") else: print("non-positive")`

- **if-elif-else chain**: Multiple conditions
  - Example: Multiple cases for grades (A, B, C, D, F)
  - Conditions checked top-to-bottom; first match executes
  - else is optional and catches all remaining cases

- **Ternary operator** (conditional expression)
  - Syntax: `value_if_true if condition else value_if_false`
  - Example: `"adult" if age >= 18 else "minor"`

- **Comparison operators**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical operators**: `and`, `or`, `not`

### 2. **For and While Loops**
- **for loop**: Iterate over sequences (strings, lists, tuples, range)
  - Syntax: `for item in sequence:`
  - `range()`: Generate numbers - `range(n)`, `range(start, stop, step)`
  - `enumerate()`: Get index and value - `for i, val in enumerate(seq):`
  - **for-else**: else runs if loop completes without break

- **while loop**: Repeat while condition is True
  - Syntax: `while condition:`
  - Risk of infinite loops
  - **while-else**: else runs if condition becomes False (not via break)

- **break**: Exit loop immediately
  - Skips remaining iterations and else block
  - In nested loops, only breaks innermost

- **continue**: Skip current iteration
  - Goes to next iteration
  - Useful for filtering

### 3. **Function Basics**
- **Function definition**: `def function_name(parameters):`
  - Docstring: first string in function (explains purpose)
  - Parameters: variables function accepts
  - Must be defined before calling

- **Calling functions**: `function_name(arguments)`
  - Arguments: actual values passed
  - Execution and return value

- **Return statement**: `return value`
  - Exits function and returns value
  - No explicit return means function returns None
  - Can return multiple values: `return x, y` (creates tuple)

### 4. **Function Parameters**
- **Positional parameters**: Order matters
  - Example: `def add(a, b):`
  - Arguments must match order and count

- **Default parameters**: Optional with default value
  - Syntax: `def greet(name, greeting="Hello"):`
  - **WARNING**: Mutable defaults (list, dict) shared across calls

- **Keyword arguments**: Pass by name
  - Order doesn't matter: `greet(greeting="Hi", name="Alice")`
  - Mix with positional: `func(pos_arg, kwarg=value)`

- **\*args**: Variable positional arguments
  - Collected into tuple
  - Access: `args[0]`, `args[1]`, etc.

- **\*\*kwargs**: Variable keyword arguments
  - Collected into dictionary
  - Access: `kwargs['key']` or `kwargs.get('key')`

- **Parameter order**: positional → \*args → keyword-only → \*\*kwargs

### 5. **Scope and Lifetime**
- **Local scope**: Inside function
  - Created when function called, destroyed on return
  - Not accessible outside function

- **Global scope**: Module level
  - Accessible from anywhere in module
  - Shared across all function calls

- **Enclosing scope**: Outer function in nested functions
  - Accessible to inner functions

- **LEGB lookup rule**: Local → Enclosing → Global → Built-in

- **global keyword**: Declare to modify global variable
  - Syntax: `global var_name` (before using)
  - Avoid when possible (side effects)

- **nonlocal keyword**: Modify enclosing scope variable
  - Only in nested functions
  - Syntax: `nonlocal var_name`

### 6. **Lambda Functions**
- **Anonymous functions**: Small unnamed functions
  - Syntax: `lambda args: expression`
  - Single expression, returns result
  - Example: `square = lambda x: x ** 2`

- **Common uses**:
  - `map(lambda x: x**2, [1, 2, 3])` - apply function
  - `filter(lambda x: x > 5, [1, 3, 6, 8])` - filter elements
  - `sorted(list, key=lambda x: x[1])` - sort by key

### 7. **Higher-Order Functions**
- **Taking functions as arguments**:
  - Example: `def apply_op(a, b, op): return op(a, b)`
  - Used for callbacks and functional patterns

- **Returning functions**:
  - Returns new function with modified behavior
  - Example: Factory pattern, decorators

- **Closures**: Inner function captures outer scope
  - "Remembers" variables from outer function
  - Used in decorators, factories

### 8. **Recursion**
- **Function calling itself**: Powerful pattern for certain problems
  - Must have **base case** (stop condition)
  - Must progress toward base case
  - Each call uses new scope

- **Stack**: Each call stored on call stack
  - Python limits recursion (~1000 calls)
  - Too deep → RecursionError

- **Examples**: Factorial, Fibonacci, tree traversal

- **Memoization**: Cache results to avoid recomputation
  - Dramatically improves performance
  - Fibonacci: O(2^n) → O(n)

### 9. **Decorators**
- **Wrapper functions**: Modify behavior of another function
  - Syntax: `@decorator_name` above function
  - Decorator wraps original function

- **Pattern**:
  1. Define decorator function
  2. Create wrapper inside
  3. Wrapper calls original function
  4. Return wrapper

- **Use cases**: Logging, timing, authentication, caching

## Common Mistakes

1. **Indentation errors**: Critical in Python
2. **Off-by-one in range()**: Remember exclusive end
3. **Modifying collection during iteration**: Skips elements
4. **Mutable default arguments**: Shared across calls
5. **Forgetting return**: Returns None
6. **Global/nonlocal scope issues**: Confusing modifications
7. **Infinite loops**: Forgetting to update condition
8. **Deep recursion**: Stack overflow

## Practice Exercises

1. **Conditionals**: Grade system based on scores
2. **Loops**: Sum, filter, search with for/while
3. **Functions**: Multiple parameter types
4. **Scope**: Nested function variable access
5. **Lambda**: Sort complex data
6. **Recursion**: Factorial, Fibonacci
7. **Decorators**: Logging or timing wrapper

## Reference Implementation

Run `control-flow-functions.py` to see comprehensive examples and exercises.

## Recall Checklist

- [ ] if-elif-else chains and comparisons
- [ ] for loops with range, lists, dictionaries, enumerate
- [ ] while loops and loop control
- [ ] Function definition with parameters
- [ ] Positional, keyword, *args, **kwargs
- [ ] Variable scope (LEGB rule)
- [ ] Lambda and higher-order functions
- [ ] Recursion with base case
- [ ] Simple decorators

## Resources

- [Python Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Python Functions](https://docs.python.org/3/tutorial/functions.html)
- [AlgoMaster Python Roadmap](https://algomaster.io/roadmaps/python)
