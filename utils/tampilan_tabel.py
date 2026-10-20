# utils/tampilan.py

def cetak_tabel(daftar_buku):
    """
    Mencetak daftar buku dalam format tabel yang rapi.
    Menerima parameter berupa list of dictionaries.
    """
    if not daftar_buku:
        print("[-] Tidak ada data buku untuk ditampilkan.\n")
        return

    # Menentukan lebar setiap kolom tabel
    lebar_id = 5
    lebar_judul = 40
    lebar_penulis = 25
    lebar_tahun = 6

    # Garis pembatas tabel
    garis_pembatas = "-" * (lebar_id + lebar_judul + lebar_penulis + lebar_tahun + 13)

    # Mencetak Header Tabel
    print(garis_pembatas)
    print(f"| {'ID':<{lebar_id}} | {'Judul Buku':<{lebar_judul}} | {'Penulis':<{lebar_penulis}} | {'Tahun':<{lebar_tahun}} |")
    print(garis_pembatas)

    # Mencetak Isi Tabel
    for buku in daftar_buku:
        print(f"| {buku['id']:<{lebar_id}} | {buku['judul']:<{lebar_judul}} | {buku['penulis']:<{lebar_penulis}} | {buku['tahun']:<{lebar_tahun}} |")
    
    print(garis_pembatas)
    print(f"Total: {len(daftar_buku)} buku\n")