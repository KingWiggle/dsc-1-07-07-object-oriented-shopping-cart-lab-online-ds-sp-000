class ShoppingCart:
    # write your code here
    def __init__(self, total=0, emp_discount=None):
        self.total = total
        self.employee_discount = emp_discount
        self.items = []
        
    def add_item(self, name, price, quantity=1):
        self.items.append([name, price, quantity])
        self.total += price*quantity
        return self.total
        
    def mean_item_price(self):
        num_items = 0
        for item in self.items:
            num_items += item[2]
        return round(self.total/num_items,2)
    
    def median_item_price(self):
        price_list = []
        for item in self.items:
            for i in range(item[2]):
                price_list.append(item[1])
        price_list.sort()
        if len(price_list) % 2 != 0:
            return price_list[int((len(price_list)-1)/2)]
        else:
            return (price_list[len(price_list)/2]+price_list[(len(price_list)/2)-1])/2

    def apply_discount(self):
        if self.employee_discount:
            return self.total*((100-self.employee_discount)/100)
        else:
            return "Sorry, there is no discount to apply to your cart :("

    def void_last_item(self):
        if self.items[-1][2] == 1:
            self.total -= self.items[-1][1]
            self.items.pop()
        else:
            self.total -= self.items[-1][1]
            self.items[-1][2] -=1
        