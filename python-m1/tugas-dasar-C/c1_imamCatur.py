# ================== MESIN KASIR KEMBALIAN ==================

totalBelanja = int(input("Total belanja \t: Rp "))
uangDibayar = int(input("Uang dibayar \t: Rp "))
print ()
uangCukup = bool(uangDibayar >= totalBelanja)
uangKekurangan = (uangDibayar - totalBelanja) *  bool(not uangCukup)
uangKembalian = (uangDibayar - totalBelanja) * bool(uangCukup)
pecahan100k = uangKembalian//100000
pecahan50k = (uangKembalian%100000)//50000
pecahan20k = (uangKembalian%50000)//20000
pecahan10k = (uangKembalian%20000)//10000
pecahan5k = (uangKembalian%10000)//5000
pecahan2k = (uangKembalian%5000)//2000
pecahan1k = (uangKembalian%2000)//1000
pecahan500 = (uangKembalian%1000)//500
totalPecahan = pecahan100k + pecahan50k + pecahan20k + pecahan10k + pecahan5k + pecahan2k + pecahan1k + pecahan500

print("Uang cukup \t: ",uangCukup)
print("Kekurangan \t: Rp ",abs(uangKekurangan))
print("Kembalian \t: Rp ",abs(uangKembalian))
print("Rp100.000 \t: ", pecahan100k, "lembar")
print("Rp50.000 \t: ", pecahan50k, "lembar")
print("Rp20.000 \t: ", pecahan20k, "lembar")
print("Rp10.000 \t: ", pecahan10k, "lembar")
print("Rp5.000 \t: ", pecahan5k, "lembar")
print("Rp2.000 \t: ", pecahan2k, "lembar")
print("Rp1.000 \t: ", pecahan1k, "keping")
print("Rp500 \t\t: ", pecahan500, "keping")
print("Total lembar/keping \t:", totalPecahan )