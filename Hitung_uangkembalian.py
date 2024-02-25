Daftar_menu = {
    "jus jeruk"     : 5000,
    "jus apel"      : 8000,
    "jus nanas"     : 8000,
    "jus mangga"    : 8000
}

for menu, harga in Daftar_menu.items():
    print("Daftar_menu :", menu, "\t Harga : ", harga)

beli = input("Pilih Daftar_menu:") 
jumlah = int(input("Jumlah pesanan:"))  

if beli in Daftar_menu:
    bayar = jumlah * Daftar_menu[beli]
else:
    print("Menu tidak ada dalam daftar.")
    exit()

print("Menu yang dipesan :", beli)
print("Jumlah yang dipesan :", jumlah)
print("Total biaya :", bayar)

uang_dibayar = int(input("Jumlah uang yang dibayarkan: ")) 

kembalian = uang_dibayar - bayar  

print("Total yang harus dibayar :", bayar)
print("Uang yang dibayarkan :", uang_dibayar)
print("Kembalian :", kembalian)

