def jmlrek(p):
    if p < 1 or p > 12:
        return None 
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return m[p - 1]
try:
    x = int(input("Masukkan bulan dalam bentuk angka: "))
    z = jmlrek(x)

    if z is None:
        print("Bulan tidak valid.")
    else:
        print("Jumlah hari:", z)
except ValueError:
    print("Input tidak valid. Masukkan angka antara 1 sampai 12.")
