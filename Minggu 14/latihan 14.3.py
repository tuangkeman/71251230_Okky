
def baca_kata(nama_file):
    try:
        with open(nama_file, 'r') as f:
            isi = f.read()

        kata_kata = set()
        for kata in isi.split():

            kata_bersih = kata.strip('.,!?;:\'"()[]').lower()
            if kata_bersih:
                kata_kata.add(kata_bersih)
        return kata_kata
    except FileNotFoundError:
        print(f'Error: File "{nama_file}" tidak ditemukan!')
        return None
    except Exception as e:
        print(f'Error: Tidak bisa membaca file "{nama_file}". {e}')
        return None

nama_file1 = input('Masukkan nama file pertama: ')
nama_file2 = input('Masukkan nama file kedua: ')

kata_file1 = baca_kata(nama_file1)
kata_file2 = baca_kata(nama_file2)

if kata_file1 is not None and kata_file2 is not None:

    kata_sama = kata_file1.intersection(kata_file2)

    print(f'\n Kata-kata di "{nama_file1}" ')
    print(sorted(kata_file1))

    print(f'\n Kata-kata di "{nama_file2}" ')
    print(sorted(kata_file2))

    print(f'\n Kata yang muncul di KEDUA file ')
    print(sorted(kata_sama))
