class CashRegister(object):
    def __init__(self, tax_rate = 0.0):
        self.__tax_rate = tax_rate
        self.__item_list = []
        self.__item_count = 0
    
    def add_item(self, price, is_taxed):
        self.price = price
        self.taxable = is_taxed
        
        self.__item_list.append([self.price, self.taxable])
        self.__item_count += 1
    
    def get_count(self):
        return self.__item_count
    
    def get_total(self):
        self.total_sum = 0.0 
        for element in self.__item_list:
            self.total_sum += element[0]
        return self.total_sum
    
    def get_total_with_tax(self):
        self.total_sum_w_tax = 0.0
        for element in self.__item_list:
            if element[1] == True:
                self.total_sum_w_tax += element[0] * (1 + (self.__tax_rate / 100))
            else:
                self.total_sum_w_tax += element[0]
        return self.total_sum_w_tax
    
    def clear(self):
        self.__item_list.clear()
        self.__item_count = 0
    
    def __str__(self):
        return "Items: {}, total price: {:.2f}, including tax: {:.2f}".format(self.__item_count, self.get_total(), self.get_total_with_tax())

reg1 = CashRegister(7.5)
reg1.add_item(10.0, True)
reg1.add_item(15.5, True)
reg1.add_item(23.3, False)  # The price of the item is 10.0, taxable 
print(reg1)

print(reg1.get_count())
print(reg1.get_total())
print(reg1.get_total_with_tax())

reg1.clear()
print(reg1)