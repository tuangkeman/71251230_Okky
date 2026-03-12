def ips(x):
    total = 0
    bobot = 0
    for i in range(1,x+1):
        nilai = str(input(f"Nilai Mk {i}: "))
        if nilai == "A":
            bobot += 4
        elif nilai == "B":
            bobot += 3
        elif nilai == "C":
            bobot += 2
        elif nilai == "D":
            bobot += 1
        else:
            nilai += 0
    total = bobot / x
    print(f"Nilai IPS anda semester ini {total:.2f}")
print("Program perhitungan IPS mahasiswa")
ips(x = int(input("Berapa jumlah mata kuliah? ")))