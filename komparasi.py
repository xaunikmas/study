# membuat logika 

""" angka kurang dari 3 jadi true, diatas 3 false, dan angka dibawah 10 false dan diatas 10 jadi true"""

angka = (int(input('masukkan angka dibawah 3\natau \ndibawah 10: ')))

isBenar = (angka < 3 or angka > 10)
print ('angka:', angka, isBenar)

isSalah = (angka > 3 or angka < 10)
print ('angka:', angka, isBenar)

hasil = isBenar and isSalah
print (hasil)


""" APABILA KONDISINYA SALAH 1 BENAR, MAKA KALO PAKE 'AND' HASILNYA FALSE. 
TAPI KALO PAKE 'OR' AKAN TRUE. KARENA 'OR' SYARATNYA HARUS SALAH 1 BENAR
SEDANGKAN 'AND', 2 - 2 NYA HARUS BERNILAI TRUE ATO FALSE """


""" SKARANG, MEMBUAT ANGKA LEBIH DARI 3 TRUE, DAN ANGKA DIBAWAH 10 TRUE, DIATAS 10 FALSE """

""" masukkan = int(input('masukkan angka diatas 3\ndan\ndibawah 10 : ')) """

masukkan = (int(input('masukkan angka')))

lebihDari = (masukkan > 3)
print ('angka', masukkan, 'diatas 3 = ', lebihDari)

kurangDari = (masukkan < 10)
print ('angka', masukkan, 'dibawah 10 = ', kurangDari)

isBenar = (kurangDari or lebihDari)
print ('angka yg anda masukkan', isBenar)


""" KASUS IRISAN
------ 3 +++++++++ 10 --------  
DIBAWAH 3, FALSE, DIANTARA 3 - 10 TRUE, DIATAS 10 FALSE  """

""" masukkan = int(input('masukkan angka diatas 3\ndan\ndibawah 10: '))

lebihDari = (masukkan > 3)
print ('angka', masukkan, 'diatas 3 = ', lebihDari)

kurangDari = (masukkan < 10)
print ('angka', masukkan, 'dibawah 10 = ', kurangDari)

isBenar = (kurangDari and lebihDari)
print ('angka yg anda masukkan', isBenar)  """


""" LATIHAN """
# SOAL 1/ 
#  --- 0 ++++ 5 ---- 8 ++++ 11 --- 

# angka = (int(input('masukkan angka: '))) 

# isBenar = (angka > 0 and angka < 5 or angka > 8 and angka < 11)
# print ('angka', angka, isBenar)

# isSalah = (angka < 0 and angka < 8 or angka > 11 )

# hasil = isBenar or isSalah
# print (hasil)


# SOAL 2/  +++ 0 --- 5 +++ 8 --- 11 +++  """
# angka = (int(input('masukkan angka: '))) 

# isBenar = (angka < 0 or angka > 5 and angka < 8 or angka > 11)
# print ('angka', angka, isBenar)

# isSalah = (angka > 0 and angka < 5 or angka > 8 and angka < 11)

# hasil = isBenar and isSalah
# print (hasil)
