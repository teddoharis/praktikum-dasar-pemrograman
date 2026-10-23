print("=== Total Belanja dengan Diskon ===")
harga_barang = float(input("Masukkan harga barang: "))
jumlah_barang = int(input("Masukkan jumlah barang: "))
persentase_diskon = float(input("Masukkan persentase diskon (misal 10 untuk 10%): "))

total_belanja = harga_barang * jumlah_barang
diskon = total_belanja * (persentase_diskon / 100)
total_bayar = total_belanja - diskon

print(f"Total Belanja: {total_belanja}")
print(f"Diskon: {diskon}")
print(f"Total Bayar: {total_bayar}")