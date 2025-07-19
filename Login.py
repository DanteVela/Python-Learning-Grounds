# User Login Database in Python:
# This script is part of a Python module for handling User Login functionality.
# It connects to a SQLite database to verify user credentials.
# -------------------------------------------------------------------------------------------------------------------------------
# Importing necessary libraries
import sqlite3
# -------------------------------------------------------------------------------------------------------------------------------
def login(username, password):
    # Connect to the SQLite database
    conn = sqlite3.connect('Example.db')

    # Create a cursor object to interact with the database
    cursor = conn.cursor()
    
    # ---------------------------------------------------------------------------------------------------------------------------
    # SQL query to check if the User exists with the provided username and password:
    # Note: Using string formatting directly in SQL queries can lead to SQL injection vulnerabilities.
    # cursor.execute(f"SELECT * FROM users " f"WHERE username = '{username}' " f"AND password = '{password}'")
    # cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))

    # Using parameterized query to prevent SQL injection:
    # In production, always use parameterized queries to prevent SQL injection.
    _sql = "SELECT * FROM users WHERE username = ? AND password = ?"
    _parameters = (username, password)
    
    # Execute the query with parameters
    cursor.execute(_sql, _parameters)
    # cursor.execute(_sql: "SELECT * FROM users WHERE " "username = ? AND password = ?", _parameters: (username, password))
    # ---------------------------------------------------------------------------------------------------------------------------
    
    # Fetch the result of the query
    result = cursor.fetchone()

    # Close the database connection
    conn.close()

    # If result is not None, the User exists and credentials are correct
    if result:
        print("Login successful!")
        return result
    else:
        print("Login failed! Invalid username or password.")
        return result