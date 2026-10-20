def hapus_buku(daftar_buku):
    if not daftar_buku:
        print("\n[!] Data buku masih kosong.")
        return

    katakunci = input("Masukkan ID atau Judul buku yang ingin dihapus: ").strip().lower()
    if not katakunci:
        print("\n[!] Input tidak boleh kosong.")
        return

    buku_ditemukan = None
    for buku in daftar_buku:
        if str(buku.get('id', '')).lower() == katakunci or str(buku.get('judul', '')).lower() == katakunci:
            buku_ditemukan = buku
            break

    if buku_ditemukan:
        konfirmasi = input(f"Apakah kamu yakin ingin menghapus '{buku_ditemukan.get('judul')}'? (y/n): ").strip().lower()
        if konfirmasi == 'y':
            daftar_buku.remove(buku_ditemukan)
            print("\n[✓] Buku berhasil dihapus.")
        else:
            print("\n[-] Penghapusan dibatalkan.")
    else:
        print("\n[!] Buku tidak ditemukan.")