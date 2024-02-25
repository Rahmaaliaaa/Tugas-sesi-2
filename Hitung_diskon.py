menu = {
    "fried chiken"  : 15000,
    "Burger Queen"  : 25000,
    "French Fries"  : 10000,
    "Coca-cola"     : 10000
}
print("===== Daftar menu =====")
for i in menu:
    print("Daftar Menu :", i, "\t Harga : ", menu[i])
print("Pembelian diatas RP70000, - mendapat diskon 10%")
print("=======================")    
beli = input("Pilih Menu : ")
jumlah = int(input("jumlah pesanan : "))
bayar = jumlah * menu[beli]

if bayar > 70000:
    diskon = bayar*10/100
    total = bayar - diskon
else:
    total = bayar
print("===== Detail Pembayaran =====") 
print("Menu yang dipesan : ", beli)
print("Jumlah yang dipesan : ", jumlah)
print("Total biaya : ", bayar)
print("Total yang harus dibayar : ", total)