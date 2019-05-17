class LineValues:
    def __init__(self, first_cord, second_cord):
        self.first_cord = first_cord
        self.second_cord = second_cord


    def distance(self):

        # Apply formula to calculate distance between two points.
        # How to get values for x1 and y1
        # Using tuple unpacking
        x1,y1 = self.first_cord
        x2,y2 = self.second_cord

        return ((x2-x1)**2 + (y2-y1)**2 )**0.5

    def slope(self):
        # Calculate slope in this method
        x1, y1 = self.first_cord
        x2, y2 = self.second_cord

        return (y2-y1) / (x2-x1)

print ("\nCALCULATE DISTANCE AND SLOPE OF A LINE THAT FORMED FROM TWO CO-ORDINATE VALUE")
print ("Examples............")
print ("Start = (2,4)")
print ("End = (1,3)")
c1 = (2,4)
c2 = (1,3)
myline = LineValues(c1,c2)
print("\nDistance of line formed in given two co-ordinates {}".format(myline.distance()))
print("Slope of line formed in given two co-ordinates {}".format(myline.slope()))




