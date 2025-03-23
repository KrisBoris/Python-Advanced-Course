# Example 51 - Polymorphism

from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1415926535 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Cube(Square):
    def __init__(self, side):
        super().__init__(side)

    def area(self):
        return 6 * self.side ** 2


class RubikCube(Cube):
    def __init__(self, side):
        super().__init__(side)


shapes = [Circle(4), Square(4), Cube(5), RubikCube(5)]
for shape in shapes:
    print(f"Area = {shape.area()} cm^2")
