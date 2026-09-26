# ============================================================
#  PROGRAM SIMULASI TRANSAKSI PENGISIAN BBM DI SPBU
#  Materi    : Percabangan (if / elif / else)
# ============================================================

Nama = "Rasya"          
NIM           = "2609106020"    
# ============================================================
print("======================================================================")
print("        SISTEM TRANSAKSI BBM SPBU - LOGIN")
print("======================================================================")

input_nama = input("Masukkan nama panggilan        : ")
input_nim  = input("Masukkan 2 digit terakhir NIM  : ")

nim_2_digit = NIM[-2:]

if input_nama == Nama and input_nim == nim_2_digit:
    print("\n>> LOGIN BERHASIL! Selamat datang, " + Nama + ".\n")

    print("======================================================================")
    print("               MENU PEMILIHAN BBM")
    print("======================================================================")
    print(" 1. Pertalite      : Rp 10.000 / liter")
    print(" 2. Pertamax       : Rp 12.500 / liter")
    print(" 3. Pertamax Turbo : Rp 15.000 / liter")
    print("======================================================================")

    pilihan = input("Pilih jenis BBM (1-3) : ")

    jenis_bbm = ""
    harga_per_liter = 0

    if pilihan == "1":
        jenis_bbm = "Pertalite"
        harga_per_liter = 10000
    elif pilihan == "2":
        jenis_bbm = "Pertamax"
        harga_per_liter = 12500
    elif pilihan == "3":
        jenis_bbm = "Pertamax Turbo"
        harga_per_liter = 15000
    else:
        print("\n>> Pilihan tidak valid! Program berhenti.")

    if jenis_bbm != "":
        liter = float(input("Masukkan jumlah liter yang dibeli : "))

        total_harga = harga_per_liter * liter

        if liter >= 10:
            persen_diskon = 10
        elif liter >= 5:
            persen_diskon = 5
        else:
            persen_diskon = 0

        diskon_pembelian = (persen_diskon / 100) * total_harga

        print("======================================================================")
        status_member = input("Apakah pembeli merupakan member? (y/t) : ")

        if status_member == "y" or status_member == "Y":
            is_member = True
        else:
            is_member = False

        if is_member:
            diskon_member = (2 / 100) * total_harga
            status = "MEMBER"
        else:
            diskon_member = 0
            status = "NON-MEMBER"

        total_bayar = total_harga - diskon_pembelian - diskon_member

        print()
        print("======================================================================")
        print("             STRUK TRANSAKSI PENGISIAN BBM - SPBU                 ")
        print("======================================================================")
        print("Nama Pembeli        :", Nama)
        print("NIM                 :", NIM)
        print("Status              :", status)
        print("======================================================================")
        print("Jenis BBM           :", jenis_bbm)
        print("Harga/Liter         :", harga_per_liter,"/L")
        print("Jumlah Liter        :", liter, "L")
        print("======================================================================")
        print("Total Harga         :Rp", total_harga)
        print(f"Diskon ({persen_diskon}%)        :Rp", diskon_pembelian)
        print(f"Diskon Member (2%)  :Rp", diskon_member)
        print("======================================================================")
        print("TOTAL BAYAR         :Rp", total_bayar)
        print("======================================================================")
        print()

else:
    print("\n>> LOGIN GAGAL! Nama atau NIM tidak sesuai.")
    print(">> Program berhenti. Transaksi tidak dapat dilanjutkan.")
