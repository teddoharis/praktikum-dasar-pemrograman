print("=== Konversi detik ke jam, menit, dan detik ===")
detik = int(input("Masukkan jumlah detik: "))
jam = detik // 3600
sisa_detik = detik % 3600
menit = sisa_detik // 60
detik_akhir = sisa_detik % 60
print(f"{jam:02d}:{menit:02d}:{detik_akhir:02d}")