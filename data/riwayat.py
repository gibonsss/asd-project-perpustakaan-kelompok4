from datetime import datetime

class Node:
    """Satu kotak data: berisi data dan penunjuk ke node berikutnya."""

    def __init__(self, data):
        self.data = data
        self.next = None


class RiwayatLinkedList:
    """Singly linked list untuk menyimpan catatan riwayat."""

    def __init__(self):
        self.head = None

    def is_empty(self):
        """True jika belum ada catatan sama sekali."""
        return self.head is None

    def insert_akhir(self, data):
        """Menambahkan data sebagai node baru di akhir list. O(n)."""
        node_baru = Node(data)

        # List kosong: node baru langsung menjadi head
        if self.is_empty():
            self.head = node_baru
            return

        # Jalan ke node terakhir (pakai current, jangan menggeser head)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node_baru

    def panjang(self):
        """Mengembalikan jumlah catatan di dalam list. O(n)."""
        jumlah = 0
        current = self.head
        while current is not None:
            jumlah += 1
            current = current.next
        return jumlah


# Satu daftar riwayat yang dipakai bersama oleh seluruh program
daftar_riwayat = RiwayatLinkedList()


def catat_riwayat(aksi, kode_buku, judul, nilai_lama, nilai_baru):
    """Menyimpan satu catatan riwayat ke akhir daftar_riwayat.

    aksi        : jenis perubahan: "TAMBAH", "PINJAM", "KEMBALI", atau "HAPUS"
    kode_buku   : kode buku yang berubah
    judul       : judul buku yang berubah
    nilai_lama  : nilai sebelum berubah (None jika tidak ada)
    nilai_baru  : nilai sesudah berubah (None jika tidak ada)
    """
    catatan = {
        "no_urut": daftar_riwayat.panjang() + 1,                         # DIPERBAIKI
        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),           # DIPERBAIKI
        "aksi": aksi,
        "kode_buku": kode_buku,
        "judul": judul,
        "nilai_lama": nilai_lama,
        "nilai_baru": nilai_baru,
    }
    daftar_riwayat.insert_akhir(catatan)


if __name__ == "__main__":
    # Contoh pemakaian dan pengujian. Bagian ini HANYA berjalan jika file
    # dijalankan langsung (python data/riwayat.py), tidak saat di-import,
    # sehingga daftar_riwayat tidak terisi catatan contoh di program utama.
    print("Kosong di awal :", daftar_riwayat.is_empty())

    catat_riwayat("TAMBAH", "BK007", "Python Crash Course", None, "Tersedia")
    catat_riwayat("PINJAM", "BK001", "Algoritma dan Pemrograman", "Tersedia", "Dipinjam")
    catat_riwayat("KEMBALI", "BK001", "Algoritma dan Pemrograman", "Dipinjam", "Tersedia")
    catat_riwayat("HAPUS", "BK003", "Laskar Pelangi", "Dipinjam", None)

    print("Jumlah catatan :", daftar_riwayat.panjang())
    print("Isi riwayat (urut sesuai pemanggilan):")
    current = daftar_riwayat.head
    nomor = 1
    while current is not None:
        c = current.data
        print(f"  {nomor}. {c['aksi']} | {c['kode_buku']} | {c['judul']} | "
              f"{c['nilai_lama']} -> {c['nilai_baru']}")
        current = current.next
        nomor += 1