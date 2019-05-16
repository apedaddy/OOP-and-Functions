class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_description(self):
        long_name = str(self.year)+' '+self.make + ' '+self.model
        return long_name.title()

    def read_odometer(self):
        print ("This car has " + str (self.odometer)+" miles on it")

new_car = Car ('toyota', 'avensis', 2016)
new_car.odometer = 53000
print(new_car.get_description())
new_car.read_odometer()