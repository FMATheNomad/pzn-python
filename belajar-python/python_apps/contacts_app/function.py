def daftar_kontak(kontak):  # Menerima variabel kontak sebagai argumen
    print("\n=== Daftar Kontak ===")
    if not kontak:
        print("Belum ada kontak yang tersimpan.")
    else:
        for i, kontak in enumerate(kontak, start=1):
            print(f"{i}. Nama: {kontak['Nama']}")
            print(f"   Email: {kontak['Email']}")
            print(f"   No. Telepon: {kontak['No. Telepon']}")

def tambah_kontak(kontak):  # Menerima variabel kontak sebagai argumen
    print("\n=== Tambah Kontak ===")
    nama = input("Nama: ")
    email = input("Email: ")
    telepon = input("No. Telepon: ")
    kontak_baru = {
        "Nama": nama,
        "Email": email,
        "No. Telepon": telepon
    }
    kontak.append(kontak_baru)
    print("Kontak berhasil ditambahkan.")

def hapus_kontak(kontak):  # Menerima variabel kontak sebagai argumen
    print("\n=== Hapus Kontak ===")
    nama = input("Nama kontak yang ingin dihapus: ")
    found = False
    for i, kontak in enumerate(kontak):
        if kontak["Nama"].lower() == nama.lower():
            kontak.remove(kontak)
            found = True
            print(f"Kontak dengan nama {nama} berhasil dihapus.")
            break
    if not found:
        print(f"Kontak dengan nama {nama} tidak ditemukan.")

def cari_kontak(kontak):  # Menerima variabel kontak sebagai argumen
    print("\n=== Cari Kontak ===")
    nama = input("Nama kontak yang ingin dicari: ")
    found = False
    for kontak in kontak:
        if kontak["Nama"].lower() == nama.lower():
            print(f"Nama: {kontak['Nama']}")
            print(f"Email: {kontak['Email']}")
            print(f"No. Telepon: {kontak['No. Telepon']}")
            found = True
            break
    if not found:
        print(f"Kontak dengan nama {nama} tidak ditemukan.")
