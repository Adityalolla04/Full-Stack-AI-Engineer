"""
OOP and Dataclasses - Object-Oriented Programming in Python

This module covers object-oriented programming concepts:
- Class definition and initialization
- Instance and class variables
- Methods (instance, class, static)
- Inheritance and polymorphism
- Encapsulation (public, protected, private)
- Magic methods (__init__, __str__, __repr__, __len__, etc.)
- Properties and getters/setters
- Dataclasses introduction
- Composition vs inheritance
"""

from dataclasses import dataclass, field
from typing import List

# ============================================================================
# 1. CLASS DEFINITION AND INITIALIZATION
# ============================================================================

print("\n" + "="*70)
print("1. CLASS DEFINITION AND INITIALIZATION")
print("="*70)

print("\n--- Basic Class ---")

class Dog:
    """A simple Dog class to demonstrate OOP basics"""
    
    def __init__(self, name, age, breed):
        """Initialize a Dog instance"""
        self.name = name
        self.age = age
        self.breed = breed
    
    def bark(self):
        return f"{self.name} says: Woof! Woof!"
    
    def get_info(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}"

dog1 = Dog("Buddy", 3, "Golden Retriever")
print(f"Dog object: {dog1}")
print(f"Name: {dog1.name}, Age: {dog1.age}, Breed: {dog1.breed}")
print(dog1.bark())
print(dog1.get_info())

# ============================================================================
# 2. INSTANCE AND CLASS VARIABLES
# ============================================================================

print("\n" + "="*70)
print("2. INSTANCE AND CLASS VARIABLES")
print("="*70)

print("\n--- Instance vs Class Variables ---")

class Car:
    total_cars = 0  # Class variable - shared by all instances
    
    def __init__(self, make, model):
        self.make = make  # Instance variable - unique to each instance
        self.model = model
        Car.total_cars += 1
    
    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")
car3 = Car("Ford", "Mustang")

print(f"car1: {car1.make} {car1.model}")
print(f"car2: {car2.make} {car2.model}")
print(f"car3: {car3.make} {car3.model}")
print(f"Total cars created: {Car.get_total_cars()}")
print(f"Total cars (via Car.total_cars): {Car.total_cars}")

# ============================================================================
# 3. METHODS - INSTANCE, CLASS, AND STATIC
# ============================================================================

print("\n" + "="*70)
print("3. METHODS - INSTANCE, CLASS, AND STATIC")
print("="*70)

class Calculator:
    """Demonstration of different method types"""
    
    version = "1.0"  # Class variable
    
    def __init__(self, name):
        self.name = name
    
    # Instance method
    def add(self, a, b):
        """Instance method - has access to self"""
        print(f"{self.name} is adding {a} + {b}")
        return a + b
    
    # Class method
    @classmethod
    def get_version(cls):
        """Class method - has access to cls"""
        return f"Calculator version {cls.version}"
    
    # Static method
    @staticmethod
    def is_even(number):
        """Static method - no access to self or cls"""
        return number % 2 == 0

calc = Calculator("MyCalc")
print(f"Add: {calc.add(5, 3)}")
print(f"Version: {Calculator.get_version()}")
print(f"Is 10 even? {Calculator.is_even(10)}")
print(f"Is 7 even? {Calculator.is_even(7)}")

# ============================================================================
# 4. INHERITANCE AND POLYMORPHISM
# ============================================================================

print("\n" + "="*70)
print("4. INHERITANCE AND POLYMORPHISM")
print("="*70)

print("\n--- Single Inheritance ---")

class Animal:
    """Base class"""
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Cat(Animal):
    """Child class inheriting from Animal"""
    def speak(self):
        return f"{self.name} says: Meow!"

class Bird(Animal):
    """Another child class inheriting from Animal"""
    def speak(self):
        return f"{self.name} says: Tweet!"

cat = Cat("Whiskers")
bird = Bird("Tweety")

print(cat.speak())
print(bird.speak())

print("\n--- Polymorphism ---")
animals = [cat, bird, Animal("Generic")]
for animal in animals:
    print(animal.speak())

# ============================================================================
# 5. ENCAPSULATION - PUBLIC, PROTECTED, PRIVATE
# ============================================================================

print("\n" + "="*70)
print("5. ENCAPSULATION")
print("="*70)

class BankAccount:
    """Demonstration of encapsulation"""
    
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public
        self._pin = "1234"  # Protected (convention: single underscore)
        self.__balance = balance  # Private (name mangling with double underscore)
    
    def deposit(self, amount):
        """Public method to deposit money"""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        """Public method to withdraw money"""
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}")
        else:
            print("Invalid withdrawal amount")
    
    def get_balance(self):
        """Public method to check balance"""
        return self.__balance

account = BankAccount("123456", 1000)
print(f"Account: {account.account_number}")
account.deposit(500)
account.withdraw(200)
print(f"Balance: ${account.get_balance()}")

# Trying to access private variable (Python allows it but shouldn't)
print(f"\nName-mangled private variable: {account._BankAccount__balance}")

# ============================================================================
# 6. MAGIC METHODS
# ============================================================================

print("\n" + "="*70)
print("6. MAGIC METHODS")
print("="*70)

class Person:
    """Demonstration of magic methods"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        """Called by str() and print()"""
        return f"Person: {self.name}, Age: {self.age}"
    
    def __repr__(self):
        """Called by repr() - should be unambiguous"""
        return f"Person('{self.name}', {self.age})"
    
    def __len__(self):
        """Called by len()"""
        return len(self.name)
    
    def __eq__(self, other):
        """Called by == operator"""
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False
    
    def __lt__(self, other):
        """Called by < operator"""
        if isinstance(other, Person):
            return self.age < other.age
        return False
    
    def __add__(self, other):
        """Called by + operator"""
        if isinstance(other, Person):
            return f"{self.name} and {other.name}"
        return NotImplemented

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Alice", 30)

print(f"str(): {str(person1)}")
print(f"repr(): {repr(person1)}")
print(f"len(): {len(person1)}")
print(f"person1 == person3: {person1 == person3}")
print(f"person2 < person1: {person2 < person1}")
print(f"person1 + person2: {person1 + person2}")

# ============================================================================
# 7. PROPERTIES AND GETTERS/SETTERS
# ============================================================================

print("\n" + "="*70)
print("7. PROPERTIES AND GETTERS/SETTERS")
print("="*70)

class Temperature:
    """Using @property for getters and setters"""
    
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter for celsius with validation"""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Computed property"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature from Fahrenheit"""
        self._celsius = (value - 32) * 5/9

temp = Temperature(25)
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")

temp.celsius = 30
print(f"Updated Celsius: {temp.celsius}°C")
print(f"Updated Fahrenheit: {temp.fahrenheit}°F")

temp.fahrenheit = 86
print(f"From Fahrenheit - Celsius: {temp.celsius:.2f}°C")

# ============================================================================
# 8. DATACLASSES
# ============================================================================

print("\n" + "="*70)
print("8. DATACLASSES")
print("="*70)

@dataclass
class Student:
    """A dataclass for Student - automatically generates __init__, __str__, __eq__"""
    name: str
    student_id: int
    gpa: float = 0.0
    courses: List[str] = field(default_factory=list)

student1 = Student("John Doe", 12345, 3.8, ["Math", "Physics"])
student2 = Student("Jane Smith", 12346)

print(f"Student 1: {student1}")
print(f"Student 2: {student2}")
print(f"student1 == student2: {student1 == student2}")

student2.courses.append("Chemistry")
print(f"Updated Student 2: {student2}")

# Dataclass with post-init
@dataclass
class Circle:
    """Dataclass with __post_init__"""
    radius: float
    
    def __post_init__(self):
        """Called after __init__"""
        if self.radius <= 0:
            raise ValueError("Radius must be positive")
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def circumference(self):
        return 2 * 3.14159 * self.radius

circle = Circle(5)
print(f"Circle with radius {circle.radius}")
print(f"Area: {circle.area():.2f}")
print(f"Circumference: {circle.circumference():.2f}")

# ============================================================================
# 9. COMPOSITION VS INHERITANCE
# ============================================================================

print("\n" + "="*70)
print("9. COMPOSITION VS INHERITANCE")
print("="*70)

print("\n--- Inheritance Example ---")

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def describe(self):
        return f"{self.make} {self.model}"

class ElectricCar(Vehicle):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity
    
    def describe(self):
        return f"{super().describe()} with {self.battery_capacity}kWh battery"

electric_car = ElectricCar("Tesla", "Model 3", 75)
print(f"Inheritance: {electric_car.describe()}")

print("\n--- Composition Example ---")

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def specs(self):
        return f"{self.horsepower} HP"

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition
    
    def describe(self):
        return f"{self.make} {self.model} with {self.engine.specs()} engine"

my_engine = Engine(150)
my_car = Car("Honda", "Civic", my_engine)
print(f"Composition: {my_car.describe()}")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n" + "="*70)
print("PRACTICE EXERCISES")
print("="*70)

print("""
1. Create a Polygon Class:
   - Base class with vertices (list of points)
   - Calculate perimeter (sum of distances between consecutive vertices)
   - Create subclasses: Triangle, Square, Pentagon
   - Override perimeter calculation if needed
   - Implement magic methods: __str__, __repr__, __len__ (number of vertices)

2. Create a Library System:
   - Book class with title, author, isbn, year_published
   - Library class with collection of books
   - Add methods: add_book, remove_book, find_by_author, find_by_year
   - Track how many times a book has been borrowed
   - Use dataclass for Book

3. Create a Game Character System:
   - Character class with name, health, mana, level
   - Subclasses: Warrior, Mage, Rogue with different attributes
   - Implement magic methods for comparison (< > == for level comparison)
   - Create a Party class (composition) that contains multiple characters
   - Implement methods to calculate total party power

4. Create a Temperature Logger:
   - DataClass with timestamp, celsius value
   - Property to get fahrenheit and kelvin
   - Logger class to store multiple temperatures
   - Methods to get min, max, average temperature
   - Find temperatures within a range

5. Create a Bank System:
   - Account class with private balance
   - Transaction history
   - Methods: deposit, withdraw, transfer
   - Savings and Checking account subclasses with different withdrawal rules
   - Use encapsulation to protect balance
   - Custom exceptions for invalid transactions
""")

print("\n" + "="*70)
print("Module completed successfully!")
print("="*70)
