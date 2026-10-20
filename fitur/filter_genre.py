"""Fitur 5: Filter buku berdasarkan genre (partial, tidak case sensitive)."""
from data.koleksi import koleksi_buku
from utils.validasi import input_tidak_kosong
from utils.tampilan import cetak_tabel


def filter_genre():
    """Meminta genre, lalu menampilkan buku yang genre-nya mengandung kata itu."""
    print("=== FILTER BERDASARKAN GENRE ===")
    genre = input_tidak_kosong("Masukkan genre")
    hasil = [b for b in koleksi_buku if genre.lower() in b["genre"].lower()]

    if not hasil:
        print(f"Tidak ada buku dengan genre '{genre}' dalam koleksi.")
        return

    print(f"Menampilkan buku genre: {genre} ({len(hasil)} buku ditemukan).")
    cetak_tabel(hasil)