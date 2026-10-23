def main():
    nomor = 1
    header(nomor, "Apa Ibukota Indonesia?")
    jawaban = input("Jawaban Anda: ")
    def periksa_jawaban(jawaban, arg1):
        ...

    hasil = periksa_jawaban(jawaban, "B")
    if hasil:
        jumlah_benar = 1
    else:
        jumlah_benar = 0
def hitung_skor(jumlah_benar, arg1):
    ...

class jumlah_benar:
    ...

skor_akhir = hitung_skor(jumlah_benar, 1)
print(f"Skor akhir: {skor_akhir}")

def header(nomor, soal):
    print("*** Sesi Ujian ***")
    print(f"Soal {nomor}")
    print(soal)

main()