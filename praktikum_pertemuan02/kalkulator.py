# Program kalkulator sederhana
print("=== Kalkulator Sederhana ===")
angka1 = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /): ")
angka2 = float(input("Masukkan angka kedua: "))

if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasil: {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"Hasil: {hasil}")
elif operator == "*":
    hasil = angka1 * angka2
    print(f"Hasil: {hasil}")
elif operator == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil: {hasil}")
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
else:
    print("Error: Operator tidak valid.")