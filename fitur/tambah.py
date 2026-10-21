def tambah_buku(daftar_buku):
    print("\n=== TAMBAH BUKU BARU ===")
    id_buku = input("Masukkan ID Buku: ").strip()
    
    # Cek apakah ID buku sudah terdaftar
    for buku in daftar_buku:
        if buku['id'] == id_buku:
            print("Gagal: ID Buku sudah terdaftar!")
            return daftar_buku
            
    judul = input("Masukkan Judul Buku: ").strip()
    penulis = input("Masukkan Penulis Buku: ").strip()
    tahun = input("Masukkan Tahun Terbit: ").strip()
    
    buku_baru = {
        'id': id_buku,
        'judul': judul,
        'penulis': penulis,
        'tahun': tahun,
        'status': 'Tersedia'
    }
    
    daftar_buku.append(buku_baru)
    print(f"Buku '{judul}' berhasil ditambahkan!")
    return daftar_buku