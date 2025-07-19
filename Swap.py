# A simple Python script to demonstrate a No-Swap and other Swap operations.
# This script shows how to perform a No-Swap operation using arithmetic operations.
# This script also includes various methods for swapping values in Python.
# --------------------------------------------------------------------------------------------------------------------------------

def main():
    a = 99
    b = 13

    # Print the values before any operation
    print(f"Before swap: a = {a}, b = {b}")

    # Perform a Swap operation using arithmetic operations:
    # No-Swap operation is performed
    a = a * b
    b = a / b
    a = a / b

    # Print the values after the No-Swap operation
    # Convert numbers to string for display
    print("\na = " + str(int (a)) + ", b = " + str(int (b)))

def tuple_swap(a, b):
    # Tuple Unpacking
    a, b = b, a

def variable_swap(a, b):
    # Temporary Variable - 30% slower than Tuple Unpacking
    tmp = a
    a = b
    b = tmp

def xor_swap(a, b):
    # XOR Swap - Only works for integers
    a ^= b
    b ^= a
    a ^= b

def in_place_swap(list):
    # In-Place List Element Swap - Leverages Tuple Unpacking on List elements
    list = [1, 2, 3]
    list[0], list[2] = list[2], list[0]

def extended_unpacking_swap(a, b, c):
    # Extended Unpacking for Multiple Swaps
    # a, b, c = 1, 2, 3
    a, b, c = c, a, b
    # Now a==3, b==1, c==2

    # Tuple unpacking	    Performance: 76 ns
    # Temporary variable	Performance: 106 ns
    # XOR swap	            Performance: 145 ns

if __name__ == "__main__":
    main()