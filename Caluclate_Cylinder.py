class Cylinder:
    # height and radius set to 1 as default value
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height *3.14 *(self.radius)**2

    def surface_area(self):
        top = 3.14 * (self.radius**2)
        return (2*top)+ (2*3.14*self.radius*self.height)

height = int(input("Enter value for height: "))
radius = int(input("Enter value for radius: "))

calc_cylinder = Cylinder(height, radius)
print("\nVolume of given cylinder is {}".format(calc_cylinder.volume()))
print("Surface area of given cylinder is {}".format(calc_cylinder.surface_area()))
