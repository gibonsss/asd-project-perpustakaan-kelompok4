def cari_buku(daftar_buku):
    if not daftar_buku:
        print("\n[!] Data buku masih kosong.")
        return

    katakunci = input("Masukkan kata kunci pencarian (ID/Judul/Penulis): ").strip().lower()
    if not katakunci:
        print("\n[!] Kata kunci tidak boleh kosong.")
        return

    hasil = [
        buku for buku in daftar_buku
        if katakunci in str(buku.get('id', '')).lower()
        or katakunci in str(buku.get('judul', '')).lower()
        or katakunci in str(buku.get('penulis', '')).lower()
    ]

    if hasil:
        print(f"\n--- Hasil Pencarian ({len(hasil)} ditemukan) ---")
        for idx, buku in enumerate(hasil, 1):
            print(f"{idx}. ID: {buku.get('id', '-')} | Judul: {buku.get('judul', '-')} | Penulis: {buku.get('penulis', '-')} | Status: {buku.get('status', '-')}")
    else:
        print("\n[!] Buku tidak ditemukan.")