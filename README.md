# asd-project-perpustakaan-kelompok4
UTS ALGORITMA DAN STRUKTUR DATA

# Sistem Perpustakaan Mini

**Kelompok 4** | Algoritma dan Struktur Data | Sistem Informasi, FTI Unmer Malang

## Anggota Kelompok

| Nama | NIM | Username GitHub |
|---|---|---|
| Fathir Wafi Ivansyah | 25083000004 | DeJ4v9 |
| Giftfen Yurian Adventius | 25083000008 | gifen45-spec |
| Azizah Nailah Ramadhani | 25083000013 | nailahazizah07 |
| Ahmad Yusuf Mahendra | 25083000049 | YuuQwarl |
| Ghibran Maulana Surya | 25083000050 | gibonsss |

## Deskripsi Sistem

Sistem Perpustakaan Mini adalah program berbasis terminal (CLI) untuk membantu petugas mengelola koleksi buku: menambah, menampilkan, mencari, memfilter berdasarkan genre, mengubah status peminjaman, dan menghapus buku. Setiap buku disimpan sebagai dictionary dalam list of dictionary di memori (Array of Struct). Data tidak disimpan ke file, sehingga kembali ke data contoh setiap program dijalankan ulang

## Cara Menjalankan

Syarat: Python 3.8 atau lebih baru. Tidak memerlukan library tambahan.

```bash
git clone https://github.com/(gibonsss)/asd-project-perpustakaan-kelompok4.git
cd asd-project-perpustakaan-kelompok4
python main.py
```

Program menampilkan menu utama. Ketik angka menu (0 sampai 6), lalu tekan Enter.
Setelah sebuah fitur selesai, tekan Enter lagi untuk kembali ke menu.

## Fitur yang Sudah Ada (Tahap 1)

- [x] **F1 Tambah Buku Baru**: validasi kode duplikat, field kosong, dan tahun terbit; status awal otomatis Tersedia
- [x] **F2 Tampilkan Semua Buku**: tabel koleksi dengan ringkasan total, Tersedia, dan Dipinjam
- [x] **F3 Cari Buku**: berdasarkan kode (exact match) atau judul (partial match, tidak case sensitive)
- [x] **F4 Update Status Buku**: status berganti otomatis antara Tersedia dan Dipinjam setelah konfirmasi (y/n)
- [x] **F5 Filter Buku Berdasarkan Genre**: partial match, tidak case sensitive
- [x] **F6 Hapus Buku**: buku berstatus Dipinjam tidak dapat dihapus; penghapusan memerlukan konfirmasi (y/n)

## Data Contoh

Program dimulai dengan 6 buku contoh (BK001 sampai BK006), tiga di antaranya
berstatus Dipinjam, sehingga seluruh fitur dapat langsung dicoba.

koleksi_buku = [
    _buku("BK001", "Algoritma dan Pemrograman", "Rinaldi Munir",     "Teknologi",    2020, STATUS_TERSEDIA),
    _buku("BK002", "Laskar Pelangi",            "Andrea Hirata",     "Fiksi",        2005, STATUS_DIPINJAM),
    _buku("BK003", "Pengantar Algoritma",       "Thomas H. Cormen",  "Teknologi",    2009, STATUS_DIPINJAM),
    _buku("BK004", "Dune",                      "Frank Herbert",     "Fiksi Ilmiah", 1965, STATUS_TERSEDIA),
    _buku("BK005", "Cosmos",                    "Carl Sagan",        "Sains",        1980, STATUS_TERSEDIA),
    _buku("BK006", "Sapiens",                   "Yuval Noah Harari", "Sejarah",      2011, STATUS_DIPINJAM),
]

## Struktur Folder

```
main.py              # menu utama
data/
  koleksi.py         # data koleksi buku dan fungsi cari_by_kode()
utils/
  validasi.py        # validasi input (tidak kosong, tahun, konfirmasi y/n)
  tampilan_tabel.py  # format tabel buku yang dipakai bersama
fitur/
  tambah.py          # F1
  tampil.py          # F2
  cari.py            # F3
  status.py          # F4
  filter_genre.py    # F5
  hapus_buku.py      # F6
```

## Pembagian Tugas

| Anggota | Tugas |
|---|---|
| (Fathir Wafi Ivansyah) | File fitur Hapus Buku dan Cari |
| (Giftfen Yurina Adventius) | File fitur filter_genre dan ulits/tampilan_tabel |
| (Azizah Nailah Ramadhani) | File fitur tambah buku baru dan update status buku |
| (iAhmad Yusuh Mahendra) | File koleksi.py dan fitur tampilkan semua buku |
| (Ghibran Maulana Surya) | File `main.py`, `validasi.py`, review dan merge Pull Request,README |

## Alur Kerja Git

Branch `main` berisi versi stabil. Pengembangan dan penginputan dilakukan di branch `develop`, dan setiap fitur dikerjakan di branch fitur masing-masing, lalu digabung lewat
Pull Request yang di-review ketua.