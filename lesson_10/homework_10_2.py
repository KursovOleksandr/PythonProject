from abc import ABC, abstractmethod
import math


class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Figure):

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Figure):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


class Triangle(Figure):

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def perimeter(self):
        return self.__a + self.__b + self.__c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))


figures = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5)
]

for figure in figures:
    print(f"{figure.__class__.__name__}:")
    print(f"  Площа = {figure.area():.2f}")
    print(f"  Периметр = {figure.perimeter():.2f} \n")