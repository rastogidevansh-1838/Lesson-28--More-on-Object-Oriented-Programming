import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
user_input = float(input("Enter the radius of the circle: "))
my_circle = Circle(user_input)
print("Area:", my_circle.area())
print("Perimeter:", my_circle.perimeter())