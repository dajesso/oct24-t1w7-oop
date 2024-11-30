# Shape base class with an area() method
# Subclasses such as square, circle, triangle, etc...

import math
from abc import ABC, abstractmethod # abstract class

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi *  self.radius * self.radius
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# main
c1 = Circle(7)
print(c1.area())

r1 = Rectangle(5, 10)
print(r1.area())