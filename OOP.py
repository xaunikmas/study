class Item:
    pay_rate = 0.8  # DISCOUNT 20%
    def __init__(self, name: str, brand: str, price: float, quantity):
    
        # RUN VALIDATIONS TO THE RECEIVED ARGUMENT
        assert price >= 0, f'price {price} must greater than 0'
        assert quantity >= 0, f'Quantity {quantity} must greater than 0'

        # ASSIGN TO SELF OBJECT
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity

    def diskon (self):
        self.price = self.price * Item.pay_rate    
        
item1 = Item ('laptop', 'HP', 7900, 5)
item1.diskon()

item2 = Item ('chromebook', 'Dell', 8500, 5)
item2.diskon()

item3 = Item ('smartphone', 'Apple', 13000, 10)
item3.diskon()

item4 = Item ('smartphone', 'Samsung', 4500, 100)
item4.diskon()

item5 = Item ('smartphone', 'Redmi', 3000, 100)
item5.diskon()

item6 = Item ('smartphone', 'Oppo', 3100, 200)
item6.diskon()

item7 = Item ('smartphone', 'Xiaomi',3200, 100)
item7.diskon()

print (item1.__dict__)
