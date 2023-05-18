coba = 0
rahasia = 4
limit = 3

while coba < limit:
    masuk = int(input('masukkan angka [1 -9] (tebak angka rahasia: ) '))
    if masuk == rahasia:
        print ('selamat, anda menang ')
    coba = coba +1

else:
    print ('maaf, anda kurang beruntung ')
