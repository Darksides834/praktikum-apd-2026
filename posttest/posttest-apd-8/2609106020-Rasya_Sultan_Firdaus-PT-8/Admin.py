from Data import anime, watchlist, pilihan_status_anime
from Utils import (bersihkan_layar, jeda, ke_angka, id_berikutnya, pesan_sukses, pesan_error, pesan_info, judul_halaman)
from Tampilan import cetak_tabel_pilih_anime, buat_tabel, tampil_pilihan

KEMBALI = "\nTekan Enter untuk kembali ke menu admin..."


def tambah_anime():
    bersihkan_layar()
    judul_halaman("TAMBAH ANIME")
    judul_baru = input("Judul anime      : ")

    if judul_baru == "":
        pesan_error("Judul tidak boleh kosong, data batal disimpan.")
        jeda(KEMBALI)
        return

    genre_baru = input("Genre            : ")
    if genre_baru == "":
        genre_baru = "-"

    episode_baru = ke_angka(input("Jumlah episode   : "))
    if episode_baru == None:
        pesan_error("Jumlah episode harus angka, data batal disimpan.")
        jeda(KEMBALI)
        return

    tampil_pilihan("Pilihan status anime :", pilihan_status_anime)
    status_baru = input("Status [1/2/3]   : ")
    if status_baru not in pilihan_status_anime:
        pesan_error("Pilihan status tidak tersedia, data batal disimpan.")
        jeda(KEMBALI)
        return

    tahun_baru = ke_angka(input("Tahun rilis      : "))
    if tahun_baru == None:
        pesan_error("Tahun rilis harus angka, data batal disimpan.")
        jeda(KEMBALI)
        return

    id_baru = id_berikutnya(list(anime.keys()), 0)
    anime[id_baru] = {
        "judul": judul_baru,
        "genre": genre_baru,
        "episode": episode_baru,
        "status": pilihan_status_anime[status_baru],
        "tahun": tahun_baru
    }
    pesan_sukses("Anime berhasil ditambahkan dengan ID " + str(id_baru) + ".")
    jeda(KEMBALI)


def _tampil_detail_edit(id_anime):
    bersihkan_layar()
    judul_halaman("EDIT INFORMASI ANIME")
    tabel = buat_tabel(["No", "Data", "Nilai"], ["Data", "Nilai"])
    tabel.add_row([1, "Judul", anime[id_anime]["judul"]])
    tabel.add_row([2, "Genre", anime[id_anime]["genre"]])
    tabel.add_row([3, "Episode", anime[id_anime]["episode"]])
    tabel.add_row([4, "Status", anime[id_anime]["status"]])
    tabel.add_row([5, "Tahun", anime[id_anime]["tahun"]])
    tabel.add_row([0, "Selesai / kembali", ""])
    print(tabel)


def edit_anime():
    bersihkan_layar()
    judul_halaman("EDIT INFORMASI ANIME")

    if len(anime) == 0:
        pesan_info("Belum ada data anime yang bisa diedit.")
        jeda(KEMBALI)
        return

    cetak_tabel_pilih_anime()
    id_edit = input("Masukkan ID anime yang akan diedit : ")
    id_edit_angka = ke_angka(id_edit)

    if id_edit_angka == None:
        pesan_error("ID harus berupa angka.")
        jeda(KEMBALI)
        return
    if id_edit_angka not in anime:
        pesan_error("Anime dengan ID " + id_edit + " tidak ditemukan.")
        jeda(KEMBALI)
        return

    edit_jalan = True
    while edit_jalan:
        _tampil_detail_edit(id_edit_angka)
        pilih_edit = input("Pilih data yang akan diubah [0-5] : ")

        if pilih_edit == "1":
            nilai_baru = input("Judul baru   : ")
            if nilai_baru == "":
                pesan_error("Judul tidak boleh kosong.")
            else:
                anime[id_edit_angka]["judul"] = nilai_baru
                pesan_sukses("Judul berhasil diubah.")
            jeda("Tekan Enter...")

        elif pilih_edit == "2":
            nilai_baru = input("Genre baru   : ")
            if nilai_baru == "":
                pesan_error("Genre tidak boleh kosong.")
            else:
                anime[id_edit_angka]["genre"] = nilai_baru
                pesan_sukses("Genre berhasil diubah.")
            jeda("Tekan Enter...")

        elif pilih_edit == "3":
            nilai_baru = ke_angka(input("Episode baru : "))
            if nilai_baru == None:
                pesan_error("Episode harus berupa angka.")
            else:
                anime[id_edit_angka]["episode"] = nilai_baru
                pesan_sukses("Jumlah episode berhasil diubah.")
            jeda("Tekan Enter...")

        elif pilih_edit == "4":
            tampil_pilihan("Pilihan status anime :", pilihan_status_anime)
            nilai_baru = input("Status baru [1/2/3] : ")
            if nilai_baru not in pilihan_status_anime:
                pesan_error("Pilihan status tidak tersedia.")
            else:
                anime[id_edit_angka]["status"] = pilihan_status_anime[nilai_baru]
                pesan_sukses("Status berhasil diubah.")
            jeda("Tekan Enter...")

        elif pilih_edit == "5":
            nilai_baru = ke_angka(input("Tahun baru   : "))
            if nilai_baru == None:
                pesan_error("Tahun harus berupa angka.")
            else:
                anime[id_edit_angka]["tahun"] = nilai_baru
                pesan_sukses("Tahun rilis berhasil diubah.")
            jeda("Tekan Enter...")

        elif pilih_edit == "0":
            edit_jalan = False

        else:
            pesan_error("Pilihan tidak tersedia.")
            jeda("Tekan Enter...")


def hapus_anime():
    bersihkan_layar()
    judul_halaman("HAPUS ANIME")

    if len(anime) == 0:
        pesan_info("Belum ada data anime yang bisa dihapus.")
        jeda(KEMBALI)
        return

    cetak_tabel_pilih_anime()
    id_hapus = input("Masukkan ID anime yang akan dihapus : ")
    id_hapus_angka = ke_angka(id_hapus)

    if id_hapus_angka == None:
        pesan_error("ID harus berupa angka.")
        jeda(KEMBALI)
        return
    if id_hapus_angka not in anime:
        pesan_error("Anime dengan ID " + id_hapus + " tidak ditemukan.")
        jeda(KEMBALI)
        return

    print(" Judul : " + str(anime[id_hapus_angka]["judul"]))
    print(" Genre : " + str(anime[id_hapus_angka]["genre"]))
    yakin = input("Yakin ingin menghapus data ini? [y/n] : ")

    if yakin == "y" or yakin == "Y":
        judul_terhapus = anime[id_hapus_angka]["judul"]
        anime.pop(id_hapus_angka)
        for nama_user in watchlist:
            if id_hapus_angka in watchlist[nama_user]:
                watchlist[nama_user].pop(id_hapus_angka)
        pesan_sukses("Anime '" + judul_terhapus + "' berhasil dihapus.")
    else:
        pesan_info("Penghapusan dibatalkan.")

    jeda(KEMBALI)