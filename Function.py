def hay (nama, umur):
    print ('welcome ' + nama, 'you are', umur, 'years old', '\n')

#penggunaan function begini bisa, atau
hay ('niko', 40)

#begini
hay (nama = 'niko', umur = 40)


# penggunaan asterix jika kita ingin isi lebih dari 1 argument, dan bisa di spesifikan dengan indexing nya
def halo (*names):
    print ('welcome back ', names, '\n')

halo ('niko', 'naunx', 'rino')


def sapa (nama, umur, alamat):
    print ('welcome, ' + 'your name is ' + str(nama) + ', your age is ' + str(umur) + ' & lived in ' + str(alamat))

nama = input ('please enter your name? ')
umur = input ('enter your age ')
alamat = input ('enter your address ')

sapa (nama, umur, alamat)


