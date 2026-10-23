kode_token = ""

while kode_token != "abc":
    kode_token = input("Masukkan kode token akses ujian: ")
    if kode_token != "abc":
        print("Kode token salah. Silakan coba lagi.")
print("Kode token valid. Anda dapat memulai ujian.")