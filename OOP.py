# class Karyawan:
#     def __init__(self, inputName, inputJob, inputAdd, inputCity):
#         self.name = inputName
#         self.job = inputJob
#         self.address = inputAdd
#         self.city = inputCity
        
# karyawan1 = Karyawan ('niko','software dev', 'rawamangun', 'Jakarta')
# karyawan2 = Karyawan ('anunx', 'network engineer', 'bintaro', 'tangsel')
# karyawan3 = Karyawan ('rino', 'marketing agent', 'cempaka putih', 'Jakarta')

# print (karyawan1.__dict__)
# print (karyawan2.__dict__)
# print (karyawan3.__dict__)

##### CONSTRUCTOR ######

class Item:
    def __init__(self, name, type, price, quantity):
        
        self.name = name
        self.type = type
        self.price = price
        self.quantity = quantity

    def totalHarga(self):
        return self.price * self.quantity
    
item1 = Item('phone', 'smartphone', 1000, 10)
print (f'total harga dan jumlah smartphone:', item1.totalHarga())
        
item2 = Item('laptop', 'macbook', 2000, 10)
print (f'total harga dan jumlah laptop macbook:', item2.totalHarga())

print (item1.__dict__)
