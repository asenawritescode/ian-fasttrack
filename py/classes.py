class Coordinate():
    def __init__(self, input_x, input_y):
        self.x = input_x
        self.y = input_y

p = Coordinate(3, 4)
print(f"This is the x value -> {p.x}")
print(f"This is the y value -> {p.y}")

# New Object dont have "new" keyword
# self is like "this" in Java, a ref to the object itself
# self is the first parameter of every method in a class
# Dot natation to get instance variables
# __init__ is a constructor, what happens when you create a new object