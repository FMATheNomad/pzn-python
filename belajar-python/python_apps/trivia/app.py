import random

# List kata-kata yang dapat digunakan dalam game
kata_kata = ["apel", "jeruk", "mangga", "pisang", "semangka"]

# Memilih kata acak dari list kata-kata
kata_rahasia = random.choice(kata_kata)

# Membuat string dengan garis-garis untuk menunjukkan jumlah huruf
tebakan = "-" * len(kata_rahasia)

# Mengubah string menjadi list untuk memudahkan manipulasi
tebakan_list = list(tebakan)

# Jumlah kesempatan yang diberikan kepada pengguna
kesempatan = 5

# Menampilkan kata tebakan awal kepada pengguna
print("Tebak kata:", tebakan)

while kesempatan > 0:
    # Meminta pengguna untuk menebak huruf
    tebak = input("Masukkan huruf tebakan: ")

    if len(tebak) != 1:
        print("Masukkan hanya satu huruf!")
        continue

    if tebak in tebakan_list:
        print("Anda sudah menebak huruf ini sebelumnya.")
        continue

    # Mengecek apakah huruf tebakan benar
    if tebak in kata_rahasia:
        for i in range(len(kata_rahasia)):
            if kata_rahasia[i] == tebak:
                tebakan_list[i] = tebak
        print("Huruf tebakan benar!")
    else:
        print("Huruf tebakan salah!")
        kesempatan -= 1
        print("Kesempatan tersisa:", kesempatan)

    # Menampilkan kata tebakan terbaru kepada pengguna
    print("Tebak kata:", "".join(tebakan_list))

    # Mengecek apakah pengguna berhasil menebak kata
    if "".join(tebakan_list) == kata_rahasia:
        print("Selamat, Anda berhasil menebak kata", kata_rahasia)
        break

if kesempatan == 0:
    print("Sayang sekali, Anda gagal menebak kata. Kata yang benar adalah", kata_rahasia)
