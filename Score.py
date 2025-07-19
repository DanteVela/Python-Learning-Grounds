# A simple class to represent a Score with Addition functionality and a way to Sum multiple scores together.

class Score:
    def __init__(self, points):
        self.points = points

    def __repr__(self):
        return f"Score(points={self.points})"

    def __add__(self, other):
        return Score(self.points + other.points)

a = Score(10)
b = Score(20)

print(a + b)  # Output: Score(points=30)

total = sum([Score(5), Score(15), Score(25)], Score(0))

print(total)  # Output: Score(points=45)