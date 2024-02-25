Gaji_pokok = float(input("Masukan gaji pokok karyawan             :"))
Uang_transport = float(input("Masukan transport harian            :"))
Uang_makan = float(input("Masukan uang makan harian               :"))
Tunjangan_jabatan = float(input("Masukan tunjangan jabatan        :"))
Honor_lembur = float(input("Masukan honor lembur                  :"))
Total_bekerja = float(input("Masukan total bekerja selama sebulan :"))

Total_gaji = (Gaji_pokok +(Uang_transport*Total_bekerja) +(Uang_makan*Total_bekerja) + Tunjangan_jabatan + Honor_lembur)

print("Total gaji karyawan adalah :", Total_gaji)