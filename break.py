# Break

angka = 0

while angka < 5:
    angka += 1
    print(f"cangka sekarang = {angka}")

    if angka == 3:
        print("bom")
        break

    print("indahnya")

print("program berakhir")

# cara kedua

data_int = int(input("hitung sampai = "))

angka = 0

while True:
    angka += 1
    print(f"angka sekarang adalah {angka}")

    if angka == data_int:
        print(f"count = {angka}")
        break

    print("indahnya")

print("program berakhir")