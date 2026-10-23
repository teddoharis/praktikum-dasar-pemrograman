def konversi_menit_ke_detik(menit):
    """
    Fungsi untuk mengkonversi menit ke detik
    Parameter:
        menit (int): jumlah menit yang akan dikonversi
    Nilai kembalian:
        detik (int): jumlah detik yang dikonversi dari menit
    """
    detik = menit * 60
    return detik
print(konversi_menit_ke_detik(3))
print(konversi_menit_ke_detik.__doc__) 