# ============================
# Program Pembelian Furnitur
# ============================

# --- Data Login ---
username_benar = "Agung"
nim_benar = "12345"

# --- Data Furnitur ---
harga_sofa = 500000
harga_meja = 250000
harga_rak = 150000

# --- Variabel Percobaan Login ---
maksimal_login = 3
percobaan = 0

# ============================
# Validasi Login
# ============================

while percobaan < maksimal_login:
    print("\n=== LOGIN ===")
    username = input("Masukkan Nama (username): ")
    nim = input("Masukkan NIM (password): ")

    if username == username_benar and nim == nim_benar:
        print("Login berhasil!\n")
        break
    else:
        percobaan += 1
        print(f"Login salah! Percobaan ke-{percobaan}")
        if percobaan == maksimal_login:
            print("Login gagal 3 kali. Program berhenti.")
            exit()   # hentikan program

# ============================
# Menu Pembelian Furnitur
# ============================

while True:
    print("\n=== MENU PEMBELIAN FURNITUR ===")
    print("1. Sofa        - Rp 500.000")
    print("2. Meja Belajar- Rp 250.000")
    print("3. Rak Lemari  - Rp 150.000")
    print("4. Keluar")
    
    pilihan = input("Pilih opsi (1-4): ")

    # Keluar dari program
    if pilihan == "4":
        print("Terima kasih telah menggunakan program ini.")
        break

    # Cek pilihan valid
    if pilihan not in ["1", "2", "3"]:
        print("Pilihan tidak valid! Silakan pilih 1-4.")
        continue

    # Input jumlah unit
    try:
        jumlah_unit = int(input("Masukkan jumlah unit yang ingin dibeli: "))
        if jumlah_unit <= 0:
            print("Jumlah unit harus lebih dari 0!")
            continue
    except ValueError:
        print("Input tidak valid! Masukkan angka.")
        continue

    # Tentukan jenis furnitur dan harga
    if pilihan == "1":
        jenis = "Sofa"
        harga_per_unit = harga_sofa
    elif pilihan == "2":
        jenis = "Meja Belajar"
        harga_per_unit = harga_meja
    else:
        jenis = "Rak Lemari"
        harga_per_unit = harga_rak

    # Hitung total bayar dengan loop for
    total_bayar = 0
    for i in range(jumlah_unit):
        total_bayar += harga_per_unit

    # ============================
    # POIN PLUS: Diskon & Bonus
    # ============================

    potongan = 0
    bonus = ""

    if total_bayar >= 700000:
        potongan = 0.20 * total_bayar
    elif total_bayar >= 500000:
        potongan = 0.08 * total_bayar
    elif total_bayar >= 150000:
        bonus = "Kitchen Set"

    total_setelah_potongan = total_bayar - potongan

    # ============================
    # Tampilkan Hasil
    # ============================
    print("\n=== HASIL PEMBELIAN ===")
    print(f"Jenis Furnitur : {jenis}")
    print(f"Jumlah Unit    : {jumlah_unit}")
    print(f"Total Bayar    : Rp {total_bayar:,}")
    
    if potongan > 0:
        print(f"Potongan       : Rp {int(potongan):,}")
    if bonus != "":
        print(f"Bonus          : {bonus}")
        
    print(f"Total Akhir    : Rp {int(total_setelah_potongan):,}")
    print("=========================\n")