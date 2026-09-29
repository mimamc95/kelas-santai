# ================== TARIF PARKIR MAL ==================

jamMasuk = int(input("Jam Masuk \t: "))
menitMasuk = int(input("Menit Masuk \t: "))
jamKeluar = int(input("Jam Keluar \t: "))
menitKeluar = int(input("Menit Keluar \t: "))

totMenit = (jamKeluar - jamMasuk) * 60 + (menitKeluar - menitMasuk)
lamaParkir = (totMenit >= 0 and totMenit) or (totMenit + 24 * 60)
lamaJam = lamaParkir // 60
lamaMenit = lamaParkir % 60
jamDitagih = lamaJam + (lamaMenit > 0 and 1 or 0)
tarif = 3000 + (jamDitagih - 1) * 2000
totTarif = (tarif <= 20000 and tarif) or 20000

print ("\nLama parkir \t: ", lamaJam, "jam", lamaMenit, "menit" )
print ("Jam ditagih \t: ", jamDitagih, "jam")
print ("Tarif \t\t: Rp ", totTarif)
