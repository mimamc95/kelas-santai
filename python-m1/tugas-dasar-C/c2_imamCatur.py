# ================== ANALISIS BILANGAN 5 DIGIT ==================

limaDigit = int(input("Masukkan bilangan 5 digit: "))
print()
validasi = bool(limaDigit//10000)
jumlahDigit1_2 = limaDigit // 10000 + limaDigit % 10000 // 1000
jumlahDigit3_4 =  limaDigit % 1000 // 100 + limaDigit % 100 // 10
digit5 =    limaDigit % 10
qtyDigitGenap = (limaDigit//10000%2==0)+(limaDigit//1000%2==0)+(limaDigit//100%2==0)+(limaDigit//10%2==0)+(limaDigit%2==0)
bilTerbalik1_2 = (limaDigit%10)*10000 + (limaDigit%100 // 10) * 1000 
bilTerbalik3_4 = (limaDigit%1000 // 100) * 100 + (limaDigit % 10000 // 1000) * 10 
bilTerbalik5 = (limaDigit // 10000) * 1
bilPalindrom = (limaDigit == bilTerbalik1_2 + bilTerbalik3_4 + bilTerbalik5)
bilHarshad = (jumlahDigit1_2 + jumlahDigit3_4 + digit5) % limaDigit == 0

print ("Input Valid: ", validasi)
print ("Jumlah Digit: ", jumlahDigit1_2 + jumlahDigit3_4 + digit5)
print ("Banyak digit genap: ", qtyDigitGenap)
print ("Bilangan terbalik: ", bilTerbalik1_2 + bilTerbalik3_4 + bilTerbalik5)
print ("Bilangan Palindrom: ", bilPalindrom)
print ("Bilangan Harshad: ", bilHarshad)