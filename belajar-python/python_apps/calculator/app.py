# Fungsi untuk menjumlahkan dua angka
def tambah(a, b):
    return a + b

# Fungsi untuk mengurangkan dua angka
def kurang(a, b):
    return a - b

# Fungsi untuk mengalikan dua angka
def kali(a, b):
    return a * b

# Fungsi untuk membagi dua angka
def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Pembagian dengan nol tidak dapat dilakukan."

# Menampilkan menu operasi
print("Pilih operasi matematika:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

# Meminta pengguna memilih operasi
operasi = input("Masukkan nomor operasi (1/2/3/4): ")

# Meminta pengguna memasukkan dua angka
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Melakukan operasi sesuai pilihan pengguna
if operasi == "1":
    hasil = tambah(angka1, angka2)
    print("Hasil penjumlahan:", hasil)
elif operasi == "2":
    hasil = kurang(angka1, angka2)
    print("Hasil pengurangan:", hasil)
elif operasi == "3":
    hasil = kali(angka1, angka2)
    print("Hasil perkalian:", hasil)
elif operasi == "4":
    hasil = bagi(angka1, angka2)
    print("Hasil pembagian:", hasil)
else:
    print("Pilihan operasi tidak valid.")