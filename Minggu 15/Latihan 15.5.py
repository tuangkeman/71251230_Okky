def komb(n, r):
    if r == 0:
        return 1
    if r == n:
        return 1
    return komb(n - 1, r - 1) + komb(n - 1, r)

n = int(input("Masukkan n: "))
r = int(input("Masukkan r: "))
 
if r > n:
    print("Error: r tidak boleh lebih besar dari n!")
else:
    hasil = komb(n, r)
    print(f"C({n}, {r}) = {hasil}")
 