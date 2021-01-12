from order import Order

class TaxableOrder(Order):
    def __init__(self, item_str, price, tax):
        self.__tax = tax
        self.__price = price + (price * tax)
        super().__init__(item_str, self.__price)
