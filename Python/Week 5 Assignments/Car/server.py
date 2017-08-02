class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.Price = price
        self.Speed = speed
        self.Fuel = fuel
        self.Mileage = mileage
        self.Tax = 0

    def display_all(self):
        if self.Price > 10000:
            self.Tax = 0.15
        else:
            self.Tax = 0.12
        
        print "Price: {}".format(self.Price)
        print "Speed: {}".format(self.Speed)
        print "Fuel: {}".format(self.Fuel)
        print "Mileage: {}".format(self.Mileage)
        print "Tax: {}".format(self.Tax)

car1 = Car(2000, "35mph", "Full", "15mpg")
car1.display_all()

car2 = Car(2000, "5mph", "Not Full", "105mpg")
car2.display_all()

car3 = Car(2000, "15mph", "Kind of Full", "95mpg")
car3.display_all()

car4 = Car(2000, "25mph", "Full", "255mpg")
car4.display_all()

car5 = Car(2000, "45mph", "Empty", "25mpg")
car5.display_all()

car6 = Car(20000000, "35mph", "Empty", "15mpg")
car6.display_all()