# PortScanner in Python: 
# This script scans a range of ports on a specified IP address to check if they are Open or Closed.
# It uses the socket library to attempt connections to each port in the specified range.
# --------------------------------------------------------------------------------------------------------------------------------
# WARNING: Unauthorized port scanning can be illegal and unethical. This code is provided for educational purposes only.
# DISCLAIMER: DO NOT EXECUTE THIS CODE AGAINST ANY SYSTEM WITHOUT PERMISSION.
# All actions taken with this code is the sole responsibility of the user.
# --------------------------------------------------------------------------------------------------------------------------------
# Importing the necessary library
import socket

# IP address input from the user
ip = input("Enter the IP address to scan: ")

for port in range(1, 4000):                                         # Scanning ports from 1 to 4000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        if not s.connect_ex((ip, port)):                            # If connect_ex returns 0, the port is Open
            print(f"Port {port} is open on {ip}")
        else:
            print(f"Port {port} is closed on {ip}")                 # If connect_ex returns a non-zero value, the port is Closed

print("Port scanning completed.")