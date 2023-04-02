#  Loop control statement = change a loop execution from its normal sequence

#  break    = used to terminate the loop seluruhnya
#  continue = skip to the next iteration of the loop
#  pass     = does nothing, acts as a placeholder


#  penggunaan "break"

while True:
    nama = input('masukkan nama anda? ')
    if nama != '':
        break
print ('nama anda adalah ', nama)
    
print ('\n============= penggunaan break =======================\n')

# penggunaan continue

telepon = "0812-8331-0220"

for i in telepon:
    if i == "-":
        continue
    print (i, end='')

print ('\n============= penggunaan continue =======================\n')

# pengunaan pass

for isi in range (1, 11):
    if isi == 3:
        pass
    else:
        print (isi)


print ('\n============= penggunaan pass =======================')
