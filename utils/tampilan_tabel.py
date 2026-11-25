"""Fungsi tampilan yang dipakai bersama (F2, F3 judul, F5)."""


def _potong(teks, panjang):
    """Memotong teks yang melebihi lebar kolom agar tabel tetap rapi."""
    if teks is None:          
        return "-"
    teks = str(teks)
    if len(teks) > panjang:
        return teks[:panjang - 3] + "..."
    return teks


def cetak_tabel(daftar_buku):
    """Mencetak tabel dari list buku (list of dict)."""
    garis = "-" * 100
    print(garis)
    print(f"{'No':<4}{'Kode':<9}{'Judul':<28}{'Pengarang':<20}"
          f"{'Genre':<16}{'Tahun':<7}Status")
    print(garis)
    for no, b in enumerate(daftar_buku, start=1):
        status = f"[{b['status'].upper()}]"
        print(f"{no:<4}{_potong(b['kode_buku'], 8):<9}"
              f"{_potong(b['judul'], 27):<28}"
              f"{_potong(b['pengarang'], 19):<20}"
              f"{_potong(b['genre'], 15):<16}"
              f"{b['tahun_terbit']:<7}{status}")
    print(garis)

def cetak_tabel_riwayat(riwayat_linked_list):
    """Mencetak tabel riwayat dengan garis pemisah antar kolom."""
    judul_kolom = ["No", "Waktu", "Aksi", "Kode", "Judul Buku", "Lama", "Baru"]
    lebar = [4, 19, 8, 8, 22, 10, 10]   # lebar isi tiap kolom

    def baris(isi):
        """Menyusun satu baris: setiap sel dipotong, diratakan kiri, dipisah '|'."""
        sel = [f"{_potong(t, w):<{w}}" for t, w in zip(isi, lebar)]
        return "| " + " | ".join(sel) + " |"

    # Garis pemisah horizontal, contoh: +------+-------------------+----...+
    garis = "+" + "+".join("-" * (w + 2) for w in lebar) + "+"

    print(garis)
    print(baris(judul_kolom))
    print(garis)

    ringkasan = {"TAMBAH": 0, "PINJAM": 0, "KEMBALI": 0, "HAPUS": 0}
    current = riwayat_linked_list.head
    while current is not None:
        r = current.data
        print(baris([r["no_urut"], r["waktu"], r["aksi"], r["kode_buku"],
                     r["judul"], r["nilai_lama"], r["nilai_baru"]]))
        if r["aksi"] in ringkasan:
            ringkasan[r["aksi"]] += 1
        current = current.next
    print(garis)

    total = sum(ringkasan.values())
    print(f"Ringkasan: TAMBAH {ringkasan['TAMBAH']} | "
          f"PINJAM {ringkasan['PINJAM']} | "
          f"KEMBALI {ringkasan['KEMBALI']} | "
          f"HAPUS {ringkasan['HAPUS']} | Total {total}")