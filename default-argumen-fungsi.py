'''Default Argumen'''

# def fungsi(argument):
# def fungsi(argument = nilai defaultnya):

# contoh 1
def say_hello(nama = "Ganteng"):
    '''fungsi dengan default argument'''
    print(f"Hello {nama}")

say_hello("Musashi")
say_hello()

# contoh 2
def sapa_dia(nama, pesan = "Apa kabar?"):
    '''fungsi input biasa, dan satu fefault argument'''
    print(f"hai {nama} {pesan}")

sapa_dia("Musashi", "Hai Keren")
sapa_dia("Musashi")

# contoh 3
def hitung_pangkat(angka, pangkat=2):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(2,4))

hasil = hitung_pangkat(pangkat=3, angka=5)
print(hasil)

# contoh 4
def fungsi(input1=1, input2=2, input3=3, input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input3=10))