harga_awal = 650000
berat_emas = 25
modal_beli = harga_awal * berat_emas

harga_kenaikan = 685000
nilai_saatini = harga_kenaikan * berat_emas

untung_rp_1 = nilai_saatini - modal_beli
untung_persen_1 = (untung_rp_1 / modal_beli) * 100

print("Pembelian Gerard Pertama (25 gram):")
print(f"Modal Awal: Rp {modal_beli:,}")
print(f"Keuntungan: Rp {untung_rp_1:,}")
print(f"Persentase Keuntungan: {untung_persen_1:.2f}%")
print()


harga_pembelian_kedua = 685000
berat_pembelian_kedua = 15
modal_pembelian_kedua = harga_pembelian_kedua * berat_pembelian_kedua


total_berat = berat_emas + berat_pembelian_kedua
total_modal = modal_beli + modal_pembelian_kedua

harga_akhir = 715000
nilai_akhir = total_berat * harga_akhir

untung_rp_total = nilai_akhir - total_modal
untung_persen_total = (untung_rp_total / total_modal) * 100

print("Pembelian Gerard Kedua (15 gram):")
print(f"Total Modal (25g + 15g): Rp {total_modal:,}")
print(f"Nilai Emas Akhir: Rp {nilai_akhir:,}")
print(f"Total Keuntungan: Rp {untung_rp_total:,}")
print(f"Total Persentase Keuntungan: {untung_persen_total:.2f}%")