# membuat logika 

""" angka kurang dari 3 jadi true, dan angka diatas 10 jadi true"""

inputAngka = float(input("masukkan angka lebih dari 3\ndan\nkurang dari 10 : "))

# isKurangDari = (inputAngka < 3)
# print ("angka ini", inputAngka, "kurang dari 3 =", isKurangDari)

# isLebihDari = (inputAngka > 10)
# print ("angka ini", inputAngka, "lebih dari 10 =", isLebihDari)

isLebihDari = (inputAngka > 3)
print ("angka ini", inputAngka, "lebih dari 3 = ", isLebihDari)

isKurangDari = (inputAngka < 10)
print ("angka ini :", inputAngka, "kurang dari 10 =", isKurangDari)
