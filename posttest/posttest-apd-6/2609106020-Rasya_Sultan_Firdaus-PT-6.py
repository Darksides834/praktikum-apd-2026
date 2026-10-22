# =====================================================================
# PROGRAM  : SISTEM STREAMING ANIME
# =====================================================================
import os

clear = "cls" if os.name == "nt" else "clear"  

# akun admin yang sudah disediakan oleh sistem
admin_username = "admin"
admin_password = "admin123"

# tempat akun pengguna: {username: password}
akun = {
    "user": "user123"
}

# data anime: {id: {judul, genre, episode, status, tahun}}
anime = {
    1: {"judul": "Naruto Shippuden", "genre": "Action",   "episode": 500,  "status": "Completed", "tahun": 2007},
    2: {"judul": "One Piece",        "genre": "Action",   "episode": 1120, "status": "Ongoing",   "tahun": 1999},
    3: {"judul": "Attack on Titan",  "genre": "Action",   "episode": 87,   "status": "Completed", "tahun": 2013},
    4: {"judul": "Spy x Family",     "genre": "Comedy",   "episode": 37,   "status": "Ongoing",   "tahun": 2022},
    5: {"judul": "Death Note",       "genre": "Thriller", "episode": 37,   "status": "Completed", "tahun": 2006},
    6: {"judul": "Dr. Stone",        "genre": "Adventure","episode": 35,   "status": "Ongoing",   "tahun": 2019},
    7: {"judul": "Konosuba",         "genre": "Comedy",   "episode": 31,   "status": "Completed", "tahun": 2016},
    8: {"judul": "Tensura",          "genre": "Adventure","episode": 96,   "status": "Ongoing",   "tahun": 2018},
    9: {"judul": "jojo's Bizarre Adventure", "genre": "Action", "episode": 190, "status": "Ongoing", "tahun": 2012},
    10: {"judul": "Your lie in April", "genre": "Romance", "episode": 22, "status": "Completed", "tahun": 2014}
}

# data watchlist: {username: {id_anime: status_tonton}}
watchlist = {
    "user": {3: "Sudah Ditonton"}
}

# pilihan status 
pilihan_status_anime = {"1": "Ongoing", "2": "Completed", "3": "Hiatus"}
pilihan_status_watchlist = {"1": "Belum Ditonton", "2": "Rencana", "3": "Sudah Ditonton"}

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
                    ketemu = False
                    if input_username in akun and akun[input_username] == input_password:
                        ketemu = True

                    if ketemu == False:
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
                            for kunci in pilihan_status_anime:
                                print("  " + kunci + ". " + pilihan_status_anime[kunci])
                            status_baru = input("Status [1/2/3]   : ")

                            if status_baru not in pilihan_status_anime:
                                print("\n[!] Pilihan status tidak tersedia, data batal disimpan.")
                            else:
                                tahun_baru = input("Tahun rilis      : ")
                                if tahun_baru.isdigit() == False:
                                    print("\n[!] Tahun rilis harus angka, data batal disimpan.")
                                else:
                                    id_baru = 1
                                    for id_anime in anime:
                                        if id_anime >= id_baru:
                                            id_baru = id_anime + 1
                                    anime[id_baru] = {
                                        "judul": judul_baru,
                                        "genre": genre_baru,
                                        "episode": int(episode_baru),
                                        "status": pilihan_status_anime[status_baru],
                                        "tahun": int(tahun_baru)
                                    }
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
                        for id_anime in anime:
                            data = anime[id_anime]
                            print(" " + str(id_anime).ljust(3) + " | "
                                  + str(data["judul"][:25]).ljust(25) + " | "
                                  + str(data["genre"]).ljust(11) + " | "
                                  + str(data["episode"]).ljust(4) + " | "
                                  + str(data["status"]).ljust(9) + " | "
                                  + str(data["tahun"]))
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
                        for id_anime in anime:
                            print(" ID " + str(id_anime).ljust(3) + " : " + anime[id_anime]["judul"])
                        print("----------------------------------------------")
                        id_edit = input("Masukkan ID anime yang akan diedit : ")

                        if id_edit.isdigit() == False:
                            print("\n[!] ID harus berupa angka.")
                            input("\nTekan Enter untuk kembali ke menu admin...")
                        else:
                            if int(id_edit) not in anime:
                                print("\n[!] Anime dengan ID " + id_edit + " tidak ditemukan.")
                                input("\nTekan Enter untuk kembali ke menu admin...")
                            else:

                                id_edit_angka = int(id_edit)
                                edit_jalan = True
                                while edit_jalan:

                                    os.system(clear)
                                    print("==============================================")
                                    print("            EDIT INFORMASI ANIME")
                                    print("==============================================")
                                    print(" 1. Judul   : " + str(anime[id_edit_angka]["judul"]))
                                    print(" 2. Genre   : " + str(anime[id_edit_angka]["genre"]))
                                    print(" 3. Episode : " + str(anime[id_edit_angka]["episode"]))
                                    print(" 4. Status  : " + str(anime[id_edit_angka]["status"]))
                                    print(" 5. Tahun   : " + str(anime[id_edit_angka]["tahun"]))
                                    print("----------------------------------------------")
                                    print(" 0. Selesai / kembali")
                                    print("==============================================")
                                    pilih_edit = input("Pilih data yang akan diubah [0-5] : ")

                                    if pilih_edit == "1":
                                        nilai_baru = input("Judul baru   : ")
                                        if nilai_baru == "":
                                            print("\n[!] Judul tidak boleh kosong.")
                                        else:
                                            anime[id_edit_angka]["judul"] = nilai_baru
                                            print("\n[+] Judul berhasil diubah.")
                                        input("Tekan Enter...")

                                    elif pilih_edit == "2":
                                        nilai_baru = input("Genre baru   : ")
                                        if nilai_baru == "":
                                            print("\n[!] Genre tidak boleh kosong.")
                                        else:
                                            anime[id_edit_angka]["genre"] = nilai_baru
                                            print("\n[+] Genre berhasil diubah.")
                                        input("Tekan Enter...")

                                    elif pilih_edit == "3":
                                        nilai_baru = input("Episode baru : ")
                                        if nilai_baru.isdigit() == False:
                                            print("\n[!] Episode harus berupa angka.")
                                        else:
                                            anime[id_edit_angka]["episode"] = int(nilai_baru)
                                            print("\n[+] Jumlah episode berhasil diubah.")
                                        input("Tekan Enter...")

                                    elif pilih_edit == "4":
                                        print("----------------------------------------------")
                                        for kunci in pilihan_status_anime:
                                            print("  " + kunci + ". " + pilihan_status_anime[kunci])
                                        nilai_baru = input("Status baru [1/2/3] : ")
                                        if nilai_baru not in pilihan_status_anime:
                                            print("\n[!] Pilihan status tidak tersedia.")
                                        else:
                                            anime[id_edit_angka]["status"] = pilihan_status_anime[nilai_baru]
                                            print("\n[+] Status berhasil diubah.")
                                        input("Tekan Enter...")

                                    elif pilih_edit == "5":
                                        nilai_baru = input("Tahun baru   : ")
                                        if nilai_baru.isdigit() == False:
                                            print("\n[!] Tahun harus berupa angka.")
                                        else:
                                            anime[id_edit_angka]["tahun"] = int(nilai_baru)
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
                        for id_anime in anime:
                            print(" ID " + str(id_anime).ljust(3) + " : " + anime[id_anime]["judul"])
                        print("----------------------------------------------")
                        id_hapus = input("Masukkan ID anime yang akan dihapus : ")

                        if id_hapus.isdigit() == False:
                            print("\n[!] ID harus berupa angka.")
                            input("\nTekan Enter untuk kembali ke menu admin...")
                        else:
                            if int(id_hapus) not in anime:
                                print("\n[!] Anime dengan ID " + id_hapus + " tidak ditemukan.")
                                input("\nTekan Enter untuk kembali ke menu admin...")
                            else:
                                print("----------------------------------------------")
                                print(" Judul  : " + str(anime[int(id_hapus)]["judul"]))
                                print(" Genre  : " + str(anime[int(id_hapus)]["genre"]))
                                print("----------------------------------------------")
                                yakin = input("Yakin ingin menghapus data ini? [y/n] : ")

                                if yakin == "y" or yakin == "Y":
                                    judul_terhapus = anime[int(id_hapus)]["judul"]
                                    anime.pop(int(id_hapus))

                                    for nama_user in watchlist:
                                        if int(id_hapus) in watchlist[nama_user]:
                                            watchlist[nama_user].pop(int(id_hapus))

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
                        for id_anime in anime:
                            data = anime[id_anime]
                            print(" " + str(id_anime).ljust(3) + " | "
                                  + str(data["judul"][:25]).ljust(25) + " | "
                                  + str(data["genre"]).ljust(11) + " | "
                                  + str(data["episode"]).ljust(4) + " | "
                                  + str(data["status"]).ljust(9) + " | "
                                  + str(data["tahun"]))
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
                        for id_anime in anime:
                            print(" ID " + str(id_anime).ljust(3) + " : " + anime[id_anime]["judul"])
                        print("----------------------------------------------")
                        id_tambah = input("Masukkan ID anime : ")

                        if id_tambah.isdigit() == False:
                            print("\n[!] ID harus berupa angka.")
                            input("\nTekan Enter untuk kembali ke menu pengguna...")
                        else:
                            if int(id_tambah) not in anime:
                                print("\n[!] Anime dengan ID " + id_tambah + " tidak ditemukan.")
                                input("\nTekan Enter untuk kembali ke menu pengguna...")
                            else:
                                sudah_ada = False
                                if int(id_tambah) in watchlist[user_aktif]:
                                    sudah_ada = True

                                if sudah_ada == True:
                                    print("\n[!] Anime sudah ada di watchlist Anda.")
                                    input("\nTekan Enter untuk kembali ke menu pengguna...")
                                else:
                                    print("----------------------------------------------")
                                    print(" Pilihan status tontonan :")
                                    for kunci in pilihan_status_watchlist:
                                        print("  " + kunci + ". " + pilihan_status_watchlist[kunci])
                                    status_tonton = input("Status awal [1/2/3] : ")

                                    if status_tonton not in pilihan_status_watchlist:
                                        print("\n[!] Pilihan status tidak tersedia, data batal disimpan.")
                                    else:
                                        watchlist[user_aktif][int(id_tambah)] = pilihan_status_watchlist[status_tonton]
                                        print("\n[+] '" + str(anime[int(id_tambah)]["judul"]) + "' berhasil ditambahkan ke watchlist.")

                                    input("\nTekan Enter untuk kembali ke menu pengguna...")

                # ---------- 3. TAMPILKAN WATCHLIST ----------
                elif menu_user == "3":

                    os.system(clear)
                    print("==============================================")
                    print("            WATCHLIST SAYA")
                    print("  User : " + user_aktif)
                    print("==============================================")

                    punya = len(watchlist[user_aktif])

                    if punya == 0:
                        print(" Watchlist Anda masih kosong.")
                    else:
                        print("----------------------------------------------------------------------")
                        print(" NO | JUDUL                     | GENRE       | STATUS")
                        print("----------------------------------------------------------------------")
                        nomor = 0
                        for id_anime in watchlist[user_aktif]:
                            nomor = nomor + 1
                            judul_tampil = "-"
                            genre_tampil = "-"
                            if id_anime in anime:
                                judul_tampil = anime[id_anime]["judul"]
                                genre_tampil = anime[id_anime]["genre"]
                            print(" " + str(nomor).ljust(2) + " | "
                                  + str(judul_tampil[:25]).ljust(25) + " | "
                                  + str(genre_tampil).ljust(11) + " | "
                                  + str(watchlist[user_aktif][id_anime]))
                        print("----------------------------------------------------------------------")
                        print(" Total watchlist : " + str(punya))

                    input("\nTekan Enter untuk kembali ke menu pengguna...")

                # ---------- 4. EDIT STATUS WATCHLIST ----------
                elif menu_user == "4":

                    os.system(clear)
                    print("==============================================")
                    print("          EDIT STATUS WATCHLIST")
                    print("==============================================")

                    punya = len(watchlist[user_aktif])

                    if punya == 0:
                        print(" Watchlist Anda masih kosong.")
                        input("\nTekan Enter untuk kembali ke menu pengguna...")
                    else:
                        nomor = 0
                        index_watchlist = []
                        for id_anime in watchlist[user_aktif]:
                            nomor = nomor + 1
                            index_watchlist.append(id_anime)
                            judul_tampil = "-"
                            if id_anime in anime:
                                judul_tampil = anime[id_anime]["judul"]
                            print(" " + str(nomor) + ". " + str(judul_tampil)
                                  + "  [" + str(watchlist[user_aktif][id_anime]) + "]")
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
                            for kunci in pilihan_status_watchlist:
                                print("  " + kunci + ". " + pilihan_status_watchlist[kunci])
                            status_tonton = input("Status baru [1/2/3] : ")

                            if status_tonton not in pilihan_status_watchlist:
                                print("\n[!] Pilihan status tidak tersedia.")
                            else:
                                watchlist[user_aktif][index_watchlist[int(no_edit) - 1]] = pilihan_status_watchlist[status_tonton]
                                print("\n[+] Status watchlist berhasil diubah.")

                            input("\nTekan Enter untuk kembali ke menu pengguna...")

                # ---------- 5. HAPUS DARI WATCHLIST ----------
                elif menu_user == "5":

                    os.system(clear)
                    print("==============================================")
                    print("        HAPUS ANIME DARI WATCHLIST")
                    print("==============================================")

                    punya = len(watchlist[user_aktif])

                    if punya == 0:
                        print(" Watchlist Anda masih kosong.")
                        input("\nTekan Enter untuk kembali ke menu pengguna...")
                    else:
                        nomor = 0
                        index_watchlist = []
                        for id_anime in watchlist[user_aktif]:
                            nomor = nomor + 1
                            index_watchlist.append(id_anime)
                            judul_tampil = "-"
                            if id_anime in anime:
                                judul_tampil = anime[id_anime]["judul"]
                            print(" " + str(nomor) + ". " + str(judul_tampil)
                                  + "  [" + str(watchlist[user_aktif][id_anime]) + "]")
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
                                watchlist[user_aktif].pop(index_watchlist[int(no_hapus) - 1])
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
                if username_baru in akun:
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
                            akun[username_baru] = password_baru
                            watchlist[username_baru] = {}
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