# SOAL 4.1
try:
    derajat = int(input("Masukkan suhu tubuh: ")) 

    if derajat >= 38:
        print("Anda demam")
    else:
        print("Anda tidak demam")

except ValueError:
    print("Anda salah memasukan input, tolong masukan input yang benar kembali ")

# SOAL 4.2  
try:
    bilangan = int(input("Masukkan suatu bilangan: "))
    if bilangan > 0:
        print("Positif")
    elif bilangan < 0:
        print("Negatif")
    elif bilangan == 0:
        print("Nol")

except ValueError:
    print("Eror, coba masukan input dengan benar")

# SOAL 4.3
try:
    o = int(input("Masukkan bilangan pertama: "))
    p = int(input("Masukkan bilangan kedua: "))
    m = int(input("Masukkan bilangan ketiga: "))

    if o > p and o > m:
        print("Terbesar: ", o)
    elif p > o and p > m:
        print("Terbesar: ", p)
    elif m > o and m > p:
        print("Terbesar: ", m)

except ValueError:
    print("Input kamu salah, coba lagi ")