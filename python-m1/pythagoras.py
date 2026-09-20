apps = "Kalkulator Pythagoras"
print(f"===== {apps} =====")
nama = input("Masukkan Nama Anda: ")
print (f"Selamat datang {nama} di {apps}")
print ()

# ==========================================
# KALKULATOR PYTHAGORAS
# ==========================================
print(f"===== {apps} =====")
print ("Kalkulator untuk menghitung nilai C, jika diketahui nilai A dan B.")
print()

nialiA = float(input("Masukkan nilai A: ")) 
nilaiB = float(input("Masukkan nilai B: ")) 
nilaiC = (nialiA ** 2 + nilaiB ** 2) ** 0.5
print (f"Nilai C adalah {nilaiC}")
print() 

print (f"Terima kasih {nama} sudah mencoba {apps}.")