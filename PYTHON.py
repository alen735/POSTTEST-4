# ========================================
# PROGRAM PEMBELIAN FURNITUR
# ========================================

# --- Data login yang benar ---
nama_pengguna = "Agung"          # Username
nim_pengguna = "12345"           # Password

# --- Batas percobaan login ---
maks_percobaan = 3
login_berhasil = False

# ========================================
# Proses LOGIN
# ========================================
for percobaan in range(maks_percobaan):
    print("=== LOGIN ===")
    input_nama = input("Masukkan Nama (username): ")
    input_nim = input("Masukkan NIM (password): ")

    if input_nama == nama_pengguna and input_nim == nim_pengguna:
        print("\n✅ Login berhasil!\n")
        login_berhasil = True
        break
    else:
        print(f"❌ Login gagal! Percobaan ke-{percobaan+1}\n")

if not login_berhasil:
    print("🚫 Batas login habis. Program berhenti.")
    exit()

# ========================================
# Menu Pembelian Furnitur
# ========================================
while True:
    print("=== MENU PEMBELIAN FURNITUR ===")
    print("1. Sofa          - Rp 500.000 / unit")
    print("2. Meja Belajar  - Rp 250.000 / unit")
    print("3. Rak Lemari    - Rp 150.000 / unit")
    print("4. Keluar")

    pilihan_furnitur = input("Pilih opsi (1-4): ")

    # Keluar dari program
    if pilihan_furnitur == "4":
        print("🙏 Terima kasih telah berbelanja!")
        break

    # Validasi input menu
    if pilihan_furnitur not in ["1", "2", "3"]:
        print("⚠️ Pilihan tidak valid! Coba lagi.\n")
        continue

    # Tentukan nama furnitur dan harga
    if pilihan_furnitur == "1":
        nama_furnitur = "Sofa"
        harga_per_unit = 500000
    elif pilihan_furnitur == "2":
        nama_furnitur = "Meja Belajar"
        harga_per_unit = 250000
    elif pilihan_furnitur == "3":
        nama_furnitur = "Rak Lemari"
        harga_per_unit = 150000

    # Input jumlah unit
    jumlah_unit = input(f"Masukkan jumlah {nama_furnitur} yang ingin dibeli: ")

    if not jumlah_unit.isdigit() or int(jumlah_unit) <= 0:
        print("⚠️ Jumlah harus angka positif!\n")
        continue

    jumlah_unit = int(jumlah_unit)

    # ========================================
    # Hitung total bayar (menggunakan for loop)
    # ========================================
    total_bayar = 0
    for i in range(jumlah_unit):
        total_bayar += harga_per_unit

    # ========================================
    # Hitung diskon atau bonus
    # ========================================
    potongan = 0
    bonus = None

    if total_bayar >= 700000:
        potongan = total_bayar * 0.20
    elif total_bayar >= 500000:
        potongan = total_bayar * 0.08
    elif total_bayar >= 150000:
        bonus = "Kitchen Set"

    total_setelah_potongan = total_bayar - potongan

    # ========================================
    # Tampilkan hasil pembelian
    # ========================================
    print("\n=== HASIL PEMBELIAN ===")
    print(f"Jenis Furnitur : {nama_furnitur}")
    print(f"Jumlah Unit    : {jumlah_unit}")
    print(f"Total Bayar    : Rp {total_bayar:,}")

    if potongan > 0:
        print(f"Potongan       : Rp {potongan:,}")
        print(f"Total Akhir    : Rp {total_setelah_potongan:,}")
    else:
        print(f"Total Akhir    : Rp {total_setelah_potongan:,}")

    if bonus:
        print(f"Bonus          : {bonus}")

    print("=============================\n")