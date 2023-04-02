print ("""
Nama : niko
kelas : 2
job : software developer
""")
# multiline literal string, bisa bikin value/argument yang banyak

print (r"c:\windows\user\application_data")  # r = raw string. dibelakang R smeua dianggap string
print ("================================================")

""" OPERASI DAN MANIPULASI STRING """
# 1. CONCATENATE = MENYAMBUNG STRING

nama_awal = 'niko'
nama_tengah = 'noviyanto'
nama_akhir = 'nixau'

nama_lengkap = nama_awal +" " + nama_tengah + " " + nama_akhir
print ('panjang karakter dari', nama_lengkap, len(nama_lengkap), type(nama_lengkap))

# operator dalam bentuk method

nama = "niko noviyanto"
print ('jumlah n pada niko noviyanto adalah:', nama.count('n')) # --> dalam OOP berlaku seperti ini: nama (adalah object).count (adalah method)

# PENGECEKAN DENGAN METHOD "is.X"

nama = "niko noviyanto"
namaLower = nama.islower()
print (nama + ' is lower ' + str(namaLower))
namaUpper = nama.isupper()
print (nama + ' is upper ' + str(namaUpper))



