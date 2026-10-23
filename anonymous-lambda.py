# lambda function

def f_kuadrat(angka):
    return angka**2

print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")

# menggunakan lambda
# output = lambda argument; expression
kuadrat = lambda angka:angka**2
print(f"hasil dari lambda kuadrat = {kuadrat(5)}")

pangkat = lambda num,pow : num**pow
print(f"hasil lambda pangkat = {pangkat(4,2)}")

## kegunaan dari fungsi ini

# sorting untuk list
data_list = ["Musashi", "Ganryu", "Takamura"]
data_list.sort()
print(f"sorted list = {data_list}")

# sorting pakai panjang
def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama)
print(f"sorted list by panjang = {data_list}")
data_list.sort(key=lambda nama:len(nama))
print(f"sorted list by lambda = {data_list}")