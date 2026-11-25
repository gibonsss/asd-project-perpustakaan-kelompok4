
"""Fitur untuk menampilkan riwayat transaksi perpustakaan."""
from data.riwayat import daftar_riwayat, RiwayatLinkedList
from utils.tampilan_tabel import cetak_tabel_riwayat


def tampil_riwayat():
    """Menampilkan seluruh catatan riwayat."""
    print("=== DAFTAR RIWAYAT ===")

    if daftar_riwayat.is_empty():
        print("Belum ada riwayat.")
        return

    cetak_tabel_riwayat(daftar_riwayat)


def tampil_riwayat_per_kode():
    """Menampilkan riwayat transaksi berdasarkan kode buku."""
    print("=== RIWAYAT PER KODE BUKU ===")

    kode = input("Masukkan kode buku: ").strip()

    hasil = RiwayatLinkedList()
    current = daftar_riwayat.head

    while current is not None:
        data = current.data

        if data["kode_buku"].lower() == kode.lower():
            hasil.insert_akhir(data)

        current = current.next

    if hasil.is_empty():
        print(f"Riwayat dengan kode buku {kode} tidak ditemukan.")
        return

    cetak_tabel_riwayat(hasil)
