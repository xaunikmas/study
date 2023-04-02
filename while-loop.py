# while loop, pengulangan

nama = ""

while len(nama) == 0:  # kondisi dimana input nama nya kosong, alias sama dengan null, maka akan loop terus meminta input argument nya
    nama = input("enter your name ?   ")  # result :  enter your name ?  

print("your name is " + nama)  # result : your name is niko

# atau pake metode lain, sperti dibawah :

nama = None

while not nama:
    nama = input ("please, enter your name?  ")

print ("your name is " + nama)


import time

hitung = 1
while (hitung < 4):
    print ('...', hitung)
    time.sleep (1)
    hitung = hitung + 1

nama ='Adieu nixau'
print (nama.upper())

# PENGGUNAAN FOR LOOP  #

angka = [1,2,3,4,5]
for x in angka:
    print (x)

buah = ['nanas', 'jambu', 'melon', 'pepaya']

for isi in buah:
    print ('saya suka makan buah',isi, '\n')

print ('saya paling suka dengan buah', buah[3], '\n')
