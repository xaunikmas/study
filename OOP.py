class Item:
    pay_rate = 0.8  # INI ADALAH DISCOUNT 20%
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
        
item1 = Item ('laptop', 'HP', 1000, 5)
item1.diskon()

item2 = Item ('chromebook', 'Dell', 100, 5)
item2.diskon()

item3 = Item ('smartphone', 'Apple', 1000, 10)
item3.diskon()

item4 = Item ('smartphone', 'Samsung', 500, 100)
item4.diskon()

item5 = Item ('smartphone', 'Redmi', 200, 100)
item5.diskon()

item6 = Item ('smartphone', 'Oppo', 300, 200)
item6.diskon()

item7 = Item ('smartphone', 'Xiaomi', 200, 100)
item7.diskon()

print (item1.__dict__)
