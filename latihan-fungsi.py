'''Latihan Fungsi'''

import os

# program menghitung luas dan keliling persegi panjang

# membuat header program
#os.system("cls")
#print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
#print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
#print(F"{'-'*40:^40}")

# mengambil input user
#LEBAR = int(input("masukkan nilai lebar: "))
#PANJANG = int(input("masukkan nilai panjang: "))

## program menghitung luas
#LUAS = PANJANG*LEBAR
#KELILING = 2*(PANJANG+LEBAR)

## tampilan hasilnya
#print(f"hasil perhitungan luas = {LUAS}")
#print(f"hasil perhitungan keliling = {KELILING}")

def header():
    '''fungsi header'''
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(F"{'-'*40:^40}")

def input_user():
    '''fungsi input user'''
    # mengambil input user
    lebar = int(input("masukkan nilai lebar: "))
    panjang = int(input("masukkan nilai panjang: "))

    return lebar, panjang

def hitung_luas(lebar,panjang):
    '''fungsi luas'''
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''fungsi keliling'''
    return 2*(lebar+panjang)

def display(message, value):
    ''' fungsi display'''
    print(f" hasil perhitungan {message} = {value}")


# program utamanya
while True:
    header()
    opsi = input("pilih opsi (1. hitung luas, 2. hitung keliling, 3. hitung keduanya): ")
    if opsi == "1":
        LEBAR, PANJANG = input_user()
        LUAS = hitung_luas(LEBAR,PANJANG)
        display("luas", LUAS)

    elif opsi == "2":
        LEBAR, PANJANG = input_user()
        KELILING = hitung_keliling(LEBAR,PANJANG)
        display("keliling", KELILING)

    elif opsi == "3":
        LEBAR, PANJANG = input_user()
        LUAS = hitung_luas(LEBAR,PANJANG)
        KELILING = hitung_keliling(LEBAR,PANJANG)
        display("luas", LUAS)
        display("keliling", KELILING)

    isContinue = input ("apakah lanjut(y/n)?")
    if isContinue == "n":
        break
print("Program seleai, terima kasih")

