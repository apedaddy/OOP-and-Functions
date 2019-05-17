import math
#or assign value of pi as pi = 3.14
class Circle():
    # value of radius is required to calculate area and perimeter of the circle
    def __init__(self, radius = 1):
        self.radius = radius
    def area (self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2 * math.pi * self.radius


radius = int(input("\nEnter value of the radius: "))
mycircle = Circle(4)
# if mycircle = Circle(), default value of radius will be 1

print (f"Area of circle is: {mycircle.area()}")
print (f"Perimeter of the circle is: {mycircle.perimeter()}")
