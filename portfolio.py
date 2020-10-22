class Stock(object):
    def __init__(self, symbol_str='', shares=0):
        self.value = symbol_str + ": " + str(shares)
    
    def __str__(self):
        return str(self.value)

class Portfolio(object):
    def __init__(self, portfolio_value=[]):
        self.value = list(portfolio_value)
    
    def add(self, value):
        self.value.append(value)
    
    def __str__(self):
        return str("\n".join([str(x) for x in self.value]))

stock1 = Stock('IBM', 100)
print(stock1)
stock2 = Stock('GOOG', 200)
stock3 = Stock('AMZN', 500)

portfolio = Portfolio()
portfolio.add(stock1)
portfolio.add(stock2)
portfolio.add(stock3)
print()
print(portfolio)

