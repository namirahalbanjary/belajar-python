data_angka = [1,4,1,1,3,9,1,8,1,8]

print(f"data angka = \n{data_angka}")

# count data

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data (index)

data = ["Amicia", "Hugo", "Lucas", "Beatrice"]
print(f"data = {data}")

index_lucas = data.index("Lucas")
index_beatrice = data.index("Beatrice")
print(f"index si Lucas = {index_lucas}")
print(f"index si Beatrice = {index_beatrice}")

# mengurutkan list
print(f"data angka sebelum sort = {data_angka}")
data_angka.sort()
print(f"data angka sort = {data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# balik listnya 
data_angka.reverse()
data.reverse()
print(f"data di reverse = \n{data_angka} \n{data}")
