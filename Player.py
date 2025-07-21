# A simple class to represent a Player with a name and level.
# The class overrides the __eq__ method to allow comparison based on attributes rather than object identity.
# -------------------------------------------------------------------------------------------------------------------------------

class Player:
    def __init__(self, name, level):
        """Initialize a Player with a name and level."""
        self.name = name
        self.level = level
    
    # Dunder eq method to compare Player instances:
    # Overrides the default equality check to compare based on attributes.
    def __eq__(self, other):
        """Check if two Player instances are equal based on their attributes."""
        return ((self.name, self.level) == (other.name, other.level))

a = Player("Bob", 5)
b = Player("Bob", 5)

# ---------------------------------------------------------------------------------------------------------------------------------
# Before overriding __eq__, the default behavior would compare object identities.
print(a == b)   # This will print False because a and b are different instances, even though they have the same attributes.

players = [a]
print(b in players) # This will print False because b is not in the players list, even though it has the same attributes as a.
# ---------------------------------------------------------------------------------------------------------------------------------
# After overriding __eq__, the comparison will check the attributes.
print(a == b)   # This will print True because a and b have the same name and level.


print(b in players) # This will print True because b is now considered equal to a based on the overridden __eq__ method.