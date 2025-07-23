# A simple Python script using dataclasses to showcase the Person class with or without negative Age check.
# -------------------------------------------------------------------------------------------------------------------------------
from dataclasses import dataclass

@dataclass
class FakePerson:
    name: str
    age: int

bob = FakePerson("Bob", -30)        # Age can't be negative
print(bob)                          # Still prints due to Age being negative
# ------------------------------------------------------------------------------------------------------------------------------
@dataclass
class Person:
    name: str
    age: int
    
    # Checks if Age is negative then prints an ValueError statement
    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age can't be negative")

try:
    bob = Person("Bob", -30)
    print(bob)
except ValueError as e:
    print(e)