# Data kurs mata uang
kurs_usd_ke_eur = 0.82
kurs_eur_ke_usd = 1.22

# Fungsi untuk mengonversi USD ke EUR
def usd_to_eur(usd):
    return usd * kurs_usd_ke_eur

# Fungsi untuk mengonversi EUR ke USD
def eur_to_usd(eur):
    return eur * kurs_eur_ke_usd

# Menampilkan menu konversi mata uang
print("Pilih konversi mata uang:")
print("1. USD ke EUR")
print("2. EUR ke USD")

# Meminta pengguna memilih konversi
pilihan = input("Masukkan nomor konversi (1/2): ")

# Melakukan konversi sesuai pilihan pengguna
if pilihan == "1":
    usd = float(input("Masukkan jumlah USD: "))
    hasil = usd_to_eur(usd)
    print("Hasil konversi:", hasil, "EUR")
elif pilihan == "2":
    eur = float(input("Masukkan jumlah EUR: "))
    hasil = eur_to_usd(eur)
    print("Hasil konversi:", hasil, "USD")
else:
    print("Pilihan konversi tidak valid.")
