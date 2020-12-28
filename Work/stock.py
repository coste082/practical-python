from typedproperty import String, Integer, Float

class Stock:
    '''
    Class for stock holdings.
    '''
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price

    def sell(self,sell_amount):
        self.shares = self.shares - sell_amount

    def update_prices(self,current_price):
        self.current_price = current_price
        self.change = round(self.current_price - self.price,2)

    def __repr__(self):
        return 'Stock({},{},{})'.format(self.name,self.shares,self.price)
