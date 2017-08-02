class Bike(object):
    
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
        
    def displayInfo(self):
        print "${}, top speed {}, miles ridden {}".format(self.price, self.max_speed, self.miles)

    def ride(self):
        self.miles += 10
        print "Riding {} miles".format(self.miles)
        return self
    
    def reversing(self):
        if self.miles == 0:
            print "Cannot Reverse already at 0 miles"
            return self
        else:
            self.miles -=5
            print "Reversing {} miles".format(self.miles)
        return self

bike1 = Bike(200, "25mph")
bike1.ride().ride().ride().reversing().displayInfo()

bike2 = Bike(300, "30mph")
bike2.ride().ride().reversing().reversing().displayInfo()

bike3 = Bike(1000, "45mph")
bike3.reversing().reversing().reversing().displayInfo()


