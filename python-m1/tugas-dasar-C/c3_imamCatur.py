# ================== VALIDATOR TANGGAL ==================

tanggal = int(input("Tanggal: "))
bulan = int(input("Bulan: "))
tahun = int(input("Tahun: "))

kabisat = bool(tahun % 4 == 0 and tahun % 100 != 0 or tahun % 400 == 0)
jumlahHari = tanggal 
tanggalValid = bool(bulan == 1 and tanggal <= 31 or bulan == 2 and tanggal <= 28 + kabisat or bulan == 3 and tanggal <= 31  or bulan == 4 and tanggal <= 30  or bulan == 5 and tanggal <= 31  or bulan == 6 and tanggal <= 30  or bulan == 7 and tanggal <= 31  or bulan == 8 and tanggal <= 31  or bulan == 9 and tanggal <= 30  or bulan == 10 and tanggal <= 31  or bulan == 11 and tanggal <= 30  or bulan == 12 and tanggal <= 31 )

print("Tahun Kabisat: \t", kabisat)
print("Jumlah hari: \t", jumlahHari)
print("Tanggal Valid: \t", tanggalValid)