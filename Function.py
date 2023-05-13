def sapa (name, age, address):
    print ('welcome '+ str(name) + ' you are ' + str(age) + ' years old ' + 'and lived in ' + str(address), '\n')

#penggunaan function begini bisa, atau
sapa ('James', 40, 'Jakarta')

#begini juga bisa
sapa (name = 'James', age = 40, address= 'jakarta')


# penggunaan asterix jika kita ingin isi lebih dari 1 argument, dan bisa di spesifikan dengan indexing nya

def halo (*names):
    print ('welcome ' + names[0])

halo ('niko', 'naunx', 'rino')

