"""Sistem Perpustakaan Mini (Tahap 1: Array & Struct).

Jalankan dengan: python main.py
"""
from fitur.tambah import tambah_buku
from fitur.tampil import tampil_semua_buku
from fitur.cari import cari_buku
from fitur.status import update_status
from fitur.filter_genre import filter_genre
from fitur.hapus_buku import hapus_buku
from fitur.riwayat import tampil_riwayat, tampil_riwayat_per_kode

MENU = {
    "1": ("Tambah buku baru", tambah_buku),
    "2": ("Tampilkan semua buku", tampil_semua_buku),
    "3": ("Cari buku", cari_buku),
    "4": ("Update status buku", update_status),
    "5": ("Filter buku berdasarkan genre", filter_genre),
    "6": ("Hapus buku", hapus_buku),
    "7": ("Tampilkan riwayat", tampil_riwayat),
    "8": ("Riwayat per kode buku", tampil_riwayat_per_kode)
}


def tampilkan_menu():
    print("\n=== SISTEM PERPUSTAKAAN MINI ===")
    for nomor, (nama, _) in MENU.items():
        print(f"{nomor}. {nama}")
    print("0. Keluar")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "0":
            print("Terima kasih. Program selesai.")
            break
        if pilihan in MENU:
            print()
            MENU[pilihan][1]()
        else:
            print("Pilihan tidak valid. Masukkan angka 0 sampai 8.")
        input("\nTekan Enter untuk kembali ke menu...")


if __name__ == "__main__":
    main()
