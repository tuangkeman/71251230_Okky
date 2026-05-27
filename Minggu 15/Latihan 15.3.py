def suku(k):
    return (2 ** k) - 1
 
def drt(k):
    if k == 1:
        return 1
    return suku(k) + drt(k - 1)

n = int(input("Masukkan jumlah suku deret (n): "))

print("Deret: ", end="")
for i in range(1, n + 1):
    if i < n:
        print(suku(i), end=" + ")
    else:
        print(suku(i), end="")
 
print(f" = {drt(n)}")
 