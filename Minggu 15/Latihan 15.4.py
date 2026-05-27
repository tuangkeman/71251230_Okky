def jumladgt(n):
    n = abs(n)
    if n < 10:
        return n
    return (n % 10) + jumladgt(n // 10)

bilangan = int(input("Masukkan bilangan: "))

digits = [int(d) for d in str(abs(bilangan))]
proses = " + ".join(map(str, digits))
hasil = jumladgt(bilangan)
 
print(f"Jumlah digit dari {bilangan}: {proses} = {hasil}")