''' Fungsi dengan Argument (input) '''

# Template
#def nama_fungsi(argument):
#    Badan Fungsi

def hello_world(nama):
    '''fungsi Hello World menerima imput dengan variable nama'''
    print(f"Selamat datang dunia wahai {nama}")



hello_world("Musashi")
hello_world("Ganryu")

# program tambah
def tambah(angka_1,angka_2):
    '''fungsi tambah'''
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(1,5)
tambah(10000,1)

def say_hi(list_peserta):
    '''fungsi say hi'''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Yang Terhormat {peserta}")


anggota_boyband = ["Musashi", "Ganryu", "Shizuka"]

say_hi(anggota_boyband)