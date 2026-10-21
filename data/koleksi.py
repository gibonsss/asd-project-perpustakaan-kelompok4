
# ======================================================================
# KONSTANTA
# ======================================================================
 
STATUS_TERSEDIA = "Tersedia"
STATUS_DIPINJAM = "Dipinjam"
 
 
# ======================================================================
# DATA
# ======================================================================
 
def _buku(kode_buku, judul, pengarang, genre, tahun_terbit, status):
    """Membuat satu buku (dict). Status wajib diisi: STATUS_TERSEDIA atau STATUS_DIPINJAM."""
    return {
        "kode_buku": kode_buku,
        "judul": judul,
        "pengarang": pengarang,
        "genre": genre,
        "tahun_terbit": tahun_terbit,
        "status": status,
    }
 
 
# Format tiap baris: kode, judul, pengarang, genre, tahun, status
koleksi_buku = [
    _buku("BK001", "Algoritma dan Pemrograman", "Rinaldi Munir",     "Teknologi",    2020, STATUS_TERSEDIA),
    _buku("BK002", "Laskar Pelangi",            "Andrea Hirata",     "Fiksi",        2005, STATUS_DIPINJAM),
    _buku("BK003", "Pengantar Algoritma",       "Thomas H. Cormen",  "Teknologi",    2009, STATUS_DIPINJAM),
    _buku("BK004", "Dune",                      "Frank Herbert",     "Fiksi Ilmiah", 1965, STATUS_TERSEDIA),
    _buku("BK005", "Cosmos",                    "Carl Sagan",        "Sains",        1980, STATUS_TERSEDIA),
    _buku("BK006", "Sapiens",                   "Yuval Noah Harari", "Sejarah",      2011, STATUS_DIPINJAM),
]
 
 
# ======================================================================
# FUNGSI PENCARIAN
# ======================================================================
 
def cari_by_kode(kode):
    """Mengembalikan dict buku dengan kode persis sama (tidak case sensitive).
 
    Mengembalikan None jika tidak ditemukan.
    """
    kode = kode.strip().lower()
    for buku in koleksi_buku:
        if buku["kode_buku"].lower() == kode:
            return buku
    return None
 