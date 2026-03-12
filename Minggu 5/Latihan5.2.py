def cek_digit_belakang(a, b, c):
    x = a % 10
    z = b % 10
    v = c % 10
    if x == z or z == v or v == x:
        return True
    else:
        return False

try:
    a = int(input("Masukkan Input pertama: "))
    b = int(input("Masukkan Input kedua: "))
    c = int(input("Masukkan Input ketiga: "))
    
    hasil = cek_digit_belakang(a, b, c)
    print(f"Output = {hasil}")
    
except ValueError:
    print("Mohon masukkan angka bulat yang valid.")