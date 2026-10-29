# =====================================================================
# PROGRAM  : SISTEM STREAMING ANIME (POSTTEST 7)
# =====================================================================
import os

# ---------------------------------------------------------------------
# VARIABEL GLOBAL
# ---------------------------------------------------------------------
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


# =====================================================================
# FUNGSI DENGAN PARAMETER
# =====================================================================
def ke_angka(teks):
    try:
        if teks.isdigit() == False:
            raise ValueError
        hasil = int(teks)
        return hasil
    except ValueError:
        return None


def validasi_login(username, password, data_akun):
    try:
        if username in data_akun and data_akun[username] == password:
            return True
        return False
    except TypeError:
        return False


def id_berikutnya(daftar_id, indeks):
    if indeks == len(daftar_id):
        return 1
    terbesar_lain = id_berikutnya(daftar_id, indeks + 1)
    kandidat = daftar_id[indeks] + 1
    if kandidat > terbesar_lain:
        return kandidat
    return terbesar_lain


def ambil_watchlist(nama_user):
    try:
        return watchlist[nama_user]
    except KeyError:
        watchlist[nama_user] = {}
        return watchlist[nama_user]


def daftar_nomor_watchlist(nama_user):
    data_watch = ambil_watchlist(nama_user)
    nomor = 0
    index_watchlist = []
    for id_anime in data_watch:
        nomor = nomor + 1
        index_watchlist.append(id_anime)
        judul_tampil = "-"
        if id_anime in anime:
            judul_tampil = anime[id_anime]["judul"]
        print(" " + str(nomor) + ". " + str(judul_tampil)
              + "  [" + str(data_watch[id_anime]) + "]")
    return index_watchlist


# =====================================================================
# FUNGSI TANPA PARAMETER
# =====================================================================
def jumlah_anime():
    return len(anime)


def input_kredensial():
    username_input = input("Username : ")
    password_input = input("Password : ")
    return username_input, password_input


# =====================================================================
# PROSEDUR
# =====================================================================
def bersihkan_layar():
    os.system(clear)


def jeda(pesan):
    input(pesan)


def tampil_daftar_anime():
    bersihkan_layar()
    print("==============================================")
    print("            DAFTAR ANIME")
    print("==============================================")

    if jumlah_anime() == 0:
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
        print(" Total anime : " + str(jumlah_anime()))


def tampil_watchlist(user_aktif):
    bersihkan_layar()
    print("==============================================")
    print("            WATCHLIST SAYA")
    print("  User : " + user_aktif)
    print("==============================================")

    data_watch = ambil_watchlist(user_aktif)
    punya = len(data_watch)

    if punya == 0:
        print(" Watchlist Anda masih kosong.")
    else:
        print("----------------------------------------------------------------------")
        print(" NO | JUDUL                     | GENRE       | STATUS")
        print("----------------------------------------------------------------------")
        nomor = 0
        for id_anime in data_watch:
            nomor = nomor + 1
            judul_tampil = "-"
            genre_tampil = "-"
            if id_anime in anime:
                judul_tampil = anime[id_anime]["judul"]
                genre_tampil = anime[id_anime]["genre"]
            print(" " + str(nomor).ljust(2) + " | "
                  + str(judul_tampil[:25]).ljust(25) + " | "
                  + str(genre_tampil).ljust(11) + " | "
                  + str(data_watch[id_anime]))
        print("----------------------------------------------------------------------")
        print(" Total watchlist : " + str(punya))


# ---------------------------------------------------------------------
# PROSEDUR ADMIN
# ---------------------------------------------------------------------
def tambah_anime():
    bersihkan_layar()
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

        episode_baru = ke_angka(input("Jumlah episode   : "))
        if episode_baru == None:
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
                tahun_baru = ke_angka(input("Tahun rilis      : "))
                if tahun_baru == None:
                    print("\n[!] Tahun rilis harus angka, data batal disimpan.")
                else:
                    id_baru = id_berikutnya(list(anime.keys()), 0)
                    anime[id_baru] = {
                        "judul": judul_baru,
                        "genre": genre_baru,
                        "episode": episode_baru,
                        "status": pilihan_status_anime[status_baru],
                        "tahun": tahun_baru
                    }
                    print("\n[+] Anime berhasil ditambahkan dengan ID " + str(id_baru) + ".")

    jeda("\nTekan Enter untuk kembali ke menu admin...")


def edit_anime():
    bersihkan_layar()
    print("==============================================")
    print("            EDIT INFORMASI ANIME")
    print("==============================================")

    if jumlah_anime() == 0:
        print(" Belum ada data anime yang bisa diedit.")
        jeda("\nTekan Enter untuk kembali ke menu admin...")
        return

    for id_anime in anime:
        print(" ID " + str(id_anime).ljust(3) + " : " + anime[id_anime]["judul"])
    print("----------------------------------------------")
    id_edit = input("Masukkan ID anime yang akan diedit : ")
    id_edit_angka = ke_angka(id_edit)

    if id_edit_angka == None:
        print("\n[!] ID harus berupa angka.")
        jeda("\nTekan Enter untuk kembali ke menu admin...")
        return

    if id_edit_angka not in anime:
        print("\n[!] Anime dengan ID " + id_edit + " tidak ditemukan.")
        jeda("\nTekan Enter untuk kembali ke menu admin...")
        return

    edit_jalan = True
    while edit_jalan:

        bersihkan_layar()
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
            jeda("Tekan Enter...")

        elif pilih_edit == "2":
            nilai_baru = input("Genre baru   : ")
            if nilai_baru == "":
                print("\n[!] Genre tidak boleh kosong.")
            else:
                anime[id_edit_angka]["genre"] = nilai_baru
                print("\n[+] Genre berhasil diubah.")
            jeda("Tekan Enter...")

        elif pilih_edit == "3":
            nilai_baru = ke_angka(input("Episode baru : "))
            if nilai_baru == None:
                print("\n[!] Episode harus berupa angka.")
            else:
                anime[id_edit_angka]["episode"] = nilai_baru
                print("\n[+] Jumlah episode berhasil diubah.")
            jeda("Tekan Enter...")

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
            jeda("Tekan Enter...")

        elif pilih_edit == "5":
            nilai_baru = ke_angka(input("Tahun baru   : "))
            if nilai_baru == None:
                print("\n[!] Tahun harus berupa angka.")
            else:
                anime[id_edit_angka]["tahun"] = nilai_baru
                print("\n[+] Tahun rilis berhasil diubah.")
            jeda("Tekan Enter...")

        elif pilih_edit == "0":
            edit_jalan = False

        else:
            print("\n[!] Pilihan tidak tersedia.")
            jeda("Tekan Enter...")


def hapus_anime():
    bersihkan_layar()
    print("==============================================")
    print("                HAPUS ANIME")
    print("==============================================")

    if jumlah_anime() == 0:
        print(" Belum ada data anime yang bisa dihapus.")
        jeda("\nTekan Enter untuk kembali ke menu admin...")
        return

    for id_anime in anime:
        print(" ID " + str(id_anime).ljust(3) + " : " + anime[id_anime]["judul"])
    print("----------------------------------------------")
    id_hapus = input("Masukkan ID anime yang akan dihapus : ")
    id_hapus_angka = ke_angka(id_hapus)

    if id_hapus_angka == None:
        print("\n[!] ID harus berupa angka.")
        jeda("\nTekan Enter untuk kembali ke menu admin...")
        return

    if id_hapus_angka not in anime:
        print("\n[!] Anime dengan ID " + id_hapus + " tidak ditemukan.")
        jeda("\nTekan Enter untuk kembali ke menu admin...")
        return

    print("----------------------------------------------")
    print(" Judul  : " + str(anime[id_hapus_angka]["judul"]))
    print(" Genre  : " + str(anime[id_hapus_angka]["genre"]))
    print("----------------------------------------------")
    yakin = input("Yakin ingin menghapus data ini? [y/n] : ")

    if yakin == "y" or yakin == "Y":
        judul_terhapus = anime[id_hapus_angka]["judul"]
        anime.pop(id_hapus_angka)

        for nama_user in watchlist:
            if id_hapus_angka in watchlist[nama_user]:
                watchlist[nama_user].pop(id_hapus_angka)

        print("\n[+] Anime '" + judul_terhapus + "' berhasil dihapus.")
    else:
        print("\n[*] Penghapusan dibatalkan.")

    jeda("\nTekan Enter untuk kembali ke menu admin...")


# ---------------------------------------------------------------------
# PROSEDUR PENGGUNA (WATCHLIST)
# ---------------------------------------------------------------------
def tambah_watchlist(user_aktif):
    bersihkan_layar()
    print("==============================================")
    print("          TAMBAH KE WATCHLIST")
    print("==============================================")

    if jumlah_anime() == 0:
        print(" Belum ada data anime.")
        jeda("\nTekan Enter untuk kembali ke menu pengguna...")
        return

    for id_anime in anime:
        print(" ID " + str(id_anime).ljust(3) + " : " + anime[id_anime]["judul"])
    print("----------------------------------------------")
    id_tambah = input("Masukkan ID anime : ")
    id_tambah_angka = ke_angka(id_tambah)

    if id_tambah_angka == None:
        print("\n[!] ID harus berupa angka.")
        jeda("\nTekan Enter untuk kembali ke menu pengguna...")
        return

    if id_tambah_angka not in anime:
        print("\n[!] Anime dengan ID " + id_tambah + " tidak ditemukan.")
        jeda("\nTekan Enter untuk kembali ke menu pengguna...")
        return

    data_watch = ambil_watchlist(user_aktif)
    if id_tambah_angka in data_watch:
        print("\n[!] Anime sudah ada di watchlist Anda.")
        jeda("\nTekan Enter untuk kembali ke menu pengguna...")
        return

    print("----------------------------------------------")
    print(" Pilihan status tontonan :")
    for kunci in pilihan_status_watchlist:
        print("  " + kunci + ". " + pilihan_status_watchlist[kunci])
    status_tonton = input("Status awal [1/2/3] : ")

    if status_tonton not in pilihan_status_watchlist:
        print("\n[!] Pilihan status tidak tersedia, data batal disimpan.")
    else:
        data_watch[id_tambah_angka] = pilihan_status_watchlist[status_tonton]
        print("\n[+] '" + str(anime[id_tambah_angka]["judul"]) + "' berhasil ditambahkan ke watchlist.")

    jeda("\nTekan Enter untuk kembali ke menu pengguna...")


def edit_watchlist(user_aktif):
    bersihkan_layar()
    print("==============================================")
    print("          EDIT STATUS WATCHLIST")
    print("==============================================")

    data_watch = ambil_watchlist(user_aktif)

    if len(data_watch) == 0:
        print(" Watchlist Anda masih kosong.")
        jeda("\nTekan Enter untuk kembali ke menu pengguna...")
        return

    index_watchlist = daftar_nomor_watchlist(user_aktif)
    print("----------------------------------------------")
    no_edit = input("Pilih nomor watchlist : ")
    no_edit_angka = ke_angka(no_edit)

    if no_edit_angka == None:
        print("\n[!] Nomor harus berupa angka.")
    elif no_edit_angka < 1 or no_edit_angka > len(index_watchlist):
        print("\n[!] Nomor " + no_edit + " tidak ada di watchlist Anda.")
    else:
        print("----------------------------------------------")
        print(" Pilihan status tontonan :")
        for kunci in pilihan_status_watchlist:
            print("  " + kunci + ". " + pilihan_status_watchlist[kunci])
        status_tonton = input("Status baru [1/2/3] : ")

        if status_tonton not in pilihan_status_watchlist:
            print("\n[!] Pilihan status tidak tersedia.")
        else:
            data_watch[index_watchlist[no_edit_angka - 1]] = pilihan_status_watchlist[status_tonton]
            print("\n[+] Status watchlist berhasil diubah.")

    jeda("\nTekan Enter untuk kembali ke menu pengguna...")


def hapus_watchlist(user_aktif):
    bersihkan_layar()
    print("==============================================")
    print("        HAPUS ANIME DARI WATCHLIST")
    print("==============================================")

    data_watch = ambil_watchlist(user_aktif)

    if len(data_watch) == 0:
        print(" Watchlist Anda masih kosong.")
        jeda("\nTekan Enter untuk kembali ke menu pengguna...")
        return

    index_watchlist = daftar_nomor_watchlist(user_aktif)
    print("----------------------------------------------")
    no_hapus = input("Pilih nomor watchlist : ")
    no_hapus_angka = ke_angka(no_hapus)

    if no_hapus_angka == None:
        print("\n[!] Nomor harus berupa angka.")
    elif no_hapus_angka < 1 or no_hapus_angka > len(index_watchlist):
        print("\n[!] Nomor " + no_hapus + " tidak ada di watchlist Anda.")
    else:
        yakin = input("Yakin ingin menghapus dari watchlist? [y/n] : ")
        if yakin == "y" or yakin == "Y":
            data_watch.pop(index_watchlist[no_hapus_angka - 1])
            print("\n[+] Anime berhasil dihapus dari watchlist.")
        else:
            print("\n[*] Penghapusan dibatalkan.")

    jeda("\nTekan Enter untuk kembali ke menu pengguna...")


# ---------------------------------------------------------------------
# LOGIN (ADMIN & PENGGUNA)
# ---------------------------------------------------------------------
def login_admin():
    """Login admin maksimal 3 percobaan. Mengembalikan True bila berhasil."""
    percobaan = 0
    berhasil = False
    while percobaan < 3 and berhasil == False:

        bersihkan_layar()
        print("==============================================")
        print("               LOGIN ADMIN")
        print("==============================================")
        input_username, input_password = input_kredensial()

        if input_username == "" or input_password == "":
            print("\n[!] Username dan password tidak boleh kosong.")
            percobaan = percobaan + 1
        elif input_username == admin_username and input_password == admin_password:
            print("\n[+] Login admin berhasil!")
            berhasil = True
        else:
            print("\n[!] Username atau password salah.")
            percobaan = percobaan + 1
            if percobaan < 3:
                print("    Sisa percobaan : " + str(3 - percobaan))

        if berhasil == False and percobaan < 3:
            jeda("\nTekan Enter untuk mencoba lagi...")

    if berhasil == False:
        print("\n[!] Percobaan login habis, kembali ke menu login.")
        jeda("Tekan Enter untuk melanjutkan...")

    return berhasil


def login_pengguna():
    bersihkan_layar()
    print("==============================================")
    print("              LOGIN PENGGUNA")
    print("==============================================")
    input_username, input_password = input_kredensial()

    if input_username == "" or input_password == "":
        print("\n[!] Username dan password tidak boleh kosong.")
        jeda("Tekan Enter untuk melanjutkan...")
        return None

    if validasi_login(input_username, input_password, akun) == False:
        print("\n[!] Akun tidak ditemukan atau password salah.")
        print("    Silakan register terlebih dahulu bila belum punya akun.")
        jeda("Tekan Enter untuk melanjutkan...")
        return None

    print("\n[+] Login berhasil, selamat datang " + input_username + "!")
    jeda("Tekan Enter untuk melanjutkan...")
    return input_username


def menu_login():
    login_jalan = True
    berhasil_login = False
    role = ""
    user_aktif = ""

    while login_jalan:

        bersihkan_layar()
        print("==============================================")
        print("                   LOGIN")
        print("==============================================")
        print(" 1. Login sebagai Admin")
        print(" 2. Login sebagai Pengguna")
        print(" 0. Kembali ke menu utama")
        print("==============================================")
        pilihan_login = input("Pilih [0/1/2] : ")

        if pilihan_login == "1":
            if login_admin() == True:
                berhasil_login = True
                role = "admin"
                user_aktif = admin_username
                login_jalan = False

        elif pilihan_login == "2":
            hasil_login = login_pengguna()
            if hasil_login != None:
                berhasil_login = True
                role = "user"
                user_aktif = hasil_login
                login_jalan = False

        elif pilihan_login == "0":
            login_jalan = False

        else:
            print("\n[!] Pilihan tidak tersedia, silakan pilih 0, 1, atau 2.")
            jeda("Tekan Enter untuk melanjutkan...")

    return berhasil_login, role, user_aktif


# ---------------------------------------------------------------------
# SESI ADMIN & SESI PENGGUNA
# ---------------------------------------------------------------------
def sesi_admin(user_aktif):
    sesi_jalan = True
    while sesi_jalan:

        bersihkan_layar()
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

        if menu_admin == "1":
            tambah_anime()

        elif menu_admin == "2":
            tampil_daftar_anime()
            jeda("\nTekan Enter untuk kembali ke menu admin...")

        elif menu_admin == "3":
            edit_anime()

        elif menu_admin == "4":
            hapus_anime()

        elif menu_admin == "5":
            print("\n[*] Logout berhasil, kembali ke menu utama.")
            sesi_jalan = False
            jeda("Tekan Enter untuk melanjutkan...")

        else:
            print("\n[!] Pilihan tidak tersedia, silakan pilih 1 sampai 5.")
            jeda("Tekan Enter untuk melanjutkan...")


def sesi_user(user_aktif):
    sesi_jalan = True
    while sesi_jalan:

        bersihkan_layar()
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

        if menu_user == "1":
            tampil_daftar_anime()
            jeda("\nTekan Enter untuk kembali ke menu pengguna...")

        elif menu_user == "2":
            tambah_watchlist(user_aktif)

        elif menu_user == "3":
            tampil_watchlist(user_aktif)
            jeda("\nTekan Enter untuk kembali ke menu pengguna...")

        elif menu_user == "4":
            edit_watchlist(user_aktif)

        elif menu_user == "5":
            hapus_watchlist(user_aktif)

        elif menu_user == "6":
            print("\n[*] Logout berhasil, kembali ke menu utama.")
            sesi_jalan = False
            jeda("Tekan Enter untuk melanjutkan...")

        else:
            print("\n[!] Pilihan tidak tersedia, silakan pilih 1 sampai 6.")
            jeda("Tekan Enter untuk melanjutkan...")


# ---------------------------------------------------------------------
# REGISTER
# ---------------------------------------------------------------------
def register():
    register_jalan = True
    while register_jalan:

        bersihkan_layar()
        print("==============================================")
        print("                 REGISTER")
        print("==============================================")
        username_baru = input("Username baru : ")

        if username_baru == "":
            print("\n[!] Username tidak boleh kosong.")
        elif username_baru == admin_username:
            print("\n[!] Username tersebut tidak boleh digunakan.")
        elif username_baru in akun:
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

    jeda("\nTekan Enter untuk kembali ke menu utama...")


# ---------------------------------------------------------------------
# MENU UTAMA
# ---------------------------------------------------------------------
def main():
    program_jalan = True
    while program_jalan:

        bersihkan_layar()
        print("==============================================")
        print("          SISTEM STREAMING ANIME")
        print("==============================================")
        print(" 1. Login")
        print(" 2. Register (Pengguna Baru)")
        print(" 3. Keluar")
        print("==============================================")
        menu_utama = input("Pilih menu [1/2/3] : ")

        if menu_utama == "1":
            berhasil_login, role, user_aktif = menu_login()
            if berhasil_login == True and role == "admin":
                sesi_admin(user_aktif)
            elif berhasil_login == True and role == "user":
                sesi_user(user_aktif)

        elif menu_utama == "2":
            register()

        elif menu_utama == "3":
            bersihkan_layar()
            print("==============================================")
            print("   Terima kasih telah menggunakan program")
            print("        SISTEM STREAMING ANIME")
            print("==============================================")
            program_jalan = False

        else:
            print("\n[!] Pilihan '" + menu_utama + "' tidak tersedia.")
            print("    Silakan pilih menu 1, 2, atau 3.")
            jeda("Tekan Enter untuk melanjutkan...")


# ---------------------------------------------------------------------
# PROGRAM UTAMA (dengan error handling)
# ---------------------------------------------------------------------
try:
    main()
except (KeyboardInterrupt, EOFError):
    print("\n\n[!] Program dihentikan oleh pengguna.")
finally:
    pass