def kom(n, r):
    if r == 0:
        return 1
    if r == n:
        return 1
    return kom(n - 1, r - 1) + kom(n - 1, r)
 
n = int(input("Masukkan n: "))
r = int(input("Masukkan r: "))
 
if r > n:
    print("Error: r tidak boleh lebih besar dari n!")
else:
    hasil = kom(n, r)
    print(f"C({n}, {r}) = {hasil}")
 