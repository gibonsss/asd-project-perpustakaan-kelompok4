from data.koleksi import cari_by_kode
from utils.validasi import input_tidak_kosong, konfirmasi
from utils.tampilan import cetak_tabel


def update_status():
    """Mengubah status buku secara otomatis (toggle) setelah konfirmasi."""
    print("=== UPDATE STATUS BUKU ===")
    kode = input_tidak_kosong("Masukkan kode buku")
    buku = cari_by_kode(kode)
    if buku is None:
        print(f"Error: buku dengan kode '{kode}' tidak ditemukan dalam koleksi.")
        return

    print("Data buku:")
    cetak_tabel([buku])

    lama = buku["status"]
    baru = "Dipinjam" if lama == "Tersedia" else "Tersedia"
    aksi = "dipinjam" if baru == "Dipinjam" else "dikembalikan"

    if konfirmasi(f"Ubah status dari {lama} menjadi {baru}?"):
        buku["status"] = baru
        print(f"Buku '{buku['judul']}' berhasil {aksi}. "
              f"Status diubah: {lama} menjadi {baru}.")
    else:
        print("Perubahan status dibatalkan.")
