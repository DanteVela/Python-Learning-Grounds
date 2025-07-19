# A simple Python script to demonstrate a Dunder method for a Book class.
# This script defines a Book class with a Dunder method to return a string representation of the Book.
# --------------------------------------------------------------------------------------------------------------------------------

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    # Dunder method to return a string representation of the Book object
    def __str__(self):
        return (f"{self.title} by " f"{self.author}")

# Example usage:
book = Book("1984", "George Orwell")

print(book)     # Output: 1984 by George Orwell