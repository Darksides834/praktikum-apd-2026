from prettytable import PrettyTable
from Data import anime, watchlist
from Utils import bersihkan_layar, judul_halaman, Fore, Style


def buat_tabel(kolom, rata_kiri):
    tabel = PrettyTable()
    tabel.field_names = kolom
    for nama in rata_kiri:
        tabel.align[nama] = "l"
    return tabel


def ambil_watchlist(nama_user):
    try:
        return watchlist[nama_user]
    except KeyError:
        watchlist[nama_user] = {}
        return watchlist[nama_user]


def cetak_tabel_pilih_anime():
    tabel = buat_tabel(["ID", "Judul", "Genre"], ["Judul", "Genre"])
    for id_anime in anime:
        tabel.add_row([id_anime, anime[id_anime]["judul"], anime[id_anime]["genre"]])
    print(tabel)


def tampil_daftar_anime():
    bersihkan_layar()
    judul_halaman("DAFTAR ANIME")

    if len(anime) == 0:
        print(" Belum ada data anime.")
        return

    tabel = buat_tabel(["ID", "Judul", "Genre", "Episode", "Status", "Tahun"],
                       ["Judul", "Genre", "Status"])
    for id_anime in anime:
        d = anime[id_anime]
        tabel.add_row([id_anime, d["judul"], d["genre"], d["episode"], d["status"], d["tahun"]])
    print(tabel)
    print(Fore.CYAN + " Total anime : " + str(len(anime)))


def cetak_tabel_watchlist(nama_user):
    data_watch = ambil_watchlist(nama_user)
    tabel = buat_tabel(["No", "Judul", "Genre", "Status"], ["Judul", "Genre", "Status"])
    index_watchlist = []
    nomor = 0
    for id_anime in data_watch:
        nomor = nomor + 1
        index_watchlist.append(id_anime)
        judul_tampil = "-"
        genre_tampil = "-"
        if id_anime in anime:
            judul_tampil = anime[id_anime]["judul"]
            genre_tampil = anime[id_anime]["genre"]
        tabel.add_row([nomor, judul_tampil, genre_tampil, data_watch[id_anime]])
    print(tabel)
    return index_watchlist


def tampil_watchlist(user_aktif):
    bersihkan_layar()
    judul_halaman("WATCHLIST SAYA", user_aktif)

    data_watch = ambil_watchlist(user_aktif)
    if len(data_watch) == 0:
        print(" Watchlist Anda masih kosong.")
    else:
        cetak_tabel_watchlist(user_aktif)
        print(Fore.CYAN + " Total watchlist : " + str(len(data_watch)))


def tampil_menu(judul, daftar_menu, user=None):
    bersihkan_layar()
    judul_halaman(judul, user)
    tabel = buat_tabel(["No", "Menu"], ["Menu"])
    for kunci in daftar_menu:
        tabel.add_row([kunci, daftar_menu[kunci]])
    print(tabel)


def tampil_pilihan(judul, pilihan):
    print(Fore.YELLOW + judul)
    tabel = buat_tabel(["No", "Status"], ["Status"])
    for kunci in pilihan:
        tabel.add_row([kunci, pilihan[kunci]])
    print(tabel)