tinggi_cm = int(input("Masukkan tinggi badan (cm): "))
bmi_harapan = float(input("Masukkan nilai BMI yang diharapkan: "))
tinggi_m = tinggi_cm / 100
berat_perlu = bmi_harapan * (tinggi_m**2)
print(f"Berat badan yang diperlukan adalah: {berat_perlu:.2f} kg")