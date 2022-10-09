class Product:
    def __init__(self, number, price):
        self.number  = number
        self.price  = price

    def get_price(self,newamount):
        if newamount < 10:
            return self.price
        elif 10 <= newamount <= 99:
            return self.price * 0.9 
        elif newamount >= 100:
            return self.price * 0.8

    def make_purchase(self, newnumber):
        if newnumber<self.number:
            self.number = newnumber
            return self.get_price(newnumber) * newnumber
        else:
            return 0

total_amount = 0
banana = Product(20, 1000)
orange = Product(30,800)
apple = Product(40,500)
print(banana.get_price(3))
print(orange.get_price(5))
print(apple.get_price(6)) 
print(banana.make_purchase(51))
total_amount = banana.make_purchase(3) + orange.make_purchase(5) + apple.make_purchase(6)
print(total_amount)

            
