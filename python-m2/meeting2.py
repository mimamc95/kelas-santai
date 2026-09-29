print ("--------------------Percabangan--------------------")
print ()

nilaiMtk = int(input("Masukkan nilai Matematika: "))
nilaiIndo = int(input("Masukkan nilai Bahasa Indonesia: "))
nilaiEng = int(input("Masukkan nilai Bahasa Inggris: "))
nilaiSains = int(input("Masukkan nilai Sains: "))
print ()

print ("======= Hasil Kelulusan =======")
print ()

if nilaiMtk == 100:
    print ("Nilai Matematika = A+")
elif nilaiMtk >= 80:
    print ("Nilai Matematika = A")
elif nilaiMtk >= 75:
    print ("Nilai Matematika = B")
elif nilaiMtk >= 65:
    print ("Nilai Matematika = C")
else:
    print ("Nilai Matematika = D")
print()


if nilaiIndo == 100:
    print ("Nilai B.Indonesia = A+")
elif nilaiIndo >= 80:
    print ("Nilai B.Indonesia = A")
elif nilaiIndo >= 75:
    print ("Nilai B.Indonesia = B")
elif nilaiIndo >= 65:
    print ("Nilai B.Indonesia = C")
else:
    print ("Nilai B.Indonesia = D")
print ()

if nilaiEng == 100:
    print ("Nilai B.Inggris = A+")
elif nilaiEng >= 80:
    print ("Nilai B.Inggris = A")
elif nilaiEng >= 75:
    print ("Nilai B.Inggris = B")
elif nilaiEng >= 65:
    print ("Nilai B.Inggris = C")
else:
    print ("Nilai B.Inggris = D")
print ()

if nilaiSains == 100:
    print ("Nilai Sains = A+")
elif nilaiSains >= 80:
    print ("Nilai Sains = A")
elif nilaiSains >= 75:
    print ("Nilai Sains = B")
elif nilaiSains >= 65:
    print ("Nilai Sains = C")
else:
    print ("Nilai Sains = D")
print ()