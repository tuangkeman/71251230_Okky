gaji_per_jam = float(input("Masukkan gaji per jam yang diinginkan: "))
jam_per_minggu = int(input("Masukkan jumlah jam kerja per minggu: "))
pendapatan_kotor = gaji_per_jam * jam_per_minggu * 5
pajak = 0.14 * pendapatan_kotor
pendapatan_bersih = pendapatan_kotor - pajak
beli_baju = 0.1 * pendapatan_bersih
beli_alat_tulis = 0.01 * pendapatan_bersih
sisa_uang_setelah_belanja = pendapatan_bersih - beli_baju - beli_alat_tulis
total_sedekah = 0.25 * sisa_uang_setelah_belanja
sedekah_anak_yatim = 0.30 * total_sedekah
sedekah_dhuafa = total_sedekah - sedekah_anak_yatim
print("Ringkasan Keuangan Budi")
print(f"1. Pendapatan sebelum pajak: Rp {pendapatan_kotor:,.2f}")
print(f"2. Pendapatan setelah pajak: Rp {pendapatan_bersih:,.2f}")
print(f"3. Pengeluaran pakaian & aksesoris: Rp {beli_baju:,.2f}")
print(f"4. Pengeluaran alat tulis: Rp {beli_alat_tulis:,.2f}")
print(f"5. Total uang yang disedekahkan: Rp {total_sedekah:,.2f}")
print(f"6. Sedekah untuk anak yatim: Rp {sedekah_anak_yatim:,.2f}")
print(f"7. Sedekah untuk kaum dhuafa: Rp {sedekah_dhuafa:,.2f}")