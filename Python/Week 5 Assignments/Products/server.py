class product(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def tax(self):
        taxed = self.price * .09
        self.price = taxed + self.price
        return self
    
    def returned(self, reason):
        if reason == "defective":
            self.status = "Defective"
            self.price = 0
            return self
        elif reason == "returned_box":
            self.status = "Like New"
            return self
        elif reason == "opened_box":
            self.status = "used"
            discount = self.price * .2
            self.price = self.price - discount
            return self
        else:
            print "If returning please use 'defective', 'returned_box', 'opened_box'"
            return self
    
    def display_info(self):
        print "Price: {}, Brand: {}, Item Name: {}, Weight: {}, Cost: {} Status: {}".format(self.price, self.brand, self.item_name, self.weight, self.cost, self.status)
    

iphone = product(850, "Iphone", "2lbs", "Apple", 100)

iphone.returned("opened_box").display_info()