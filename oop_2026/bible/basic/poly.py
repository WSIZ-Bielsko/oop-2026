# base class
import math


class Shape:
    def __init__(self):
        pass

    def get_area(self) -> float:
        pass


# derived class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self) -> float:
        return 1.0 * self.width * self.height


class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)
        self.width = width

    # not needed -- will follow from super()


class Ellipse(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self) -> float:
        return self.a * self.b * 3.14159


class Circle(Ellipse):
    def __init__(self, radius):
        super().__init__(radius, radius)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self) -> float:
        # Calculate semi-perimeter
        s = (self.a + self.b + self.c) / 2

        # Calculate area using Heron's formula
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

        return area


if __name__ == '__main__':
    rec = Rectangle(1, 2)
    print(rec.get_area())

    tri = Triangle(3, 4, 5)
    print(tri.get_area())

    sq = Square(3)
    print(sq.get_area())  # works -> 9
