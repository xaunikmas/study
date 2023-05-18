coba = 0
rahasia = 6
limit = 3

while coba < limit:
    tebak_angka = (int(input('masukkan angka [1-10] ')))

    if tebak_angka == rahasia:
        print ('selamat, anda menang ')
    coba = coba + 1

else:
    print ('maaf, anda kurang beruntung. Silakan coba lagi ')
