def ubah_status_buku(daftar_buku):
    print("\n=== UBAH STATUS BUKU ===")
    id_buku = input("Masukkan ID Buku yang ingin diubah statusnya: ").strip()
    
    for buku in daftar_buku:
        if buku['id'] == id_buku:
            print(f"Judul Buku : {buku['judul']}")
            print(f"Status Saat Ini : {buku['status']}")
            
            print("\nPilih Status Baru:")
            print("1. Tersedia")
            print("2. Dipinjam")
            pilihan = input("Pilihan (1/2): ").strip()
            
            if pilihan == '1':
                buku['status'] = 'Tersedia'
                print("Status berhasil diubah menjadi 'Tersedia'.")
            elif pilihan == '2':
                buku['status'] = 'Dipinjam'
                print("Status berhasil diubah menjadi 'Dipinjam'.")
            else:
                print("Pilihan tidak valid.")
            return daftar_buku
            
    print("Buku dengan ID tersebut tidak ditemukan.")
    return daftar_buku


def tampilkan_status(daftar_buku):
    print("\n=== DAFTAR STATUS BUKU ===")
    if not daftar_buku:
        print("Belum ada data buku.")
        return
        
    for buku in daftar_buku:
        print(f"ID: {buku['id']} | Judul: {buku['judul']} | Status: {buku['status']}")