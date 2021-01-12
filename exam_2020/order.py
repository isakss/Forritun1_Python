class Order(object):
    def __init__(self, item_str="", price=0.0):
        self.__item = item_str
        self.__price = price

    def item(self):
        return self.__item
    
    def price(self):
        return self.__price

    def __gt__(self, other):
        return self.__price > other.__price
    
    def __add__(self, other):
        result = Order()
        result.__item = self.__item + "+" + other.__item
        result.__price = self.__price + other.__price
        return result
    
    def __str__(self):
        return "Item: {}, price: {}".format(self.__item, self.__price)
