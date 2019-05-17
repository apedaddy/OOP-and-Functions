class AreaOfRectangle():
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
print ("\nPRINT AREA OF RECTANGLE FROM GIVEN LENGTH AND BREADHT VALUE")
l = int(input("Enter value of length: "))
b = int(input("Enter value of breadth: "))
calc_area = AreaOfRectangle(l,b)
print (f"Area of given rectangle is: {calc_area.area()}")