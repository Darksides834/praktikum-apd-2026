from Utils import jeda, pesan_error, pesan_info
from Tampilan import tampil_menu, tampil_daftar_anime, tampil_watchlist
from Admin import tambah_anime, edit_anime, hapus_anime
from User import tambah_watchlist, edit_watchlist, hapus_watchlist


def sesi_admin(user_aktif):
    sesi_jalan = True
    while sesi_jalan:
        tampil_menu("MENU ADMIN", {
            "1": "Tambah Anime",
            "2": "Tampilkan Daftar Anime",
            "3": "Edit Informasi Anime",
            "4": "Hapus Anime",
            "5": "Logout"}, user_aktif + " (Admin)")
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
            pesan_info("Logout berhasil, kembali ke menu utama.")
            sesi_jalan = False
            jeda("Tekan Enter untuk melanjutkan...")
        else:
            pesan_error("Pilihan tidak tersedia, silakan pilih 1 sampai 5.")
            jeda("Tekan Enter untuk melanjutkan...")


def sesi_user(user_aktif):
    sesi_jalan = True
    while sesi_jalan:
        tampil_menu("MENU PENGGUNA", {
            "1": "Tampilkan Daftar Anime",
            "2": "Tambah Anime ke Watchlist",
            "3": "Tampilkan Watchlist Saya",
            "4": "Edit Status Watchlist",
            "5": "Hapus Anime dari Watchlist",
            "6": "Logout"}, user_aktif)
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
            pesan_info("Logout berhasil, kembali ke menu utama.")
            sesi_jalan = False
            jeda("Tekan Enter untuk melanjutkan...")
        else:
            pesan_error("Pilihan tidak tersedia, silakan pilih 1 sampai 6.")
            jeda("Tekan Enter untuk melanjutkan...")