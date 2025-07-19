# This script demonstrates a simple implementation of the Fibonacci sequence using Recursion.
# It includes both a basic version and an optimized version using Memoization.
# -------------------------------------------------------------------------------------------------------------------------------
# Importing necessary libraries
from functools import lru_cache

# Fibonacci sequence implementation
# This function computes the nth Fibonacci number using Recursion.
# This is not optimized for performance and is intended for educational purposes.
def old_fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return old_fib(n - 1) + old_fib(n - 2)
# -------------------------------------------------------------------------------------------------------------------------------
# Fibonacci sequence implementation with Memoization
# This function computes the nth Fibonacci number using Recursion with Memoization for improved performance.
# It uses the lru_cache decorator to cache results of previous computations.
# This significantly speeds up the calculation for larger values of n.
@lru_cache
def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
# -------------------------------------------------------------------------------------------------------------------------------
if input("Do you want to run the old Fibonacci sequence? (yes/no): ").strip().lower() == 'yes':
    print("Running old Fibonacci sequence:")
    for i in range(0, 40):
        print(f'{i}: {old_fib(i)}')                                         # This will print Fibonacci numbers from 0 to 39                                                             # Example call to trigger the computation
elif input("Do you want to run the optimized Fibonacci sequence with memoization? (yes/no): ").strip().lower() == 'yes':
    print("Running optimized Fibonacci sequence with memoization:")
    for i in range(0, 100):
        print(f'{i}: {fib(i)}')                                             # This will print Fibonacci numbers from 0 to 99
else:
    print("No Fibonacci sequence will be run.")