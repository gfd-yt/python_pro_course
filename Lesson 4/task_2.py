import math


class Rational:

    def __init__(self, a, b):

        if not isinstance(a, int):
            raise TypeError()
        if not isinstance(b, int):
            raise TypeError()
        if not b:
            raise ZeroDivisionError()

        self.__a = a
        self.__b = b

    @property
    def a(self):
        tmp = math.gcd(self.__a, self.__b)
        self.__a = self.__a // tmp
        self.__b //= tmp
        return self.__a

    @property
    def b(self):
        tmp = math.gcd(self.__a, self.__b)
        self.__a //= tmp
        self.__b //= tmp
        return self.__b

    def __add__(self, other):

        if isinstance(other, Rational):
            b = self.__b * other.__b
            a = other.__b * self.__a + self.__b * other.__a

            return Rational(a, b)

    def __str__(self):
        if not self.a:
            return f'0'
        elif self.b == 1:
            return f'{self.a}'
        elif self.a == self.b:
            return f'{self.a} // {self.b}'

        return f'{self.a} / {self.b}'


x = Rational(1, 2)
y = Rational(2, 3)
d = Rational(1, 3)
z = x + y + d
print(z)
