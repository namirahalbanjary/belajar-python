import datetime


mahasiswa1 = {
    'nama' : 'Musashi',
    'nim': 1321198199,
    'sks_lulus': 132,
    'beasiswa': False,
    'lahir': datetime.datetime(2013,1,21)
}

mahasiswa2 = {
    'nama' : 'Alicia',
    'nim': 1129391,
    'sks_lulus': 112,
    'beasiswa': True,
    'lahir': datetime.datetime(2011,12,9)
}

mahasiswa3 = {
    'nama' : 'Revo',
    'nim': 1852215,
    'sks_lulus': 118,
    'beasiswa': False,
    'lahir': datetime.datetime(2018,5,22)
}

data_mahasiswa = {
    'MAH001': mahasiswa1,
    'MAH002': mahasiswa2,
    'MAH003': mahasiswa3
}

print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<9}")
print("-"*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA!s:^9} {LAHIR:<10}")