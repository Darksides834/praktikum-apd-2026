from Data import akun, watchlist, admin_username, admin_password
from Utils import (bersihkan_layar, jeda, input_password, pesan_sukses, pesan_error, pesan_info, judul_halaman)
from Tampilan import tampil_menu


def validasi_login(username, password, data_akun):
    try:
        if username in data_akun and data_akun[username] == password:
            return True
        return False
    except TypeError:
        return False


def input_kredensial():
    username_input = input("Username : ")
    password_input = input_password("Password : ")
    return username_input, password_input


def login_admin():
    percobaan = 0
    berhasil = False
    while percobaan < 3 and berhasil == False:
        bersihkan_layar()
        judul_halaman("LOGIN ADMIN")
        input_username, input_pass = input_kredensial()

        if input_username == "" or input_pass == "":
            pesan_error("Username dan password tidak boleh kosong.")
            percobaan = percobaan + 1
        elif input_username == admin_username and input_pass == admin_password:
            pesan_sukses("Login admin berhasil!")
            berhasil = True
        else:
            pesan_error("Username atau password salah.")
            percobaan = percobaan + 1
            if percobaan < 3:
                print("    Sisa percobaan : " + str(3 - percobaan))

        if berhasil == False and percobaan < 3:
            jeda("\nTekan Enter untuk mencoba lagi...")

    if berhasil == False:
        pesan_error("Percobaan login habis, kembali ke menu login.")
    jeda("Tekan Enter untuk melanjutkan...")
    return berhasil


def login_pengguna():
    bersihkan_layar()
    judul_halaman("LOGIN PENGGUNA")
    input_username, input_pass = input_kredensial()

    if input_username == "" or input_pass == "":
        pesan_error("Username dan password tidak boleh kosong.")
        jeda("Tekan Enter untuk melanjutkan...")
        return None

    if validasi_login(input_username, input_pass, akun) == False:
        pesan_error("Akun tidak ditemukan atau password salah.")
        print("    Silakan register terlebih dahulu bila belum punya akun.")
        jeda("Tekan Enter untuk melanjutkan...")
        return None

    pesan_sukses("Login berhasil, selamat datang " + input_username + "!")
    jeda("Tekan Enter untuk melanjutkan...")
    return input_username


def menu_login():
    login_jalan = True
    berhasil_login = False
    role = ""
    user_aktif = ""

    while login_jalan:
        tampil_menu("LOGIN", {"1": "Login sebagai Admin",
                              "2": "Login sebagai Pengguna",
                              "0": "Kembali ke menu utama"})
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
            pesan_error("Pilihan tidak tersedia, silakan pilih 0, 1, atau 2.")
            jeda("Tekan Enter untuk melanjutkan...")

    return berhasil_login, role, user_aktif


def register():
    register_jalan = True
    while register_jalan:
        bersihkan_layar()
        judul_halaman("REGISTER")
        username_baru = input("Username baru : ")

        if username_baru == "":
            pesan_error("Username tidak boleh kosong.")
        elif username_baru == admin_username:
            pesan_error("Username tersebut tidak boleh digunakan.")
        elif username_baru in akun:
            pesan_error("Username sudah terdaftar, silakan gunakan username lain.")
        else:
            password_baru = input_password("Password       : ")
            if password_baru == "":
                pesan_error("Password tidak boleh kosong.")
            elif len(password_baru) < 4:
                pesan_error("Password minimal 4 karakter.")
            else:
                password_konfirmasi = input_password("Ulangi password: ")
                if password_konfirmasi != password_baru:
                    pesan_error("Konfirmasi password tidak sama.")
                else:
                    akun[username_baru] = password_baru
                    watchlist[username_baru] = {}
                    pesan_sukses("Register berhasil! Akun '" + username_baru + "' sudah bisa digunakan.")
                    register_jalan = False

        if register_jalan == True:
            ulang = input("\nCoba register lagi? [y/n] : ")
            if ulang == "n" or ulang == "N":
                register_jalan = False

    jeda("\nTekan Enter untuk kembali ke menu utama...")