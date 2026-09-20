print ("---------------------------VAriable dan Tipe Data---------------------------")
print("Hello World")      #String 
print("Kita belajar Python sampai jadi expert, insyaallah")      #String 

nama = "M.Imam Catur"    # String
umur = 30                # Integer
status_menikah = True    # Boolean
tinggi = 167.0           # Float
berat = 64.5             # Float

print(f"Nama Saya adalah {nama}, umur saya yaitu {umur}, dan saya status menikah saya adalah {status_menikah}")
print(f"Saya memiliki tinggi {tinggi} CM dan berat {berat} KG")


# print ("---------------------------Operator Aritmatika---------------------------")

# Bilangan1 = 5
# Bilangan2 = 10

# print (f"Hasil penjumlahan dari {Bilangan1} + {Bilangan2} = {Bilangan1 + Bilangan2}")
# print (f"Hasil pengurangan dari {Bilangan1} - {Bilangan2} = {Bilangan1 - Bilangan2}")
# print (f"Hasil perkalian dari {Bilangan1} * {Bilangan2} = {Bilangan1 * Bilangan2}")
# print (f"Hasil pembagian dari {Bilangan1} / {Bilangan2} = {Bilangan1 / Bilangan2}")
# print (f"Hasil perpangkatan dari {Bilangan1} ^ {Bilangan2} = {Bilangan1 ^ Bilangan2}")
# print (f"Hasil modulus dari {Bilangan1} % {Bilangan2} = {Bilangan1 % Bilangan2}")

print ("---------------------------Operator Aritmatika_Input---------------------------")

bilPertama = int(input("Masukkan Bilangan Pertama: "))
bilKedua = int(input("Masukkan Bilangan Kedua: "))

print (f"Hasil penjumlahan dari {bilPertama} + {bilKedua} = {bilPertama + bilKedua}")
print (f"Hasil pengurangan dari {bilPertama} - {bilKedua} = {bilPertama - bilKedua}")
print (f"Hasil perkalian dari {bilPertama} * {bilKedua} = {bilPertama * bilKedua}")
print (f"Hasil pembagian dari {bilPertama} / {bilKedua} = {bilPertama / bilKedua}")
print (f"Hasil perpangkatan dari {bilPertama} ^ {bilKedua} = {bilPertama ^ bilKedua}")
print (f"Hasil modulus dari {bilPertama} % {bilKedua} = {bilPertama % bilKedua}")

print ("---------------------------Operator Perbandingan---------------------------") # Hasilnya True atau False
print (f"Apakah {bilPertama} lebih besar dari {bilKedua}: {bilPertama > bilKedua}")
print (f"Apakah {bilPertama} lebih kecil dari {bilKedua}: {bilPertama < bilKedua}")
print (f"Apakah {bilPertama} lebih besar dari atau sama dengan {bilKedua}: {bilPertama >= bilKedua}")
print (f"Apakah {bilPertama} lebih kecil dari atau sama dengan {bilKedua}: {bilPertama <= bilKedua}")
print (f"Apakah {bilPertama} sama dengan {bilKedua}: {bilPertama == bilKedua}")
print (f"Apakah {bilPertama} tidak sama dengan {bilKedua}: {bilPertama != bilKedua}")

print ("---------------------------Operator Logika---------------------------")
#Operator Logika itu dia membandinga antara 2 Pernyataan nilai true or False --> ada 3 Operator Logika yaitu AND, OR, dan NOT 
#Operator Logika AND --> Jika Kedua Pernyataan bernilai True maka akan menghasilkan True, Jika tidak maka akan False
#Operator Logika OR --> Jika Kedua Pernyataan bernilai True maka akan menghasilkan True, Jika tidak maka akan False 

Kondisi1 = True
Kondisi2 = True

print(f"Operator Logika AND : {Kondisi1 and Kondisi2}") #Outputnya itu adalah true 
print(f"Operator Logika OR : {Kondisi1 or Kondisi2}") #Outputnya itu adalah true 
print(f"Operator Logika NOT : {not Kondisi1}") #Outputnya itu adalah false 


umur = 25
punya_ktp = True
print(umur >= 17 and punya_ktp)  # True
print(umur < 17 or punya_ktp)    # True
print(not punya_ktp)             # False


