# ================== SELEKSI BEASISWA ==================

nilaiTugas = float(input("Nilai Tugas \t\t: "))
nilaiUts = float(input("Nilai UTS \t\t: "))
nilaiUas = float(input("Nilai UAS \t\t: "))
kehadiran = float(input("% Kehadiran \t\t: "))
penghasilanOrtu = int(input("Penghasilan Ortu \t: "))
jumlahSertif = int(input("Jumlah Sertifikat \t: "))

nilaiAkhir = ((0.2*nilaiTugas + 0.35*nilaiUts+0.45*nilaiUas))
inputValid = bool(nilaiTugas >= 0 and nilaiTugas <= 100 and nilaiUts >= 0 and nilaiUts <= 100 and nilaiUas >=0 and nilaiUas <= 100 and kehadiran >= 0 and kehadiran <= 100)

layakBeasiswa = bool( inputValid == True and (nilaiAkhir >= 80 and kehadiran >= 85 and nilaiTugas >= 65 and nilaiUts >= 65 and nilaiUas >= 65 and (penghasilanOrtu <= 4000000 or jumlahSertif >= 2)))

statusLayak = (layakBeasiswa == True) * "LAYAK" + (layakBeasiswa == False) * "TIDAK LAYAK"

print (f"Nilai akhir \t\t: {nilaiAkhir:.1f}")
print ("Input Valid \t\t:", inputValid)
print ("Status Beasiswa \t:", statusLayak)