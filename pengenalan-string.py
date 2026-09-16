data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backslash
print("C:\\user\\Lenovo")

# tab
print("Masuk\t\t\tpak, semakin jauhan")

# backspace
print("namirah \balbanjary")

# newline
print("baris pertama.\nbaris kedua.") # LF -> Line feed -> unix, macos,linux
print("baris pertama.\rbaris kedua.") # CR -> Carriage return ->commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") # CRLF -> Line Feed Carriage Return -> dipakai oleh windows

# 3. String literal atau raw

# hati-hati
print('C:\\new folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : Namirah
Kelas : 3 SMA
""")

# multiline literal string & raw
print(r"""
Nama : Namirah
Kelas : 3 SMA
Website: www.namirah/newID
""")