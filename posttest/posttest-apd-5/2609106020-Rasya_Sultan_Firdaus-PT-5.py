# =====================================================================
# PROGRAM  : SISTEM STREAMING ANIME
# =====================================================================
import os

clear = "cls" if os.name == "nt" else "clear"  

# akun admin yang sudah disediakan oleh sistem
admin_username = "admin"
admin_password = "admin123"

# tempat akun pengguna
akun = [
    ["user", "user123"]
]

# data anime: [id, judul, genre, episode, status, tahun]
anime = [
    [1, "Naruto Shippuden",  "Action",  500, "Completed", 2007],
    [2, "One Piece",         "Action",  1120, "Ongoing",  1999],
    [3, "Attack on Titan",   "Action",   87, "Completed", 2013],
    [4, "Spy x Family",      "Comedy",   37, "Ongoing",   2022],
    [5, "Death Note",        "Thriller", 37, "Completed", 2006]
]

# data watchlist: [username, id_anime, status_tonton]
watchlist = [
    ["user", 3, "Sudah Ditonton"]
]

# pilihan status 
pilihan_status_anime = ["Ongoing", "Completed", "Hiatus"]
pilihan_status_watchlist = ["Belum Ditonton", "Rencana", "Sudah Ditonton"]

# ---------------------------------------------------------------------
# MENU UTAMA
# ---------------------------------------------------------------------

program_jalan = True
while program_jalan:

    os.system(clear)
    print("==============================================")
    print("          SISTEM STREAMING ANIME")
    print("==============================================")
    print(" 1. Login")
    print(" 2. Register (Pengguna Baru)")
    print(" 3. Keluar")
    print("==============================================")
    menu_utama = input("Pilih menu [1/2/3] : ")

    # =================================================================
    # MENU 1 : LOGIN
    # =================================================================
    if menu_utama == "1":

        login_jalan = True
        berhasil_login = False
        role = ""
        user_aktif = ""

        while login_jalan:

            os.system(clear)
            print("==============================================")
            print("                   LOGIN")
            print("==============================================")
            print(" 1. Login sebagai Admin")
            print(" 2. Login sebagai Pengguna")
            print(" 0. Kembali ke menu utama")
            print("==============================================")
            pilihan_login = input("Pilih [0/1/2] : ")

            # ---------- login admin ----------
            if pilihan_login == "1":

                percobaan = 0
                while percobaan < 3 and berhasil_login == False:

                    os.system(clear)
                    print("==============================================")
                    print("               LOGIN ADMIN")
                    print("==============================================")
                    input_username = input("Username : ")
                    input_password = input("Password : ")

                    if input_username == "" or input_password == "":
                        print("\n[!] Username dan password tidak boleh kosong.")
                        percobaan = percobaan + 1
                    elif input_username == admin_username and input_password == admin_password:
                        print("\n[+] Login admin berhasil!")
                        berhasil_login = True
                        role = "admin"
                        user_aktif = admin_username
                        login_jalan = False
                    else:

                        print("\n[!] Username atau password salah.")
                        percobaan = percobaan + 1
                        if percobaan < 3:
                            print("    Sisa percobaan : " + str(3 - percobaan))

                    if berhasil_login == False and percobaan < 3:
                        input("\nTekan Enter untuk mencoba lagi...")

                if berhasil_login == False:
                    print("\n[!] Percobaan login habis, kembali ke menu login.")
                    input("Tekan Enter untuk melanjutkan...")

            # ---------- login pengguna ----------
            elif pilihan_login == "2":

                os.system(clear)
                print("==============================================")
                print("              LOGIN PENGGUNA")
                print("==============================================")
                input_username = input("Username : ")
                input_password = input("Password : ")

                if input_username == "" or input_password == "":
                    print("\n[!] Username dan password tidak boleh kosong.")
                    input("Tekan Enter untuk melanjutkan...")
                else:
                    ketemu = -1
                    for i in range(len(akun)):
                        if akun[i][0] == input_username and akun[i][1] == input_password:
                            ketemu = i

                    if ketemu == -1:
                        print("\n[!] Akun tidak ditemukan atau password salah.")
                        print("    Silakan register terlebih dahulu bila belum punya akun.")
                        input("Tekan Enter untuk melanjutkan...")
                    else:
                        print("\n[+] Login berhasil, selamat datang " + input_username + "!")
                        berhasil_login = True
                        role = "user"
                        user_aktif = input_username
                        login_jalan = False
                        input("Tekan Enter untuk melanjutkan...")

            # ---------- kembali ----------
            elif pilihan_login == "0":
                login_jalan = False

            # ---------- input salah ----------
            else:
                print("\n[!] Pilihan tidak tersedia, silakan pilih 0, 1, atau 2.")
                input("Tekan Enter untuk melanjutkan...")

        # =============================================================
        # SESi ADMIN
        # =============================================================
        if berhasil_login == True and role == "admin":

            sesi_admin = True
            while sesi_admin:

                os.system(clear)
                print("==============================================")
                print("              MENU ADMIN")
                print("  User : " + user_aktif + " (Admin)")
                print("==============================================")
                print(" 1. Tambah Anime")
                print(" 2. Tampilkan Daftar Anime")
                print(" 3. Edit Informasi Anime")
                print(" 4. Hapus Anime")
                print(" 5. Logout")
                print("==============================================")
                menu_admin = input("Pilih menu [1/2/3/4/5] : ")

                # ---------- 1. TAMBAH ANIME ----------
                if menu_admin == "1":

                    os.system(clear)
                    print("==============================================")
                    print("               TAMBAH ANIME")
                    print("==============================================")
                    judul_baru = input("Judul anime      : ")

                    if judul_baru == "":
                        print("\n[!] Judul tidak boleh kosong, data batal disimpan.")
                    else:
                        genre_baru = input("Genre            : ")
                        if genre_baru == "":
                            genre_baru = "-"

                        episode_baru = input("Jumlah episode   : ")
                        if episode_baru.isdigit() == False:
                            print("\n[!] Jumlah episode harus angka, data batal disimpan.")
                        else:
                            print("----------------------------------------------")
                            print(" Pilihan status anime :")
                            for i in range(len(pilihan_status_anime)):
                                print("  " + str(i + 1) + ". " + pilihan_status_anime[i])
                            status_baru = input("Status [1/2/3]   : ")

                            if status_baru != "1" and status_baru != "2" and status_baru != "3":
                                print("\n[!] Pilihan status tidak tersedia, data batal disimpan.")
                            else:
                                tahun_baru = input("Tahun rilis      : ")
                                if tahun_baru.isdigit() == False:
                                    print("\n[!] Tahun rilis harus angka, data batal disimpan.")
                                else:
                                    id_baru = 1
                                    for baris in anime:
                                        if baris[0] >= id_baru:
                                            id_baru = baris[0] + 1
                                    anime.append([id_baru, judul_baru, genre_baru,
                                                  int(episode_baru),
                                                  pilihan_status_anime[int(status_baru) - 1],
                                                  int(tahun_baru)])
                                    print("\n[+] Anime berhasil ditambahkan dengan ID " + str(id_baru) + ".")

                    input("\nTekan Enter untuk kembali ke menu admin...")

                # ---------- 2. TAMPILKAN DAFTAR ANIME ----------
                elif menu_admin == "2":

                    os.system(clear)
                    print("==============================================")
                    print("            DAFTAR ANIME")
                    print("==============================================")

                    if len(anime) == 0:
                        print(" Belum ada data anime.")
                    else:
                        print("----------------------------------------------------------------------")
                        print(" ID  | JUDUL                     | GENRE       | EPS  | STATUS    | THN")
                        print("----------------------------------------------------------------------")
                        for baris in anime:
                            print(" " + str(baris[0]).ljust(3) + " | "
                                  + str(baris[1][:25]).ljust(25) + " | "
                                  + str(baris[2]).ljust(11) + " | "
                                  + str(baris[3]).ljust(4) + " | "
                                  + str(baris[4]).ljust(9) + " | "
                                  + str(baris[5]))
                        print("----------------------------------------------------------------------")
                        print(" Total anime : " + str(len(anime)))

                    input("\nTekan Enter untuk kembali ke menu admin...")

                # ---------- 3. EDIT INFORMASI ANIME ----------
                elif menu_admin == "3":

                    os.system(clear)
                    print("==============================================")
                    print("            EDIT INFORMASI ANIME")
                    print("==============================================")

                    if len(anime) == 0:
                        print(" Belum ada data anime yang bisa diedit.")
                        input("\nTekan Enter untuk kembali ke menu admin...")
                    else:
                        for baris in anime:
                            print(" ID " + str(baris[0]).ljust(3) + " : " + baris[1])
                        print("----------------------------------------------")
                        id_edit = input("Masukkan ID anime yang akan diedit : ")

                        if id_edit.isdigit() == False:
                            print("\n[!] ID harus berupa angka.")
                            input("\nTekan Enter untuk kembali ke menu admin...")
                        else:
                            index_edit = -1
                            for i in range(len(anime)):
                                if anime[i][0] == int(id_edit):
                                    index_edit = i

                            if index_edit == -1:
                                print("\n[!] Anime dengan ID " + id_edit + " tidak ditemukan.")
                                input("\nTekan Enter untuk kembali ke menu admin...")
                            else:

                                edit_jalan = True
                                while edit_jalan:

                                    os.system(clear)
                                    print("==============================================")
                                    print("            EDIT INFORMASI ANIME")
                                    print("==============================================")
                                    print(" 1. Judul   : " + str(anime[index_edit][1]))
                                    print(" 2. Genre   : " + str(anime[index_edit][2]))
                                    print(" 3. Episode : " + str(anime[index_edit][3]))
                                    print(" 4. Status  : " + str(anime[index_edit][4]))
                                    print(" 5. Tahun   : " + str(anime[index_edit][5]))
                                    print("----------------------------------------------")
                                    print(" 0. Selesai / kembali")
                                    print("==============================================")
                                    pilih_edit = input("Pilih data yang akan diubah [0-5] : ")

                                    if pilih_edit == "1":
                                        nilai_baru = input("Judul baru   : ")
                                        if nilai_baru == "":
                                            print("\n[!] Judul tidak boleh kosong.")
                                        else:
                                            anime[index_edit][1] = nilai_baru
                                            print("\n[+] Judul berhasil diubah.")
                                        input("Tekan Enter...")

                                    elif pilih_edit == "2":
                                        nilai_baru = input("Genre baru   : ")
                                        if nilai_baru == "":
                                            print("\n[!] Genre tidak boleh kosong.")
                                        else:
                                            anime[index_edit][2] = nilai_baru
                                            print("\n[+] Genre berhasil diubah.")
                                        input("Tekan Enter...")

                                    elif pilih_edit == "3":
                                        nilai_baru = input("Episode baru : ")
                                        if nilai_baru.isdigit() == False:
                                            print("\n[!] Episode harus berupa angka.")
                                        else:
                                            anime[index_edit][3] = int(nilai_baru)
                                            print("\n[+] Jumlah episode berhasil diubah.")
                                        input("Tekan Enter...")

                                    elif pilih_edit == "4":
                                        print("----------------------------------------------")
                                        for i in range(len(pilihan_status_anime)):
                                            print("  " + str(i + 1) + ". " + pilihan_status_anime[i])
                                        nilai_baru = input("Status baru [1/2/3] : ")
                                        if nilai_baru != "1" and nilai_baru != "2" and nilai_baru != "3":
                                            print("\n[!] Pilihan status tidak tersedia.")
                                        else:
                                            anime[index_edit][4] = pilihan_status_anime[int(nilai_baru) - 1]
                                            print("\n[+] Status berhasil diubah.")
                                        input("Tekan Enter...")

                                    elif pilih_edit == "5":
                                        nilai_baru = input("Tahun baru   : ")
                                        if nilai_baru.isdigit() == False:
                                            print("\n[!] Tahun harus berupa angka.")
                                        else:
                                            anime[index_edit][5] = int(nilai_baru)
                                            print("\n[+] Tahun rilis berhasil diubah.")
                                        input("Tekan Enter...")

                                    elif pilih_edit == "0":
                                        edit_jalan = False

                                    else:
                                        print("\n[!] Pilihan tidak tersedia.")
                                        input("Tekan Enter...")

                # ---------- 4. HAPUS ANIME ----------
                elif menu_admin == "4":

                    os.system(clear)
                    print("==============================================")
                    print("                HAPUS ANIME")
                    print("==============================================")

                    if len(anime) == 0:
                        print(" Belum ada data anime yang bisa dihapus.")
                        input("\nTekan Enter untuk kembali ke menu admin...")
                    else:
                        for baris in anime:
                            print(" ID " + str(baris[0]).ljust(3) + " : " + baris[1])
                        print("----------------------------------------------")
                        id_hapus = input("Masukkan ID anime yang akan dihapus : ")

                        if id_hapus.isdigit() == False:
                            print("\n[!] ID harus berupa angka.")
                            input("\nTekan Enter untuk kembali ke menu admin...")
                        else:
                            index_hapus = -1
                            for i in range(len(anime)):
                                if anime[i][0] == int(id_hapus):
                                    index_hapus = i

                            if index_hapus == -1:
                                print("\n[!] Anime dengan ID " + id_hapus + " tidak ditemukan.")
                                input("\nTekan Enter untuk kembali ke menu admin...")
                            else:
                                print("----------------------------------------------")
                                print(" Judul  : " + str(anime[index_hapus][1]))
                                print(" Genre  : " + str(anime[index_hapus][2]))
                                print("----------------------------------------------")
                                yakin = input("Yakin ingin menghapus data ini? [y/n] : ")

                                if yakin == "y" or yakin == "Y":
                                    judul_terhapus = anime[index_hapus][1]
                                    anime.pop(index_hapus)

                                    i = 0
                                    while i < len(watchlist):
                                        if watchlist[i][1] == int(id_hapus):
                                            watchlist.pop(i)
                                        else:
                                            i = i + 1

                                    print("\n[+] Anime '" + judul_terhapus + "' berhasil dihapus.")
                                else:
                                    print("\n[*] Penghapusan dibatalkan.")

                                input("\nTekan Enter untuk kembali ke menu admin...")

                # ---------- 5. LOGOUT ----------
                elif menu_admin == "5":
                    print("\n[*] Logout berhasil, kembali ke menu utama.")
                    sesi_admin = False
                    input("Tekan Enter untuk melanjutkan...")

                # ---------- input salah ----------
                else:
                    print("\n[!] Pilihan tidak tersedia, silakan pilih 1 sampai 5.")
                    input("Tekan Enter untuk melanjutkan...")

        # =============================================================
        # SESI PENGGUNA (USER)
        # =============================================================
        elif berhasil_login == True and role == "user":

            sesi_user = True
            while sesi_user:

                os.system(clear)
                print("==============================================")
                print("               MENU PENGGUNA")
                print("  User : " + user_aktif)
                print("==============================================")
                print(" 1. Tampilkan Daftar Anime")
                print(" 2. Tambah Anime ke Watchlist")
                print(" 3. Tampilkan Watchlist Saya")
                print(" 4. Edit Status Watchlist")
                print(" 5. Hapus Anime dari Watchlist")
                print(" 6. Logout")
                print("==============================================")
                menu_user = input("Pilih menu [1/2/3/4/5/6] : ")

                # ---------- 1. TAMPILKAN DAFTAR ANIME ----------
                if menu_user == "1":

                    os.system(clear)
                    print("==============================================")
                    print("            DAFTAR ANIME")
                    print("==============================================")

                    if len(anime) == 0:
                        print(" Belum ada data anime.")
                    else:
                        print("----------------------------------------------------------------------")
                        print(" ID  | JUDUL                     | GENRE       | EPS  | STATUS    | THN")
                        print("----------------------------------------------------------------------")
                        for baris in anime:
                            print(" " + str(baris[0]).ljust(3) + " | "
                                  + str(baris[1][:25]).ljust(25) + " | "
                                  + str(baris[2]).ljust(11) + " | "
                                  + str(baris[3]).ljust(4) + " | "
                                  + str(baris[4]).ljust(9) + " | "
                                  + str(baris[5]))
                        print("----------------------------------------------------------------------")
                        print(" Total anime : " + str(len(anime)))

                    input("\nTekan Enter untuk kembali ke menu pengguna...")

                # ---------- 2. TAMBAH KE WATCHLIST ----------
                elif menu_user == "2":

                    os.system(clear)
                    print("==============================================")
                    print("          TAMBAH KE WATCHLIST")
                    print("==============================================")

                    if len(anime) == 0:
                        print(" Belum ada data anime.")
                        input("\nTekan Enter untuk kembali ke menu pengguna...")
                    else:
                        for baris in anime:
                            print(" ID " + str(baris[0]).ljust(3) + " : " + baris[1])
                        print("----------------------------------------------")
                        id_tambah = input("Masukkan ID anime : ")

                        if id_tambah.isdigit() == False:
                            print("\n[!] ID harus berupa angka.")
                            input("\nTekan Enter untuk kembali ke menu pengguna...")
                        else:
                            index_anime = -1
                            for i in range(len(anime)):
                                if anime[i][0] == int(id_tambah):
                                    index_anime = i

                            if index_anime == -1:
                                print("\n[!] Anime dengan ID " + id_tambah + " tidak ditemukan.")
                                input("\nTekan Enter untuk kembali ke menu pengguna...")
                            else:
                                sudah_ada = False
                                for baris in watchlist:
                                    if baris[0] == user_aktif and baris[1] == int(id_tambah):
                                        sudah_ada = True

                                if sudah_ada == True:
                                    print("\n[!] Anime sudah ada di watchlist Anda.")
                                    input("\nTekan Enter untuk kembali ke menu pengguna...")
                                else:
                                    print("----------------------------------------------")
                                    print(" Pilihan status tontonan :")
                                    for i in range(len(pilihan_status_watchlist)):
                                        print("  " + str(i + 1) + ". " + pilihan_status_watchlist[i])
                                    status_tonton = input("Status awal [1/2/3] : ")

                                    if status_tonton != "1" and status_tonton != "2" and status_tonton != "3":
                                        print("\n[!] Pilihan status tidak tersedia, data batal disimpan.")
                                    else:
                                        watchlist.append([user_aktif, int(id_tambah),
                                                          pilihan_status_watchlist[int(status_tonton) - 1]])
                                        print("\n[+] '" + str(anime[index_anime][1]) + "' berhasil ditambahkan ke watchlist.")

                                    input("\nTekan Enter untuk kembali ke menu pengguna...")

                # ---------- 3. TAMPILKAN WATCHLIST ----------
                elif menu_user == "3":

                    os.system(clear)
                    print("==============================================")
                    print("            WATCHLIST SAYA")
                    print("  User : " + user_aktif)
                    print("==============================================")

                    punya = 0
                    for baris in watchlist:
                        if baris[0] == user_aktif:
                            punya = punya + 1

                    if punya == 0:
                        print(" Watchlist Anda masih kosong.")
                    else:
                        print("----------------------------------------------------------------------")
                        print(" NO | JUDUL                     | GENRE       | STATUS")
                        print("----------------------------------------------------------------------")
                        nomor = 0
                        for baris in watchlist:
                            if baris[0] == user_aktif:
                                nomor = nomor + 1
                                judul_tampil = "-"
                                genre_tampil = "-"
                                for a in anime:
                                    if a[0] == baris[1]:
                                        judul_tampil = a[1]
                                        genre_tampil = a[2]
                                print(" " + str(nomor).ljust(2) + " | "
                                      + str(judul_tampil[:25]).ljust(25) + " | "
                                      + str(genre_tampil).ljust(11) + " | "
                                      + str(baris[2]))
                        print("----------------------------------------------------------------------")
                        print(" Total watchlist : " + str(punya))

                    input("\nTekan Enter untuk kembali ke menu pengguna...")

                # ---------- 4. EDIT STATUS WATCHLIST ----------
                elif menu_user == "4":

                    os.system(clear)
                    print("==============================================")
                    print("          EDIT STATUS WATCHLIST")
                    print("==============================================")

                    punya = 0
                    for baris in watchlist:
                        if baris[0] == user_aktif:
                            punya = punya + 1

                    if punya == 0:
                        print(" Watchlist Anda masih kosong.")
                        input("\nTekan Enter untuk kembali ke menu pengguna...")
                    else:
                        nomor = 0
                        index_watchlist = []
                        for baris in range(len(watchlist)):
                            if watchlist[baris][0] == user_aktif:
                                nomor = nomor + 1
                                index_watchlist.append(baris)
                                judul_tampil = "-"
                                for a in anime:
                                    if a[0] == watchlist[baris][1]:
                                        judul_tampil = a[1]
                                print(" " + str(nomor) + ". " + str(judul_tampil)
                                      + "  [" + str(watchlist[baris][2]) + "]")
                        print("----------------------------------------------")
                        no_edit = input("Pilih nomor watchlist : ")

                        if no_edit.isdigit() == False:
                            print("\n[!] Nomor harus berupa angka.")
                            input("\nTekan Enter untuk kembali ke menu pengguna...")
                        elif int(no_edit) < 1 or int(no_edit) > len(index_watchlist):
                            print("\n[!] Nomor " + no_edit + " tidak ada di watchlist Anda.")
                            input("\nTekan Enter untuk kembali ke menu pengguna...")
                        else:
                            print("----------------------------------------------")
                            print(" Pilihan status tontonan :")
                            for i in range(len(pilihan_status_watchlist)):
                                print("  " + str(i + 1) + ". " + pilihan_status_watchlist[i])
                            status_tonton = input("Status baru [1/2/3] : ")

                            if status_tonton != "1" and status_tonton != "2" and status_tonton != "3":
                                print("\n[!] Pilihan status tidak tersedia.")
                            else:
                                watchlist[index_watchlist[int(no_edit) - 1]][2] = pilihan_status_watchlist[int(status_tonton) - 1]
                                print("\n[+] Status watchlist berhasil diubah.")

                            input("\nTekan Enter untuk kembali ke menu pengguna...")

                # ---------- 5. HAPUS DARI WATCHLIST ----------
                elif menu_user == "5":

                    os.system(clear)
                    print("==============================================")
                    print("        HAPUS ANIME DARI WATCHLIST")
                    print("==============================================")

                    punya = 0
                    for baris in watchlist:
                        if baris[0] == user_aktif:
                            punya = punya + 1

                    if punya == 0:
                        print(" Watchlist Anda masih kosong.")
                        input("\nTekan Enter untuk kembali ke menu pengguna...")
                    else:
                        nomor = 0
                        index_watchlist = []
                        for baris in range(len(watchlist)):
                            if watchlist[baris][0] == user_aktif:
                                nomor = nomor + 1
                                index_watchlist.append(baris)
                                judul_tampil = "-"
                                for a in anime:
                                    if a[0] == watchlist[baris][1]:
                                        judul_tampil = a[1]
                                print(" " + str(nomor) + ". " + str(judul_tampil)
                                      + "  [" + str(watchlist[baris][2]) + "]")
                        print("----------------------------------------------")
                        no_hapus = input("Pilih nomor watchlist : ")

                        if no_hapus.isdigit() == False:
                            print("\n[!] Nomor harus berupa angka.")
                            input("\nTekan Enter untuk kembali ke menu pengguna...")
                        elif int(no_hapus) < 1 or int(no_hapus) > len(index_watchlist):
                            print("\n[!] Nomor " + no_hapus + " tidak ada di watchlist Anda.")
                            input("\nTekan Enter untuk kembali ke menu pengguna...")
                        else:
                            yakin = input("Yakin ingin menghapus dari watchlist? [y/n] : ")
                            if yakin == "y" or yakin == "Y":
                                watchlist.pop(index_watchlist[int(no_hapus) - 1])
                                print("\n[+] Anime berhasil dihapus dari watchlist.")
                            else:
                                print("\n[*] Penghapusan dibatalkan.")

                            input("\nTekan Enter untuk kembali ke menu pengguna...")

                # ---------- 6. LOGOUT ----------
                elif menu_user == "6":
                    print("\n[*] Logout berhasil, kembali ke menu utama.")
                    sesi_user = False
                    input("Tekan Enter untuk melanjutkan...")

                # ---------- input salah ----------
                else:
                    print("\n[!] Pilihan tidak tersedia, silakan pilih 1 sampai 6.")
                    input("Tekan Enter untuk melanjutkan...")

    # =================================================================
    # MENU 2 : REGISTER
    # =================================================================
    elif menu_utama == "2":

        register_jalan = True
        while register_jalan:

            os.system(clear)
            print("==============================================")
            print("                 REGISTER")
            print("==============================================")
            username_baru = input("Username baru : ")

            if username_baru == "":
                print("\n[!] Username tidak boleh kosong.")
            elif username_baru == admin_username:
                print("\n[!] Username tersebut tidak boleh digunakan.")
            else:
                username_dipakai = False
                for baris in akun:
                    if baris[0] == username_baru:
                        username_dipakai = True

                if username_dipakai == True:
                    print("\n[!] Username sudah terdaftar, silakan gunakan username lain.")
                else:
                    password_baru = input("Password      : ")

                    if password_baru == "":
                        print("\n[!] Password tidak boleh kosong.")
                    elif len(password_baru) < 4:
                        print("\n[!] Password minimal 4 karakter.")
                    else:
                        password_konfirmasi = input("Ulangi password: ")
                        if password_konfirmasi != password_baru:
                            print("\n[!] Konfirmasi password tidak sama.")
                        else:
                            akun.append([username_baru, password_baru])
                            print("\n[+] Register berhasil! Akun '" + username_baru + "' sudah bisa digunakan.")
                            register_jalan = False

            if register_jalan == True:
                ulang = input("\nCoba register lagi? [y/n] : ")
                if ulang == "n" or ulang == "N":
                    register_jalan = False

        input("\nTekan Enter untuk kembali ke menu utama...")

    # =================================================================
    # MENU 3 : KELUAR
    # =================================================================
    elif menu_utama == "3":
        os.system(clear)
        print("==============================================")
        print("   Terima kasih telah menggunakan program")
        print("        SISTEM STREAMING ANIME")
        print("==============================================")
        program_jalan = False

    # =================================================================
    # INPUT TIDAK VALID
    # =================================================================
    else:
        print("\n[!] Pilihan '" + menu_utama + "' tidak tersedia.")
        print("    Silakan pilih menu 1, 2, atau 3.")
        input("Tekan Enter untuk melanjutkan...")
