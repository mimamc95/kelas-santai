print ("--------------------Struktur Data : LIST--------------------")
print ()

listNilaiUjian = [60,55,70,90,100,89]
listNamaSiswa = ["Caca","Indra","Doni","Fajar","Andi","Dedi"]

# Mengambil Data List
print ("Nilai Ujian   : ", listNilaiUjian[0])
print ("Nama Siswa: ", listNamaSiswa[0])
print ("Nilai Ujian   : ", listNilaiUjian[1])
print ("Nama Siswa: ", listNamaSiswa[1])
print ("Nilai Ujian   : ", listNilaiUjian[2])
print ("Nama Siswa: ", listNamaSiswa[2])
print ("Nilai Ujian   : ", listNilaiUjian[3])
print ("Nama Siswa: ", listNamaSiswa[3])
print ()

# Perulangan dengan For
for x in listNilaiUjian:
    print ("Nilai Ujian  :", x)
for y in listNamaSiswa:
    print ("Nama Siswa  :", y)

print()
# Mengedit Data
listNilaiUjian[0] = 100

print("Nilai Ujian  :", listNilaiUjian)

# Tambah Data dengan fungsi Append
listNamaSiswa.append("Sinchan")
print ("List Nama Siswa Setelah Ditambah:", listNamaSiswa)
print 
# Hapus Data dengan fungsi Remove
listNamaSiswa.remove("Sinchan")
print ("List Nama Siswa Setelah Dihapus:", listNamaSiswa)
