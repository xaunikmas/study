def salam (nama, umur, alamat):
    print ('welcome ' + nama, 'you are '+ str(umur), 'and you lived in '+ alamat, '\n')
salam ('niko', 40, 'jakarta')

# ATAU BISA MENGGUNAKAN FORMAT BEGINI

def regarde (nama, umur, alamat, pekerjaan):
    print ('halo '+ nama, 'kamu berumur '+str(umur), 'tahun, dan kamu tinggal di '+ alamat, 'pekerjaanmu '+ pekerjaan)


#  BIAR LEBIH INTERAKTIF, MENGGUNAKAN INPUT DARI USER

nama = input ('masukkan nama mu ')
umur = int(input('masukkan umur mu '))
alamat = input ('dimana kamu tinggal? ')
pekerjaan = input ('apa pekerjaanmu? ')

regarde (nama, umur, alamat, pekerjaan)


# # MENGGUNAKAN LEBIH DARI 1 ARGUMENT/NILAI

def greet (*names):
    print ('halo ', names[1], 'selamat datang di channel kami')

greet ('niko', 'rino', 'naunx')


# FUNGSI RETURN

def angka (nom1, nom2):
    return nom1 / nom2

nom1 = int(input('masukkan angka '))
nom2 = int(input('masukkan angka '))

print ('hasil dari return adalah = ', angka(nom1, nom2))

def hay (nama, umur):
    print ('welcome ' + nama, 'you are', umur, 'years old', '\n')

#penggunaan function begini bisa, atau
hay ('niko', 40)

# THIS
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



# RETURN FUNCTION
def kali (num1, num2):
    print ('your result is = ')
    return num1 * num2

num1 = int(input('masukkan nomer yang anda pilih '))
num2 = int(input('masukkan nomer yang anda pilih '))

print (kali(num1, num2))