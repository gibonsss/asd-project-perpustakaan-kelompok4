"""Fitur 6 Hapus buku dari koleksi."""
from data.koleksi import koleksi_buku, cari_by_kode
from utils.validasi import input_tidak_kosong, konfirmasi
from utils.tampilan_tabel import cetak_tabel


def hapus_buku():
    """Menghapus buku setelah konfirmasi. Buku berstatus Dipinjam tidak boleh dihapus."""
    print("=== HAPUS BUKU ===")
    kode = input_tidak_kosong("Masukkan kode buku")
    buku = cari_by_kode(kode)
    if buku is None:
        print(f"Buku dengan kode '{kode}' tidak ditemukan dalam koleksi.")
        return

    print("Data buku:")
    cetak_tabel([buku])

    if buku["status"] == "Dipinjam":
        print(f"Error: buku '{buku['judul']}' sedang dipinjam dan tidak dapat dihapus. "
              "Kembalikan buku terlebih dahulu.")
        return

    if konfirmasi("Yakin ingin menghapus buku ini?"):
        koleksi_buku.remove(buku)
        print(f"Buku '{buku['judul']}' dengan kode {buku['kode_buku']} "
              "berhasil dihapus dari koleksi.")
    else:
        print("Penghapusan dibatalkan.")