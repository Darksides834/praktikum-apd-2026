from Data import anime, pilihan_status_watchlist
from Utils import (bersihkan_layar, jeda, ke_angka,pesan_sukses, pesan_error, pesan_info, judul_halaman)
from Tampilan import (cetak_tabel_pilih_anime, cetak_tabel_watchlist, ambil_watchlist, tampil_pilihan)

KEMBALI = "\nTekan Enter untuk kembali ke menu pengguna..."


def tambah_watchlist(user_aktif):
    bersihkan_layar()
    judul_halaman("TAMBAH KE WATCHLIST")

    if len(anime) == 0:
        pesan_info("Belum ada data anime.")
        jeda(KEMBALI)
        return

    cetak_tabel_pilih_anime()
    id_tambah = input("Masukkan ID anime : ")
    id_tambah_angka = ke_angka(id_tambah)

    if id_tambah_angka == None:
        pesan_error("ID harus berupa angka.")
        jeda(KEMBALI)
        return
    if id_tambah_angka not in anime:
        pesan_error("Anime dengan ID " + id_tambah + " tidak ditemukan.")
        jeda(KEMBALI)
        return

    data_watch = ambil_watchlist(user_aktif)
    if id_tambah_angka in data_watch:
        pesan_error("Anime sudah ada di watchlist Anda.")
        jeda(KEMBALI)
        return

    tampil_pilihan("Pilihan status tontonan :", pilihan_status_watchlist)
    status_tonton = input("Status awal [1/2/3] : ")

    if status_tonton not in pilihan_status_watchlist:
        pesan_error("Pilihan status tidak tersedia, data batal disimpan.")
    else:
        data_watch[id_tambah_angka] = pilihan_status_watchlist[status_tonton]
        pesan_sukses("'" + str(anime[id_tambah_angka]["judul"]) + "' berhasil ditambahkan ke watchlist.")

    jeda(KEMBALI)


def edit_watchlist(user_aktif):
    bersihkan_layar()
    judul_halaman("EDIT STATUS WATCHLIST")

    data_watch = ambil_watchlist(user_aktif)
    if len(data_watch) == 0:
        pesan_info("Watchlist Anda masih kosong.")
        jeda(KEMBALI)
        return

    index_watchlist = cetak_tabel_watchlist(user_aktif)
    no_edit = input("Pilih nomor watchlist : ")
    no_edit_angka = ke_angka(no_edit)

    if no_edit_angka == None:
        pesan_error("Nomor harus berupa angka.")
    elif no_edit_angka < 1 or no_edit_angka > len(index_watchlist):
        pesan_error("Nomor " + no_edit + " tidak ada di watchlist Anda.")
    else:
        tampil_pilihan("Pilihan status tontonan :", pilihan_status_watchlist)
        status_tonton = input("Status baru [1/2/3] : ")
        if status_tonton not in pilihan_status_watchlist:
            pesan_error("Pilihan status tidak tersedia.")
        else:
            data_watch[index_watchlist[no_edit_angka - 1]] = pilihan_status_watchlist[status_tonton]
            pesan_sukses("Status watchlist berhasil diubah.")

    jeda(KEMBALI)


def hapus_watchlist(user_aktif):
    bersihkan_layar()
    judul_halaman("HAPUS ANIME DARI WATCHLIST")

    data_watch = ambil_watchlist(user_aktif)
    if len(data_watch) == 0:
        pesan_info("Watchlist Anda masih kosong.")
        jeda(KEMBALI)
        return

    index_watchlist = cetak_tabel_watchlist(user_aktif)
    no_hapus = input("Pilih nomor watchlist : ")
    no_hapus_angka = ke_angka(no_hapus)

    if no_hapus_angka == None:
        pesan_error("Nomor harus berupa angka.")
    elif no_hapus_angka < 1 or no_hapus_angka > len(index_watchlist):
        pesan_error("Nomor " + no_hapus + " tidak ada di watchlist Anda.")
    else:
        yakin = input("Yakin ingin menghapus dari watchlist? [y/n] : ")
        if yakin == "y" or yakin == "Y":
            data_watch.pop(index_watchlist[no_hapus_angka - 1])
            pesan_sukses("Anime berhasil dihapus dari watchlist.")
        else:
            pesan_info("Penghapusan dibatalkan.")

    jeda(KEMBALI)