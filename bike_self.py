class Bike(object):
    def __init__(self, price, max_speed, miles = 0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print "This bike's price is {}, it has a maximum speed of {} and miles of {}".format(self.price,self.max_speed, self.miles)
        return self
    def ride(self):
        print "Riding... Miles: {}".format(self.miles+10)
        return self
    def reverse(self):
        print "Reversing... Miles: {}".format(self.miles-5)
        return self

bike = Bike(123,"25mph",4343)
bike.displayInfo().ride().reverse()

bike2 = Bike(123,"25mph")
bike2.displayInfo().ride().reverse()
