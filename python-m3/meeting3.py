import cth_module as cm # as adalah alias dari module

sapa = cm.salam("Upin")
a= 20
b= 10

print(f"Halo {sapa}, hasil penjumlahan: ", cm.tambah(a, b))
print(f"Halo {sapa}, hasil pengurangan: ", cm.kurang(a, b))
print(f"Halo {sapa}, hasil perkalian: ", cm.kali(a, b))
print(f"Halo {sapa}, hasil pembagian: ", cm.bagi(a, b))

# def main():
#     a = 20
#     b = 10
#     print("hasil penjumlahan: ", cm.tambah(a, b))
#     print("hasil pengurangan: ", cm.kurang(a, b))
#     print("hasil perkalian: ", cm.kali(a, b))
#     print("hasil pembagian: ", cm.bagi(a, b))