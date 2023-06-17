def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print(f"Total {list_angka} = {total}")
jumlahkan(10,10,10,10,10,10)
#argument list hanya bisa dibuat satu, dan jika ingin membuat argument lain maka tulis nya harus di depan sebelum argumen list