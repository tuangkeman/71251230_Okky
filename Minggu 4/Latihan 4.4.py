try:
    sisipertama = int(input("Masukan angka untuk sisi 1: "))
    sisidua = int(input("Masukan angka untuk sisi 2: "))
    akhirrek = int(input("Masukan angka untuk sisi 3: "))
    if sisipertama == sisidua == akhirrek:
        print("3 sisi sama")
    elif sisipertama == sisidua or sisipertama == akhirrek or sisidua == akhirrek:
        print("2 sisi sama")
    else:
        print("Tidak ada yang sama")
except ValueError:
        print("Anda salah memasukan input, Tolong masukan input kembali dengan benar")
    