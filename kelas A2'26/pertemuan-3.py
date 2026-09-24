#angka = 11
#if angka < 10: # Kondisi percabangan IF
#print("Angka kurang dari 10")

#umur = int(input("Masukkan umur: ")) # Input umur
# Misalkan, umur = 17
#if umur >= 17:
#    print("Kamu sudah bisa membuat KTP") # Blok if dijalankan karena kondisi True
#else:
#    print("Kamu belum bisa membuat KTP") # Blok else tidak dijalankan

# Input jenis kendaraan dari user
# kendaraan = input("Masukkan jenis kendaraan anda: ").lower() 

# if kendaraan == "mobil":
#     tarif_parkir = 10000
# elif kendaraan == "motor":
#     tarif_parkir = 5000
# else:
#     tarif_parkir = 15000
# # Menampilkan tarif parkir yang harus dibayar
# print("Tarif parkir yang harus dibayar:", tarif_parkir)

# Bentuk Awal Percabangan IF/ELSE
# umur = 20
# if umur >= 18:
#     status = "Dewasa"
# else:
#     status = "Belum Dewasa"
# # Bentuk Ternary Operator
# umur = 20
# status = "Dewasa" if umur >= 18 else "Belum Dewasa"

# nilai = int(input("Masukkan nilai: "))
# if nilai >= 10:
#     if nilai >= 20:
#         if nilai >= 30:
#             print("Angka besar")
#         print("Angka sedang")
#     print("Angka kecil")

# studi kasus 1
# usia = int(input("Masukkan usia Anda: "))
# if usia >= 16:
#     print("IF/ELSE: Anda boleh masuk.")
# else:
#     print("IF/ELSE: Anda dilarang masuk.")

# status = "Boleh masuk" if usia >= 16 else "Dilarang masuk"
# print("Ternary:", status)

# studi kasus 2
nama = "Uzumaki Tatang"
total_pembelian = int(input("Masukkan total pembelian: Rp "))
if total_pembelian > 200000:
    diskon = 30
elif total_pembelian > 100000:
    diskon = 10
else:
    diskon = 0
jumlah_diskon = total_pembelian*diskon/100
total_bayar = total_pembelian-jumlah_diskon
bayar = total_pembelian
print("Nama:", nama)
print("Total pembelian: Rp", total_pembelian)
print("Diskon:", diskon, "%")
print("Jumlah diskon: Rp", jumlah_diskon)
print("Total yang harus dibayar sebelum diskon: Rp", bayar)
print("Total yang harus dibayar sesudah diskon: Rp", total_bayar)