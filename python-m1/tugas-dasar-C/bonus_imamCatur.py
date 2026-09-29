# ================== SORTING 3 BILANGAN ==================

bilangan1 = int(input("Masukkan Bilangan 1 \t: "))
bilangan2 = int(input("Masukkan Bilangan 2 \t: "))
bilangan3 = int(input("Masukkan Bilangan 3 \t: "))

bilKecil = (bilangan1 <= bilangan2 and bilangan1 or bilangan2 )
bilTerkecil = (bilKecil <= bilangan3 and bilKecil or bilangan3)
bilBesar = (bilangan1 >= bilangan2 and bilangan1 or bilangan2 )
bilTerBesar = (bilBesar >= bilangan3 and bilBesar or bilangan3)

bilTengah = (bilangan1 + bilangan2 + bilangan3) - bilTerkecil - bilTerBesar
# bilTengah, bilTerkecil = ((bilTengah == 0 and bilTerkecil or bilTengah), (bilTerkecil == 0 and bilTengah or bilTerkecil) )2

aritmetika = bool(bilangan1 - bilangan2 == bilangan2 - bilangan3 )

print ("Bilangan Terkecil \t:", bilTerkecil)
print ("Bilangan Tengah \t:", bilTengah)
print ("Bilangan Terbesar \t:", bilTerBesar)
print ("Barisan Aritmetika \t:", aritmetika)