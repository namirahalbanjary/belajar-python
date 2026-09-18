# operator dalam methods

## merubah case dari string

# merubah semua ke upper case

salam = "Assalamualaikum"
print("normal = " + salam)
salam= salam.upper()
print("upper = " + salam)

# merubah semua ke lower case
alay = "aKu KerEn AbiZzZZzz"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan menggunakan isX method

# contoh pengecekanlower case
salam = "halo guys"
apakah_lower = salam.islower() # hasilnya boolean
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() #hasilnya boolean
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <--- untuk mengecek apakah semuanya huruf
# isalnum() <--- huruf dan angka
# isdesimal() <--- angka saja
# isspace() <--- spasi, tab, newline
# istittle()<--- semua kata diawali dengan huruf besar

judul = "Istri Misterius Bos Besar"
cek_judul = judul.istitle() # hasil boolean

print(judul + " is title = " + str(cek_judul))

# ngecek komponen startswith() endswith() <--- bagus
cek_start = "Mianhae Yeobo".startswith("Mianhae")
print("start = " + str(cek_start))

cek_end = "Konseling Online".endswith("Online")
print("end = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku', 'cinta', 'kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = '.'.join(pisah)
print(gabungan)

gabungan = ' ofero '.join(pisah)
print(gabungan)

gabungan = "akuoferocintaoferokamu"
print(gabungan.split('ofero'))

## alokasi karakter rjust() ljust() center()
print(5 * "=" + "data" + "=" * 5)

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,"-")
print("'"+tengah+"'")


## kebalikannya --> strip()
tengah = tengah.strip("-") # menghilangkan tanda -
print("'"+tengah+"'")