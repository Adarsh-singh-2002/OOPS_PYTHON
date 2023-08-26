class Item:
    pay_rate = 0.8
    def __init__(self,name:str,price:float,quantity=0):
        
        #Run validations to the received arguments
        assert price>=0, f"Price {price} is not greater than zero!"
        assert quantity>=0, f"Quantity {quantity} should be greater than or equal to zero!"

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    

    def apply_discount(self):
        self.price = self.price * self.pay_rate



item1 = Item("Phone",100,5)
item2 = Item("Laptop",1000,3)

print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)

print(Item.__dict__) #All the attributes for class level 
print(item1.__dict__) #All the attributes for instance level

print(item1.name)
print(item1.quantity)
print(item1.price)
print(item2.name)
print(item2.quantity)
print(item2.price)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

item1.apply_discount()
print(item1.price)

item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)
