# Program Kalkulasi Berat Bagasi Kabin Maskapai
# Posttest 2 - Algoritma Pemrograman Dasar 
#==============================================

# 1. Data berat bagasi 6 penumpang baris pertama (kg) dan banyak penumpang
bagasi_1 = 12
bagasi_2 = 18
bagasi_3 = 7
bagasi_4 = 15
bagasi_5 = 20
bagasi_6 = 10
banyak_penumpang = 6

# 2. Hitung total berat secara MANUAL (tanpa fungsi SUM / sum())
total_berat = bagasi_1+bagasi_2+ bagasi_3+bagasi_4+bagasi_5+bagasi_6
kompensasi = 0.05*total_berat
total_berat_akhir = total_berat+kompensasi

# 3. Rata-rata berat bagasi per orang 
rata_rata = total_berat_akhir/banyak_penumpang

# 4. NIM
nim = 20

# 5. Boolean
boolean = nim < rata_rata

# list
list_bagasi = [bagasi_1, bagasi_2, bagasi_3, bagasi_4, bagasi_5, bagasi_6]

# Metode list slicing untuk menghasilkan indeks 2, 3, 4
tengah = list_bagasi[2:5]

# konversi total berat akhir ke satuan gram
total_gram = total_berat_akhir * 1000

# 6. Tampilkan seluruh nilai variabel
print("===== DATA BAGASI PENUMPANG =====")
print("bagasi_1     :", bagasi_1, "kg")
print("bagasi_2     :", bagasi_2, "kg")
print("bagasi_3     :", bagasi_3, "kg")
print("bagasi_4     :", bagasi_4, "kg")
print("bagasi_5     :", bagasi_5, "kg")
print("bagasi_6     :", bagasi_6, "kg")
print("banyak_penumpang  :", banyak_penumpang)
print()
print("===== HASIL PERHITUNGAN =====")
print("total_berat       :", total_berat, "kg")
print("kompensasi (5%)   :", kompensasi, "kg")
print("total_ berat_akhir :", total_berat_akhir, "kg")
print("rata_rata         :", rata_rata, "kg")
print("NIM               :", nim)
print("boolean           :", boolean)
print()
print("===== POIN PLUS =====")
print("list bagasi (list)            :", list_bagasi)
print("penumpang tengah (indeks 2-4) :", tengah)
print("total berat akhir (gram)       :", total_gram, "g")
print("================================")