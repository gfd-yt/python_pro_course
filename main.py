class Rectangle:

    def __init__(self, width: int | float, length: int | float):
        if not isinstance(width, (int, float)):
            raise TypeError()

        if not isinstance(length, (int, float)):
            raise TypeError()

        if width <= 0 or length <= 0:
            raise ValueError()

        self.w = width
        self.length = length

    def area(self):
        return self.w * self.length

    def __add__(self, other):
        return self.area() + other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return self.area() < other.area()

        if isinstance(other, tuple) and len(other) == 2:
            a, b = other
            return self.area() < a * b

        return NotImplemented

    def __eq__(self, other):

        if not isinstance(other, Rectangle):
            raise TypeError()

        return self.area() == other.area()

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented

        tmp = self.area() * other
        return Rectangle(1, tmp)

    def __str__(self):
        return f'{self.length} x {self.length}'


r1 = Rectangle(2, 6.5)
r2 = Rectangle(3.5, 3)

print(r1 + r2)
print(r1 > r2)
print(r1 * 2)
print(r1 == r2)


# ***********************************************************************************************

