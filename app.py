nama = input ('masukkan namamu ')
umur = int(input ('masukkan tahun lahir '))
skarang = 2023 - umur

print (f"namamu {nama}, usiamu saat ini {skarang}")


kalimat = ['ba','bi', 'bu', 'be', 'bo']

for isi in kalimat:
    if isi == 'be':
        break
    print (isi)
    
import time

for o in range (5, 0, -1):
    print (o)
    time.sleep (0.5)
print ('nixau busted!! ')


kaimat = input ('silakan masukkan kalimat ')
kaimat2 = input ('masukkan kalimat yg akan diganti ')
kaimat3 = input ('masukkan kalimat pengganti ')

print (kaimat.replace(kaimat2, kaimat3))

kursus = 'python, java, php, cplusplus'
belajar = 'java'
print (belajar in kursus)
