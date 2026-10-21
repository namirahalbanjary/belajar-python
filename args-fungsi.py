'''*args'''

# memasukkan data/argument

def fungsi (nama, tinggi, berat):
    print(f"{nama} memiliki tinggi {tinggi} dan berat {berat}")

fungsi("Musashi", 180, 70)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} memiliki tinggi {tinggi} dan berat {berat}")

fungsi(["Musashi", 180, 70])

# menggunakan *args
def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} memiliki tinggi {tinggi} dan berat {berat}")

fungsi("Musashi", 180, 70)

# studi kasus

def tambah(*data): # data tipenya tuple dan bisa diiterasi
    output = 0 
    for angka in data:
        output += angka

    return output

hasil = tambah(1,2,3,4,5,6,7,8,9,10)
print(f"Hasil = {hasil}")

hasil = tambah (10, 5, 15)
print(f"Hasil = {hasil}")