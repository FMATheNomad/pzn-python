import function

def main():
    kontak = []  # Memindahkan deklarasi variabel kontak ke sini
    while True:
        print("\n=== Management Kontak ===")
        print("1. Daftar Kontak")
        print("2. Tambah Kontak")
        print("3. Hapus Kontak")
        print("4. Cari Kontak")
        print("0. Keluar")

        menu = input("Pilih menu: ")

        if menu == "1":
            function.daftar_kontak(kontak)  # Melewatkan variabel kontak sebagai argumen
        elif menu == "2":
            function.tambah_kontak(kontak)  # Melewatkan variabel kontak sebagai argumen
        elif menu == "3":
            function.hapus_kontak(kontak)  # Melewatkan variabel kontak sebagai argumen
        elif menu == "4":
            function.cari_kontak(kontak)  # Melewatkan variabel kontak sebagai argumen
        elif menu == "0":
            print("Program selesai. Sampai jumpa!")
            break
        else:
            print("Menu tidak valid. Silakan pilih menu yang sesuai.")

if __name__ == "__main__":
    main()
