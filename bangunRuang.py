apps = "Kalkulator Bangun Ruang"
print(f"===== {apps} =====")
nama = input("Masukkan Nama Anda: ")
print (f"Selamat datang {nama} di {apps}")
print ("Ada 3 bangun ruang yang tersedia, yaitu : ")
print ("1. Kubus")
print ("2. Lingkaran")
print ("3. Kerucut")
print ()

# ==========================================
# KALKULATOR KUBUS
# ==========================================
print("===== Kalkulator Luas Permukaan & Volume Kubus =====")
sisi = float(input("Masukkan panjang sisi kubus: "))

luas_permukaan_kubus = 6 * (sisi ** 2)
volume_kubus = sisi ** 3

print(f"Luas permukaan kubus dengan sisi {sisi} adalah: {luas_permukaan_kubus}")
print(f"Volume kubus dengan sisi {sisi} adalah: {volume_kubus}")
print()

# ==========================================
# KALKULATOR LINGKARAN
# ==========================================
print("===== Kalkulator Luas Lingkaran =====")
jari_jari_lingkaran = float(input("Masukkan nilai jari-jari lingkaran: "))
phi = 3.14

luas_lingkaran = phi * (jari_jari_lingkaran ** 2)

print(f"Luas lingkaran dengan jari-jari {jari_jari_lingkaran} adalah: {luas_lingkaran}")
print()

# ==========================================
# KALKULATOR KERUCUT
# ==========================================
print("===== Kalkulator Volume & Luas Permukaan Kerucut =====")
jari_jari_kerucut = float(input("Masukkan jari-jari alas kerucut: "))
tinggi_kerucut = float(input("Masukkan tinggi kerucut: "))

# Garis pelukis (s) menggunakan pythagoras
garis_pelukis = (jari_jari_kerucut ** 2 + tinggi_kerucut ** 2) ** 0.5

luas_alas_kerucut = phi * (jari_jari_kerucut ** 2)
luas_selimut_kerucut = phi * jari_jari_kerucut * garis_pelukis

volume_kerucut = (1/3) * luas_alas_kerucut * tinggi_kerucut
luas_permukaan_kerucut = luas_alas_kerucut + luas_selimut_kerucut

print(f"Volume kerucut adalah: {volume_kerucut}")
print(f"Luas permukaan kerucut adalah: {luas_permukaan_kerucut}")
print ()
print (f"Terima kasih {nama} sudah mencoba {apps}")
