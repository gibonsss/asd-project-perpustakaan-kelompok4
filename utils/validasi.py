"""Fungsi validasi input yang dipakai bersama oleh semua fitur."""
from datetime import datetime


def input_tidak_kosong(label):
    """Meminta input sampai tidak kosong, lalu mengembalikan teksnya."""
    while True:
        nilai = input(f"{label}: ").strip()
        if nilai:
            return nilai
        print(f"Error: {label} tidak boleh kosong.")


def input_tahun(label="Tahun terbit"):
    """Meminta tahun: bilangan bulat positif dan tidak lebih dari tahun sekarang."""
    while True:
        nilai = input(f"{label}: ").strip()
        if not nilai.isdigit() or int(nilai) <= 0:
            print("Error: tahun harus berupa angka bulat positif.")
        elif int(nilai) > datetime.now().year:
            print("Error: tahun tidak boleh lebih besar dari tahun sekarang.")
        else:
            return int(nilai)


def konfirmasi(pesan):
    """Meminta jawaban y/n. Mengembalikan True jika y, False jika n."""
    while True:
        jawab = input(f"{pesan} (y/n): ").strip().lower()
        if jawab in ("y", "n"):
            return jawab == "y"
        print("Error: jawab dengan y atau n.")
