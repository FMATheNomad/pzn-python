def hitung_karakter(teks, karakter):
    count = 0
    for char in teks:
        if char == karakter:
            count += 1
    return count

# Meminta pengguna memasukkan teks
teks = input("Masukkan teks: ")

# Meminta pengguna memasukkan karakter yang ingin dihitung
karakter = input("Masukkan karakter yang ingin dihitung: ")

# Memanggil fungsi hitung_karakter() untuk menghitung jumlah karakter
jumlah_karakter = hitung_karakter(teks, karakter)

# Menampilkan hasil perhitungan
print("Jumlah karakter", karakter, "dalam teks:", jumlah_karakter)