
n = int(input('Masukkan jumlah kategori: '))

data_aplikasi = {}

for i in range(n):
    nama_kategori = input('Masukkan nama kategori: ')
    print('Masukkan 5 nama aplikasi di kategori', nama_kategori)
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input('Nama aplikasi: ')
        aplikasi.append(nama_aplikasi)

    data_aplikasi[nama_kategori] = aplikasi

print('\n=== Daftar Aplikasi per Kategori ===')
for kategori, aplikasi in data_aplikasi.items():
    print(f'{kategori}: {aplikasi}')

daftar_aplikasi_set = []
for aplikasi in data_aplikasi.values():
    daftar_aplikasi_set.append(set(aplikasi))

hasil_semua = daftar_aplikasi_set[0]
for i in range(1, len(daftar_aplikasi_set)):
    hasil_semua = hasil_semua.intersection(daftar_aplikasi_set[i])

print('\n Aplikasi yang muncul di SEMUA kategori ')
print(hasil_semua if hasil_semua else 'Tidak ada aplikasi yang muncul di semua kategori')

print('\n Aplikasi yang hanya muncul di SATU kategori saja ')
kategori_list = list(data_aplikasi.keys())
for idx, (kategori, aplikasi_set) in enumerate(zip(kategori_list, daftar_aplikasi_set)):

    set_lain = set()
    for j, s in enumerate(daftar_aplikasi_set):
        if j != idx:
            set_lain = set_lain.union(s)

    hanya_disini = aplikasi_set - set_lain
    print(f'{kategori}: {hanya_disini}')

if n > 2:
    print('\n Aplikasi yang muncul tepat di DUA kategori ')
    muncul_dua = set()
    for i in range(len(daftar_aplikasi_set)):
        for j in range(i + 1, len(daftar_aplikasi_set)):

            irisan_dua = daftar_aplikasi_set[i].intersection(daftar_aplikasi_set[j])

            for k in range(len(daftar_aplikasi_set)):
                if k != i and k != j:
                    irisan_dua = irisan_dua - daftar_aplikasi_set[k]
            if irisan_dua:
                print(f'{kategori_list[i]} & {kategori_list[j]}: {irisan_dua}')
                muncul_dua = muncul_dua.union(irisan_dua)
    if not muncul_dua:
        print('Tidak ada aplikasi yang muncul tepat di dua kategori')
