apps = "Kalkulator Konversi Suhu Sederhana"
print(f"===== {apps} =====")
nama = input("Masukkan Nama Anda: ")
print (f"Selamat datang {nama} di {apps}")
print ()

# ==========================================
# KALKULATOR KONVERSI SUHU SEDERHANA
# ==========================================
print("===== Kalkulator Konversi Suhu =====")
celcius = float(input("Masukkan suhu dalam Celcius (°C): "))

# Rumus Konversi Suhu
reamur = (4 / 5) * celcius
fahrenheit = ((9 / 5) * celcius) + 32
kelvin = celcius + 273.15

# Tampilkan Hasil
print("\nHasil Konversi:")
print(f"Reamur     : {reamur} °R")
print(f"Fahrenheit : {fahrenheit} °F")
print(f"Kelvin     : {kelvin} K")
print() 

print (f"Terima kasih {nama} sudah mencoba {apps}.")