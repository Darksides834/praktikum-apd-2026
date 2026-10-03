# =========================================================
#  PROGRAM INPUT NILAI SISWA
#  Lembaga Kursus Bahasa Inggris
#  Jumlah soal ujian : 20  ->  nilai = jumlah benar x 5
# =========================================================
username_benar = "rasya"
password_benar = "020"

jumlah_soal = 20        
batas_salah = 3        


print("=" * 50)
print("      SELAMAT DATANG DI PROGRAM NILAI SISWA")
print("=" * 50)

percobaan = 0
login_berhasil = False      

while percobaan < batas_salah:
    username = input("Username (nama panggilan)   : ")
    password = input("Password (3 digit terakhir) : ")

    percobaan = percobaan + 1

    if username == username_benar and password == password_benar:
        print("\nLogin berhasil! Silakan menginput data siswa.\n")
        login_berhasil = True
        break                       
    else:
        sisa = batas_salah - percobaan
        print("Username atau password SALAH!")
        if sisa > 0:
            print("Kesempatan tersisa :", sisa, "kali/n")
            print("Anda sudah salah 3 kali. Program dihentikan.")


if login_berhasil == False:
    print("\nAKSES DITOLAK. Silakan coba lagi nanti.")
else:
    daftar_siswa = []

    lagi = "y"                      

    while lagi == "y" or lagi == "Y":
        print("-" * 50)
        print("Data siswa ke -", len(daftar_siswa) + 1)
        print("-" * 50)

        nama = input("Nama siswa  : ")
        kelas = input("Kelas siswa : ")

        ikut = input("Apakah siswa mengikuti ujian? (y/t) : ")

        if ikut == "t" or ikut == "T":
            status = "Tidak Ikut"
            benar = 0
            salah = 0
            nilai = 0
            print("Siswa tidak ikut ujian -> nilai otomatis = 0")
        else:
            status = "Ikut"
            total = 0
            while total != jumlah_soal:
                benar = int(input("Jumlah soal BENAR : "))
                salah = int(input("Jumlah soal SALAH : "))
                total = benar + salah
                if total != jumlah_soal:
                    print("Jumlah BENAR + SALAH harus", jumlah_soal, "! Coba lagi.")

            nilai = benar * 5

        if nilai >= 80:
            kategori = "Sangat Baik"
        elif nilai >= 60:
            kategori = "Baik"
        elif nilai >= 40:
            kategori = "Cukup"
        else:
            kategori = "Perlu Belajar Lagi"

        daftar_siswa.append([nama, kelas, status, nilai, kategori])

        lagi = input("\nMasih ingin menginput data siswa? (y/t) : ")
        print()


    print("=" * 65)
    print("                   LAPORAN NILAI SISWA")
    print("=" * 65)

    daftar_kelas = []
    for siswa in daftar_siswa:
        if siswa[1] not in daftar_kelas:
            daftar_kelas.append(siswa[1])

    for kelas in daftar_kelas:              #
        print("\nKelas :", kelas)
        print("-" * 65)
        print("No   Nama Siswa          Ikut Ujian    Nilai    Kategori")
        print("-" * 65)

        nomor = 1
        for siswa in daftar_siswa:         
            if siswa[1] == kelas:           
                print(str(nomor).ljust(5),
                      siswa[0].ljust(18),
                      siswa[2].ljust(13),
                       str(siswa[3]).ljust(8),
                      siswa[4])
                nomor = nomor + 1
        print("-" * 65)


    print("\nTotal siswa yang diinput :", len(daftar_siswa))
    print("Terima kasih, program selesai.")
