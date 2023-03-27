# slicing = create a substring by extracting elements from another string
# indexing [], or slice ()

# name = "niko novianto"
# # first = name [0:8:3]  # argument pada index [start index:stop index:step index]
# balik_nama = name[::-4]
# # print (first)
# print (balik_nama)


website = "http://google.com"
website2 = "http://amazon.com"
namaFull = "niko noviyanto nixau"

potong = slice(7, -4) # 7 adalah object ke "n" dari variable website dan website2
potong1 = slice(15, 20)

print (website[potong])
print (website2[potong])
print (namaFull[potong1])
