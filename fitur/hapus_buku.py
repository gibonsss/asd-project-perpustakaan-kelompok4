"""Fitur 3: Cari buku berdasarkan kode (exact) atau judul (partial)."""
from data.koleksi import koleksi_buku, cari_by_kode
from utils.validasi import input_tidak_kosong
from utils.tampilan import cetak_tabel


def _cari_berdasarkan_kode():
    kode = input_tidak_kosong("Masukkan kode buku")
    buku = cari_by_kode(kode)
    if buku is None:
        print(f"Buku dengan kode '{kode}' tidak ditemukan dalam koleksi.")
        return
    print("Buku ditemukan:")
    cetak_tabel([buku])


def _cari_berdasarkan_judul():
    kata = input_tidak_kosong("Masukkan kata kunci judul")
    hasil = [b for b in koleksi_buku if kata.lower() in b["judul"].lower()]
    if not hasil:
        print(f"Tidak ada buku dengan judul yang mengandung '{kata}'.")
        return
    print(f"Ditemukan {len(hasil)} buku dengan judul mengandung '{kata}':")
    cetak_tabel(hasil)


def cari_buku():
    """Menu pencarian: pilih mode (kode/judul), input kata kunci, tampilkan hasil."""
    print("=== CARI BUKU ===")
    print("1. Cari berdasarkan kode")
    print("2. Cari berdasarkan judul")
    pilihan = input("Pilih mode pencarian: ").strip()
    if pilihan == "1":
        _cari_berdasarkan_kode()
    elif pilihan == "2":
        _cari_berdasarkan_judul()
    else:
        print("Pilihan tidak valid. Masukkan 1 atau 2.")