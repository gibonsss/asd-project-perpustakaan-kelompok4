"""Fitur untuk menampilkan riwayat transaksi perpustakaan."""
from data.riwayat import daftar_riwayat
from utils.tampilan_tabel import cetak_tabel_riwayat


def tampil_riwayat():
    """Menampilkan seluruh catatan riwayat dari yang paling lama ke paling baru."""
    print("=== DAFTAR RIWAYAT ===")
    if daftar_riwayat.is_empty():
        print("Belum ada riwayat.")
        return

    cetak_tabel_riwayat(daftar_riwayat)