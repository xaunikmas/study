class Karyawan:
    def __init__(self, inputName, inputJob, inputAdd, inputCity):
        self.name = inputName
        self.job = inputJob
        self.address = inputAdd
        self.city = inputCity

karyawan1 = Karyawan ('niko','software dev', 'rawamangun', 'Jakarta')
karyawan2 = Karyawan ('anunx', 'network engineer', 'bintaro', 'tangsel')
karyawan3 = Karyawan ('rino', 'marketing agent', 'cempaka putih', 'Jakarta')

print (karyawan1.__dict__)
print (karyawan2.__dict__)
print (karyawan3.__dict__)
print ('\n')
    # class Hero:
#     def __init__(self, inputName, inputHealth, inputPower):
#         self.name = inputName
#         self.health = inputHealth
#         self.power = inputPower

# hero1 = Hero ("radvik", 100, 100)
# hero2 = Hero ("komar", 100, 10)
# hero3 = Hero ("otong", 50, 10)

# print (hero1.__dict__)
# print (hero2.__dict__)
# print (hero3.__dict__)

        


programmer = 'niko'
def programmer_makan():
    print ('{} makan nasi'. format(programmer))

guru = 'putri'
def guru_makan():
    print ('{} makan nasi'. format(guru))

engineer = 'anunx'
def engineer_makan():
    print ('{} makan nasi'. format(engineer))

programmer_makan()
guru_makan()
engineer_makan()

def hasil (a, b):
    hasil = (a * b)
    return hasil

print (hasil(5, 10))


