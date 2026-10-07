# looping dari list

# for loop
print("=== for loop ===")
kumpulan_angka = [1,1,2,1,1,3]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["Amicia", "Hugo", "Lucas", "Beatrce", "Sophia"]

for nama in peserta:
    print(f"nama = {nama}")

# for loop dan range
print("=== for loop dan range ===")
kumpulan_angka = [1,6,2,1,1,2]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

# while
print("=== while loop ===")
kumpulan_angka = [1,6,2,1,1,2]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

# list comprehension
print("=== list comprehension ===")
data = ["Amicia", 6,1,5, "Hugo"]

[print(f"data = {i}") for i in data]

angka = [1,6,2,1,1,2]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# enumerate
print("=== enumerate ===")
data_list = ["Amicia", 6,1,5, "Hugo"]

for index, data in enumerate(data_list):
    print(f"index = {index}, data = {data}")
