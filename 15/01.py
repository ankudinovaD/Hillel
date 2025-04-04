import math

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return round(self.width * self.height)

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        return Rectangle.from_area(self.get_square() + other.get_square())


    def __mul__(self, n):
        return Rectangle.from_area(self.get_square() * n)

    def __str__(self):
        return f"Rectangle({self.width} x {self.height}) - Area: {self.get_square()}"

    @classmethod
    def from_area(cls, area):
        side = math.sqrt(area)
        return cls(round(side, 5), round(side, 5))


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'


r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'