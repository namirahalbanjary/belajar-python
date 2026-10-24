## Global dan Local Scope

nama_global = "Musashi" # <- ini adalah variabel global

# akses variabel global dalam fungsi
def fungsi():
    print(f"fungsi menampilkan {nama_global}")

fungsi()

#akses variabel global dalam loop
for i in range(0,5):
    print(f"loop{i} - {nama_global}")

# percabangan
if True:
    print(f"if menampilkan {nama_global}")

## variabel local scope
def fungsi2():
    nama_lokal = "Ganryu"

fungsi2()
#print(nama_lokal) # tidak bisa dilakukan

## contoh penggunaan

def say_musashi():
    print(f"hello {nama}")

nama = "Musashi"
say_musashi()

## contoh 2: merubah variasi global
angka = 0 
nama = "Ganryu"

def ubah(nilai_baru, nama_baru):
    global angka  #fungsi ini mendapat akses merubah angka
    global nama
    angka = nilai_baru
    nama = nama_baru

print(f"Sebelum {angka, nama}")
ubah(10, "Musashi")
print(f"Sesudah {angka, nama}")

## contoh 3

angka = 0

for i in range(0,5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)
