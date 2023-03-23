# while loop, pengulangan

nama = ""

while len(nama) == 0: # kondisi dimana input nama nya kosong, alias sama dengan null, maka akan loop terus meminta input argument nya
    nama = input("enter your name ?   ")  # result :  enter your name ?  

print("your name is " + nama)  # result : your name is niko

# atau pake metode lain, speerti dibawah :

nama = None

while not nama:
    nama = input ("please, enter your name?  ")

print ("your name is " + nama)