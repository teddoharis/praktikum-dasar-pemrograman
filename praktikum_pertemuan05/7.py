def hitung_subtotal(harga, jumlah):
    subtotal = harga * jumlah
    return subtotal

def hitung_diskon(subtotal):
    if subtotal >= 100000:
        diskon = subtotal * 0.10
    else:
        diskon = 0
    return diskon
def tampilkan_struk(nama_barang, subtotal, diskon):
    total = subtotal - diskon
    print("===== STRUK PEMBELIAN =====")
    print("Nama Barang:", nama_barang)
    print("Subtotal:", int(subtotal))
    print("Diskon:", float(diskon))
    print("Total:", int(total))
    return

nama_barang = "Buku Tulis"
harga = 25000
jumlah = 5
subtotal = hitung_subtotal(harga, jumlah)
diskon = hitung_diskon(subtotal)
tampilkan_struk(nama_barang, subtotal, diskon)