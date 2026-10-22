from data.koleksi import koleksi_buku, STATUS_TERSEDIA, STATUS_DIPINJAM
from utils.tampilan_tabel import cetak_tabel
 
 
def _hitung_ringkasan(daftar_buku):
    """Mengembalikan tuple (total, jumlah_tersedia, jumlah_dipinjam)."""
    tersedia = sum(1 for buku in daftar_buku if buku["status"] == STATUS_TERSEDIA)
    dipinjam = sum(1 for buku in daftar_buku if buku["status"] == STATUS_DIPINJAM)
    return len(daftar_buku), tersedia, dipinjam
 
 
def _cetak_ringkasan(daftar_buku):
    """Mencetak ringkasan di bawah tabel."""
    total, tersedia, dipinjam = _hitung_ringkasan(daftar_buku)
    print(f"Total buku : {total}")
    print(f"Tersedia   : {tersedia}")
    print(f"Dipinjam   : {dipinjam}")
 
 
def tampil_semua_buku():
    """Menampilkan seluruh koleksi dalam bentuk tabel beserta ringkasannya."""
    print("=== DAFTAR SEMUA BUKU ===")
 
    if not koleksi_buku:
        print("Belum ada buku dalam koleksi.")
        return
 
    cetak_tabel(koleksi_buku)
    _cetak_ringkasan(koleksi_buku)
 