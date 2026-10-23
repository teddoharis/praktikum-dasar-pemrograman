biaya_admin = 2500
def hitung_total(harga_barang):
    total = harga_barang + biaya_admin
    print("Total harga adalah:", total)
    return total

total_harga = hitung_total(15000)