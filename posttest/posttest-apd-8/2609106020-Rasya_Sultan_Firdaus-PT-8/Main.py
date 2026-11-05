# =====================================================================
# PROGRAM  : SISTEM STREAMING ANIME (POSTTEST 8)
# =====================================================================
from Utils import bersihkan_layar, jeda, pesan_error, judul_halaman
from Tampilan import tampil_menu
from Auth import menu_login, register
from Menu import sesi_admin, sesi_user


def main():
    program_jalan = True
    while program_jalan:
        tampil_menu("SISTEM STREAMING ANIME", {
            "1": "Login",
            "2": "Register (Pengguna Baru)",
            "3": "Keluar"})
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
            judul_halaman("Terima kasih telah menggunakan program")
            program_jalan = False

        else:
            pesan_error("Pilihan '" + menu_utama + "' tidak tersedia.")
            print("    Silakan pilih menu 1, 2, atau 3.")
            jeda("Tekan Enter untuk melanjutkan...")


try:
    main()
except (KeyboardInterrupt, EOFError):
    print("\n\n[!] Program dihentikan oleh pengguna.")
finally:
    pass