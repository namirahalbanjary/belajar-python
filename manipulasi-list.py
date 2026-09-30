## Operasi

# index  0(-3)     1(-2)    2(-1)
data = ["Amicia", "Hugo", "Lucas"]

# mengambil data dari list ini
data_0 = data[0]
print(f"data pertama(index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir = {data_terakhir}")

data_amicia = data[-3]
print(f"data amicia = {data_amicia}")

#mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

## manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

data.insert(1,"Bricia")
print(f"data sesudah ditambah = \n{data}")

# menambah di akhir list
data.append("mama")
print(f"data ditambah lagi = \n{data}")

# menambah list dengan list
data_baru = ["Sophia", "Leni", "Varo"]
data.extend(data_baru)
print(f"data gabungan =\n{data}")

# merubah data
# kita ubah data 2 menjadi Irene
data[2] = "Irene"
print(f"data rubah = {data}")

# menghilangkan data

data.remove("Bricia")
print(f"data remove = {data}")
# data remove akan eror kalau data tidak sesuai

# menghilangkan data paling belakang
data.pop()
print(f"data akhir = {data}")