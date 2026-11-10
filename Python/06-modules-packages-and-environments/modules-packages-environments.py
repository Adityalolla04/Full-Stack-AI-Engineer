"""
Modules, Packages, and Environments - Python Project Structure

This module covers how to organize Python code into modules and packages:
- Importing modules (import, from...import, as)
- Creating and using modules
- Package structure (__init__.py)
- Built-in modules (os, sys, pathlib)
- Module vs script behavior (__name__ == "__main__")
- Virtual environments concept
- pip and package installation concepts
"""

import os
import sys
import pathlib
from pathlib import Path
from datetime import datetime

# ============================================================================
# 1. IMPORTING MODULES
# ============================================================================

print("\n" + "="*70)
print("1. IMPORTING MODULES")
print("="*70)

print("\n--- Basic Import ---")
import math
print(f"math module: {math}")
print(f"math.pi: {math.pi}")
print(f"math.sqrt(16): {math.sqrt(16)}")

print("\n--- From...Import ---")
from math import pi, sqrt, cos
print(f"pi: {pi}")
print(f"sqrt(25): {sqrt(25)}")
print(f"cos(0): {cos(0)}")

print("\n--- Import with Alias ---")
import random as rnd
from math import factorial as fact
print(f"Random integer (1-10): {rnd.randint(1, 10)}")
print(f"Factorial of 5: {fact(5)}")

print("\n--- Import Multiple Items ---")
from statistics import mean, median, stdev
data = [1, 2, 3, 4, 5, 100]
print(f"Data: {data}")
print(f"Mean: {mean(data):.2f}")
print(f"Median: {median(data)}")
print(f"Std Dev: {stdev(data):.2f}")

# ============================================================================
# 2. MODULE VS SCRIPT BEHAVIOR
# ============================================================================

print("\n" + "="*70)
print("2. MODULE VS SCRIPT BEHAVIOR (__name__ == '__main__')")
print("="*70)

print(f"\nCurrent script __name__: {__name__}")

def helper_function():
    return "This function runs when module is imported"

if __name__ == "__main__":
    print("This code runs when script is executed directly")
    print(helper_function())
else:
    print("This code runs when module is imported")

# ============================================================================
# 3. EXPLORING sys MODULE
# ============================================================================

print("\n" + "="*70)
print("3. EXPLORING sys MODULE")
print("="*70)

print("\n--- sys Information ---")
print(f"Python version: {sys.version}")
print(f"Python version info: {sys.version_info}")
print(f"Platform: {sys.platform}")
print(f"Executable: {sys.executable}")

print("\n--- sys.path ---")
print(f"Number of paths: {len(sys.path)}")
print("First few paths in sys.path:")
for i, path in enumerate(sys.path[:3]):
    print(f"  {i}: {path}")

print("\n--- sys.modules (sample) ---")
print(f"Total modules loaded: {len(sys.modules)}")
print("Sample modules:")
for module_name in list(sys.modules.keys())[:5]:
    print(f"  {module_name}")

# ============================================================================
# 4. EXPLORING os MODULE
# ============================================================================

print("\n" + "="*70)
print("4. EXPLORING os MODULE")
print("="*70)

print("\n--- Current Directory ---")
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

print("\n--- Listing Directory Contents ---")
print(f"Items in current directory (first 10):")
try:
    items = os.listdir(current_dir)[:10]
    for item in items:
        item_path = os.path.join(current_dir, item)
        file_type = "DIR" if os.path.isdir(item_path) else "FILE"
        print(f"  [{file_type}] {item}")
except Exception as e:
    print(f"  Error: {e}")

print("\n--- File Path Operations ---")
file_path = os.path.join(current_dir, "example.txt")
print(f"Full path: {file_path}")
print(f"Directory: {os.path.dirname(file_path)}")
print(f"Filename: {os.path.basename(file_path)}")
print(f"Split path: {os.path.split(file_path)}")

print("\n--- Environment Variables ---")
print("Sample environment variables:")
env_vars = ['PATH', 'PYTHONPATH', 'TEMP', 'USER']
for var in env_vars:
    value = os.environ.get(var, "Not set")
    if value:
        value = value[:50] + "..." if len(value) > 50 else value
    print(f"  {var}: {value}")

# ============================================================================
# 5. EXPLORING pathlib MODULE
# ============================================================================

print("\n" + "="*70)
print("5. EXPLORING pathlib MODULE")
print("="*70)

print("\n--- Creating Path Objects ---")
current_path = Path.cwd()
print(f"Current directory (pathlib): {current_path}")
print(f"Type: {type(current_path)}")

print("\n--- Path Operations ---")
home_path = Path.home()
print(f"Home directory: {home_path}")

# Create paths using / operator
test_path = current_path / "test" / "file.txt"
print(f"Constructed path: {test_path}")
print(f"Parent directory: {test_path.parent}")
print(f"Filename: {test_path.name}")
print(f"Suffix: {test_path.suffix}")

print("\n--- Path Properties ---")
print(f"Is absolute: {test_path.is_absolute()}")
print(f"As posix (Unix-style): {test_path.as_posix()}")

print("\n--- Globbing Files ---")
print("Python files in current directory:")
for py_file in current_path.glob("*.py"):
    print(f"  {py_file.name}")

# ============================================================================
# 6. CREATING AND USING CUSTOM MODULES
# ============================================================================

print("\n" + "="*70)
print("6. CREATING AND USING CUSTOM MODULES")
print("="*70)

print("\n--- Creating Module Content (Example) ---")
print("""
To create a module named 'math_utils.py':

# math_utils.py
'''Utility functions for math operations'''

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

__all__ = ['add', 'multiply', 'factorial']
""")

print("\n--- Using __all__ ---")
print("The __all__ variable controls what gets imported with 'from module import *'")
print("It's a list of public names to export from a module")

# ============================================================================
# 7. PACKAGE STRUCTURE
# ============================================================================

print("\n" + "="*70)
print("7. PACKAGE STRUCTURE")
print("="*70)

print("""
Package Structure Example:
my_package/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py

The __init__.py file:
- Makes a directory a Python package
- Can be empty or contain initialization code
- Defines what's available when importing the package
- Can set up the package namespace

Example __init__.py content:
from .module1 import function1
from .module2 import function2

__all__ = ['function1', 'function2']
""")

# ============================================================================
# 8. PYTHON PATH AND MODULE SEARCH
# ============================================================================

print("\n" + "="*70)
print("8. PYTHON PATH AND MODULE SEARCH")
print("="*70)

print("""
When Python imports a module, it searches in this order:
1. sys.modules (already loaded modules cache)
2. Built-in modules
3. sys.path directories:
   - The directory containing the script (or current directory)
   - PYTHONPATH environment variable directories
   - Installation-dependent default paths

To add a directory to sys.path:
1. Set PYTHONPATH environment variable
2. Use sys.path.append() or sys.path.insert()
3. Install as a package with pip
""")

print("\n--- Current sys.path ---")
print(f"Number of paths: {len(sys.path)}")
print("First 5 paths:")
for i, p in enumerate(sys.path[:5]):
    print(f"  {i}: {p}")

# ============================================================================
# 9. VIRTUAL ENVIRONMENTS CONCEPT
# ============================================================================

print("\n" + "="*70)
print("9. VIRTUAL ENVIRONMENTS CONCEPT")
print("="*70)

print("""
Virtual Environments:
- Isolated Python environments for different projects
- Separate package installations per project
- Avoid conflicts between project dependencies
- Allow different Python versions per project

Creating a Virtual Environment:
# Using venv (built-in, Python 3.3+)
python -m venv env_name

# Activate (Windows)
env_name\\Scripts\\activate

# Activate (Linux/Mac)
source env_name/bin/activate

# Deactivate
deactivate

Benefits:
- Project isolation
- Reproducible environments
- Clean Python installation
- Easy deployment

Requirements Files:
# Generate requirements.txt
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt
""")

print("\n--- Check if in Virtual Environment ---")
in_venv = hasattr(sys, 'real_prefix') or (
    hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
)
print(f"Currently in virtual environment: {in_venv}")
print(f"Python executable: {sys.executable}")

# ============================================================================
# 10. pip AND PACKAGE INSTALLATION
# ============================================================================

print("\n" + "="*70)
print("10. pip AND PACKAGE INSTALLATION")
print("="*70)

print("""
pip Commands:
- pip install package_name          # Install latest version
- pip install package_name==1.2.3   # Install specific version
- pip install 'package_name>=1.0'   # Install with version constraint
- pip install -r requirements.txt    # Install from file
- pip list                           # List installed packages
- pip show package_name              # Show package info
- pip uninstall package_name         # Uninstall package
- pip freeze                         # Show installed packages in freeze format
- pip search package_name            # Search PyPI (deprecated, use website)

PyPI (Python Package Index):
- Central repository for Python packages
- Search: https://pypi.org
- Source: https://github.com (links from PyPI)

Package Naming:
- Lowercase with underscores or hyphens
- Examples: numpy, pandas, flask, django-rest-framework
""")

print("\n--- Checking Installed Packages ---")
import subprocess
result = subprocess.run([sys.executable, "-m", "pip", "list", "--format=json"], 
                       capture_output=True, text=True)
if result.returncode == 0:
    import json
    try:
        packages = json.loads(result.stdout)
        print("Installed packages (first 10):")
        for pkg in packages[:10]:
            print(f"  {pkg['name']}: {pkg['version']}")
    except:
        print("Could not parse package list")

# ============================================================================
# 11. BUILT-IN MODULES OVERVIEW
# ============================================================================

print("\n" + "="*70)
print("11. COMMON BUILT-IN MODULES")
print("="*70)

print("""
Commonly Used Built-in Modules:

File & Directory:
- os: Operating system interface
- pathlib: Object-oriented filesystem paths
- shutil: High-level file operations
- glob: Pathname pattern expansion

Data & Time:
- datetime: Date and time objects
- time: Time-related functions
- calendar: Calendar functions

Data Types:
- collections: Specialized container types (Counter, defaultdict, namedtuple)
- json: JSON encoding/decoding
- csv: CSV file reading/writing

Math & Random:
- math: Mathematical functions
- random: Random number generation
- statistics: Basic statistical functions

Iteration & Functions:
- itertools: Iterator building blocks
- functools: Higher-order functions
- operator: Standard operators as functions

Utilities:
- sys: System-specific parameters
- copy: Object copying
- pickle: Serialize Python objects
- io: Stream operations
""")

print("\n--- Using datetime Module ---")
now = datetime.now()
print(f"Current datetime: {now}")
print(f"Year: {now.year}, Month: {now.month}, Day: {now.day}")
print(f"Hour: {now.hour}, Minute: {now.minute}, Second: {now.second}")

from datetime import timedelta
tomorrow = now + timedelta(days=1)
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")

print("\n--- Using collections Module ---")
from collections import Counter
words = "the quick brown fox jumps over the lazy dog"
word_count = Counter(words.split())
print(f"Word frequency: {word_count}")
print(f"Most common: {word_count.most_common(3)}")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n" + "="*70)
print("PRACTICE EXERCISES")
print("="*70)

print("""
1. File System Explorer:
   - Create a function using pathlib to:
     - List all Python files in a directory
     - Find largest file in directory
     - Calculate total size of all files
     - Create directory structure

2. Module Creation:
   - Create a math_utils.py module with:
     - add, subtract, multiply, divide functions
     - Calculate average
     - Find max/min in a list
     - Create main script that imports and uses these

3. Configuration Management:
   - Read environment variables for configuration
   - Create a config.py that imports from environment
   - Handle missing environment variables with defaults
   - Log which configuration is being used

4. Virtual Environment Setup:
   - Document steps to create and activate venv
   - Create requirements.txt with specific versions
   - Write script to check if all requirements are installed
   - Show how to update packages

5. Package Structure:
   - Create a package with:
     - __init__.py that exports main classes
     - Multiple modules (utils.py, models.py)
     - Subpackage for database operations
     - Proper import statements and __all__ definitions
""")

print("\n" + "="*70)
print("Module completed successfully!")
print("="*70)
