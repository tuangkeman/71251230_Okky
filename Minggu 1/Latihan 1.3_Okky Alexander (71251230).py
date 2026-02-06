saldo = 200000000
target = 400000000
bunga = 0.10
tahun = 0

while saldo < target:
    saldo += saldo * bunga
    tahun += 1
    print(f"Tahun ke-{tahun}: Rp {saldo:,.0f}")
print(f"\nWaktu yang dibutuhkan adalah {tahun} tahun.")