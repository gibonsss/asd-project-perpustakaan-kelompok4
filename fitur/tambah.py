from data.koleksi import koleksi_buku, cari_by_kode
from utils.validasi import input_tidak_kosong, input_tahun


def tambah_buku():
    """Meminta data buku, memvalidasi, lalu menambahkannya ke koleksi."""
    print("=== TAMBAH BUKU BARU ===")

    kode = input_tidak_kosong("Kode buku")
    if cari_by_kode(kode) is not None:
        print(f"Error: kode '{kode}' sudah digunakan. Gunakan kode yang berbeda.")
        return

    judul = input_tidak_kosong("Judul")
    pengarang = input_tidak_kosong("Pengarang")
    genre = input_tidak_kosong("Genre")
    tahun = input_tahun()

    koleksi_buku.append({
        "kode_buku": kode,
        "judul": judul,
        "pengarang": pengarang,
        "genre": genre,
        "tahun_terbit": tahun,
        "status": "Tersedia",
    })
    print(f"Buku '{judul}' dengan kode {kode} berhasil ditambahkan ke koleksi.")
