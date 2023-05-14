name  = input ("what is your name? ")
age = int(input("how old are you? "))
height = float(input ("what is your height? "))

print ("hello, "+ name)
print ("you are " + str(age) + " years of age")
print ("your height is "+ str(height) + " tall")

datas = input("masukkan data anda ")
print ("data anda adalah ", datas)

bineri = bool(int(input ('masukkan angka ')))
print ('angka ini adalah angka', bineri, 'typenya', type(bineri))

tahun = 2023
jawaban = input ('masukkan tahun kelahiran anda .. ')
print ('umur anda saat ini adalah :', tahun - int(jawaban))

kali = input ('masukkan kalimat : ')
print ('kalimat anda adalah = ', kali)
masuk = input ('masukkan kalimat yg diganti ')
masuk2 = input ('masukkan kalimat pengganti ')
print (kali.replace(masuk, masuk2))



