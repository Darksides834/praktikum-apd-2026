# =====================================================================
# Library tambahan: prettytable (tabel), colorama (warna) & pwinput (password bertanda *)
# =====================================================================
import os

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    class _Kosong:
        def __getattr__(self, nama):
            return ""
    Fore = _Kosong()
    Style = _Kosong()

try:
    import pwinput
except ImportError:
    pwinput = None

clear = "cls" if os.name == "nt" else "clear"


def bersihkan_layar():
    os.system(clear)


def jeda(pesan):
    input(pesan)


def ke_angka(teks):
    try:
        if teks.isdigit() == False:
            raise ValueError
        return int(teks)
    except ValueError:
        return None


def id_berikutnya(daftar_id, indeks):
    if indeks == len(daftar_id):
        return 1
    terbesar_lain = id_berikutnya(daftar_id, indeks + 1)
    kandidat = daftar_id[indeks] + 1
    if kandidat > terbesar_lain:
        return kandidat
    return terbesar_lain


def input_password(prompt="Password : "):
    if pwinput != None:
        return pwinput.pwinput(prompt=prompt, mask="*")
    return input(prompt)


def pesan_sukses(teks):
    print(Fore.GREEN + Style.BRIGHT + "\n[+] " + teks)


def pesan_error(teks):
    print(Fore.RED + Style.BRIGHT + "\n[!] " + teks)


def pesan_info(teks):
    print(Fore.YELLOW + "\n[*] " + teks)


def judul_halaman(teks, user=None):
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    print(Fore.CYAN + Style.BRIGHT + teks.center(50))
    if user != None:
        print(Fore.CYAN + ("User : " + user).center(50))
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)