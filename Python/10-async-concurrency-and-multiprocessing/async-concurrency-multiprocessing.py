"""
Async, Concurrency, and Multiprocessing - Parallel Programming

This module covers concurrent and parallel programming in Python:
- Threading basics
- Threading locks and synchronization
- Multiprocessing concept
- async/await syntax
- Concurrency patterns
- Performance considerations
"""

import threading
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from queue import Queue

# ============================================================================
# 1. THREADING BASICS
# ============================================================================

print("\n" + "="*70)
print("1. THREADING BASICS")
print("="*70)

print("\n--- What is Threading? ---")
print("""
Threading allows multiple tasks to run concurrently (not in parallel)
within the same process. Good for I/O-bound tasks.

Characteristics:
- Multiple threads share the same memory
- Lighter weight than processes
- Subject to Python's Global Interpreter Lock (GIL)
- Good for I/O operations (network, file)
- NOT good for CPU-intensive tasks
""")

print("\n--- Creating Threads ---")

def print_numbers(name: str, count: int) -> None:
    """Function to run in a thread"""
    for i in range(count):
        print(f"  {name}: {i}")
        time.sleep(0.1)

print("Sequential execution (without threading):")
start = time.time()
print_numbers("Task1", 2)
print_numbers("Task2", 2)
elapsed = time.time() - start
print(f"Took {elapsed:.2f} seconds\n")

print("Concurrent execution (with threading):")
start = time.time()

thread1 = threading.Thread(target=print_numbers, args=("Thread1", 2))
thread2 = threading.Thread(target=print_numbers, args=("Thread2", 2))

thread1.start()
thread2.start()

thread1.join()  # Wait for thread1 to complete
thread2.join()  # Wait for thread2 to complete

elapsed = time.time() - start
print(f"\nTook {elapsed:.2f} seconds")

print("\n--- Threading with Class ---")

class CounterThread(threading.Thread):
    """Custom thread class"""
    
    def __init__(self, name: str, start: int, end: int):
        super().__init__()
        self.name = name
        self.start_val = start
        self.end_val = end
    
    def run(self) -> None:
        """This method runs when thread starts"""
        for i in range(self.start_val, self.end_val):
            print(f"  {self.name}: {i}")
            time.sleep(0.1)

print("Using custom thread class:")
thread1 = CounterThread("Counter1", 0, 3)
thread2 = CounterThread("Counter2", 100, 103)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# ============================================================================
# 2. THREAD SYNCHRONIZATION AND LOCKS
# ============================================================================

print("\n" + "="*70)
print("2. THREAD SYNCHRONIZATION AND LOCKS")
print("="*70)

print("\n--- Race Condition (Without Lock) ---")

counter = 0

def increment_counter_unsafe(iterations: int) -> None:
    """Increment counter without synchronization"""
    global counter
    for _ in range(iterations):
        temp = counter
        temp += 1
        counter = temp

print("Race condition demonstration (without lock):")
counter = 0
thread1 = threading.Thread(target=increment_counter_unsafe, args=(100,))
thread2 = threading.Thread(target=increment_counter_unsafe, args=(100,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(f"Counter value: {counter} (should be 200 but likely less due to race condition)")

print("\n--- Using Lock to Prevent Race Condition ---")

counter = 0
counter_lock = threading.Lock()

def increment_counter_safe(iterations: int) -> None:
    """Increment counter with lock"""
    global counter
    for _ in range(iterations):
        with counter_lock:  # Acquire lock
            temp = counter
            temp += 1
            counter = temp
            # Lock automatically released when exiting with block

print("\nSafe incrementing (with lock):")
counter = 0
thread1 = threading.Thread(target=increment_counter_safe, args=(100,))
thread2 = threading.Thread(target=increment_counter_safe, args=(100,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(f"Counter value: {counter} (should be 200)")

print("\n--- RLock (Reentrant Lock) ---")

class BankAccount:
    """Bank account with reentrant lock"""
    
    def __init__(self, balance: float):
        self.balance = balance
        self.lock = threading.RLock()
    
    def withdraw(self, amount: float) -> bool:
        """Withdraw with lock"""
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"  Withdrew ${amount}, balance: ${self.balance}")
                return True
            return False
    
    def transfer(self, other: 'BankAccount', amount: float) -> bool:
        """Transfer between accounts - needs to acquire lock twice"""
        with self.lock:
            if self.withdraw(amount):  # This also acquires lock
                other.deposit(amount)
                return True
            return False
    
    def deposit(self, amount: float) -> None:
        """Deposit with lock"""
        with self.lock:
            self.balance += amount
            print(f"  Deposited ${amount}, balance: ${self.balance}")

print("\nBank account operations with RLock:")
account1 = BankAccount(100)
account2 = BankAccount(50)
account1.transfer(account2, 25)

# ============================================================================
# 3. THREAD POOL AND FUTURES
# ============================================================================

print("\n" + "="*70)
print("3. THREAD POOL AND FUTURES")
print("="*70)

print("\n--- ThreadPoolExecutor ---")

def long_running_task(n: int) -> int:
    """Simulate long-running task"""
    print(f"  Task {n} starting")
    time.sleep(0.5)
    print(f"  Task {n} completed")
    return n * 2

print("Using ThreadPoolExecutor:")
with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit tasks
    futures = [executor.submit(long_running_task, i) for i in range(5)]
    
    # Get results as they complete
    for future in futures:
        result = future.result()
        print(f"  Result: {result}")

print("\n--- Using map with ThreadPoolExecutor ---")

def square(n: int) -> int:
    return n ** 2

print("Using executor.map():")
with ThreadPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(square, range(5)))
    print(f"Squares: {results}")

# ============================================================================
# 4. MULTIPROCESSING BASICS
# ============================================================================

print("\n" + "="*70)
print("4. MULTIPROCESSING BASICS")
print("="*70)

print("""
Multiprocessing vs Threading:

Threading:
- Shared memory space
- Lighter weight
- Subject to GIL
- Good for I/O-bound tasks
- Easier to coordinate

Multiprocessing:
- Separate memory spaces
- Heavier weight
- No GIL restriction
- Good for CPU-bound tasks
- Harder to share data

When to use each:
- I/O-bound (network, file): Use Threading
- CPU-bound (calculations): Use Multiprocessing
- Mixed workload: Consider both or async
""")

print("\n--- Multiprocessing Example Concept ---")
print("""
from multiprocessing import Process, Queue

def worker(queue, name):
    result = expensive_calculation()
    queue.put((name, result))

if __name__ == '__main__':
    queue = Queue()
    processes = []
    
    for i in range(4):
        p = Process(target=worker, args=(queue, f'Worker-{i}'))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()
    
    while not queue.empty():
        name, result = queue.get()
        print(f"{name}: {result}")
""")

# ============================================================================
# 5. ASYNC/AWAIT SYNTAX
# ============================================================================

print("\n" + "="*70)
print("5. ASYNC/AWAIT SYNTAX")
print("="*70)

print("\n--- Understanding Async ---")
print("""
asyncio is Python's library for asynchronous I/O.
Good for high-concurrency I/O operations (not CPU-bound).

Key concepts:
- Coroutines: Functions defined with async def
- await: Pause execution, let other tasks run
- Event loop: Manages and runs coroutines
- Tasks: Scheduled coroutines
""")

print("\n--- Basic Async Example ---")

async def async_task(name: str, delay: int) -> None:
    """Async task that waits"""
    print(f"  {name} started")
    await asyncio.sleep(delay)
    print(f"  {name} completed")

async def main_concurrent() -> None:
    """Run multiple tasks concurrently"""
    print("Running async tasks:")
    start = time.time()
    
    # Create tasks
    task1 = asyncio.create_task(async_task("Task1", 1))
    task2 = asyncio.create_task(async_task("Task2", 1))
    task3 = asyncio.create_task(async_task("Task3", 1))
    
    # Wait for all tasks
    await asyncio.gather(task1, task2, task3)
    
    elapsed = time.time() - start
    print(f"All tasks completed in {elapsed:.2f} seconds")

print("Sequential would take ~3 seconds, async takes ~1 second:")
asyncio.run(main_concurrent())

print("\n--- Async with Return Values ---")

async def fetch_data(source: str, delay: float) -> str:
    """Simulate fetching data"""
    print(f"  Fetching from {source}")
    await asyncio.sleep(delay)
    return f"Data from {source}"

async def gather_data() -> None:
    """Gather data from multiple sources"""
    print("Fetching data from multiple sources:")
    
    results = await asyncio.gather(
        fetch_data("Source1", 0.5),
        fetch_data("Source2", 0.3),
        fetch_data("Source3", 0.4)
    )
    
    for result in results:
        print(f"  {result}")

asyncio.run(gather_data())

print("\n--- Async Exception Handling ---")

async def risky_async_task(should_fail: bool) -> str:
    """Async task that might fail"""
    await asyncio.sleep(0.2)
    if should_fail:
        raise ValueError("Task failed!")
    return "Success"

async def handle_exceptions() -> None:
    """Handle exceptions in async tasks"""
    print("Handling async exceptions:")
    
    try:
        result = await risky_async_task(False)
        print(f"  Result: {result}")
    except ValueError as e:
        print(f"  Caught exception: {e}")
    
    try:
        result = await risky_async_task(True)
    except ValueError as e:
        print(f"  Caught exception: {e}")

asyncio.run(handle_exceptions())

# ============================================================================
# 6. CONCURRENCY PATTERNS
# ============================================================================

print("\n" + "="*70)
print("6. CONCURRENCY PATTERNS")
print("="*70)

print("\n--- Producer-Consumer Pattern ---")

queue = Queue()

def producer_thread() -> None:
    """Produce items"""
    for i in range(5):
        print(f"  Producer: Putting item {i}")
        queue.put(i)
        time.sleep(0.1)

def consumer_thread() -> None:
    """Consume items"""
    while True:
        item = queue.get()
        if item is None:  # Sentinel value
            break
        print(f"    Consumer: Got item {item}")
        queue.task_done()

print("Producer-Consumer with Queue:")
producer = threading.Thread(target=producer_thread)
consumer = threading.Thread(target=consumer_thread)

consumer.start()
producer.start()

producer.join()
queue.put(None)  # Signal consumer to stop
consumer.join()

print("\n--- Rate Limiting Pattern ---")

class RateLimiter:
    """Rate limiter for concurrent operations"""
    
    def __init__(self, max_per_second: int):
        self.max_per_second = max_per_second
        self.lock = threading.Lock()
        self.last_reset = time.time()
        self.count = 0
    
    def acquire(self) -> None:
        """Wait if rate limit exceeded"""
        with self.lock:
            now = time.time()
            if now - self.last_reset >= 1.0:
                self.last_reset = now
                self.count = 0
            
            if self.count >= self.max_per_second:
                time.sleep(1.0 - (now - self.last_reset))
            
            self.count += 1

# ============================================================================
# 7. PERFORMANCE CONSIDERATIONS
# ============================================================================

print("\n" + "="*70)
print("7. PERFORMANCE CONSIDERATIONS")
print("="*70)

print("""
Performance Guidelines:

Threading (I/O-bound):
✓ Network requests
✓ File operations
✓ Database queries
✗ CPU-intensive calculations

Multiprocessing (CPU-bound):
✓ Numerical computations
✓ Data processing
✓ Image manipulation
✗ Frequent inter-process communication

Async/await (I/O-bound, high concurrency):
✓ Web server handling many clients
✓ Many concurrent I/O operations
✓ Best for modern Python async libraries
✗ CPU-bound tasks
✗ Blocking operations

GIL (Global Interpreter Lock):
- Python's GIL prevents true parallel execution of Python bytecode
- Multiple threads can't run Python code simultaneously
- One thread at a time executes Python bytecode
- I/O operations release the GIL
- Multiprocessing bypasses the GIL

Benchmarking:
- Use time.time() or time.perf_counter()
- Run multiple times to get average
- Disable other processes
- Profile with cProfile for details
""")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n" + "="*70)
print("PRACTICE EXERCISES")
print("="*70)

print("""
1. Threading Exercise:
   - Create multiple threads that print messages
   - Use locks to synchronize access to shared resource
   - Implement thread-safe counter class
   - Compare with and without locks
   - Demonstrate race condition

2. Thread Pool Exercise:
   - Use ThreadPoolExecutor for parallel tasks
   - Submit multiple jobs and collect results
   - Implement timeout handling
   - Map function over list using thread pool
   - Compare performance

3. Async/Await Exercise:
   - Write multiple async functions
   - Use asyncio.gather() for concurrent execution
   - Implement async context manager
   - Handle exceptions in async tasks
   - Compare async vs synchronous performance

4. Concurrent Patterns:
   - Implement producer-consumer pattern
   - Implement thread pool with queue
   - Implement rate limiter
   - Test with multiple concurrent operations
   - Monitor resource usage

5. Performance Comparison:
   - Create CPU-bound and I/O-bound tasks
   - Benchmark sequential execution
   - Benchmark with threading
   - Benchmark with multiprocessing (if applicable)
   - Benchmark with async
   - Document findings
""")

print("\n" + "="*70)
print("Module completed successfully!")
print("="*70)
