# Latihan perulangan membuat segitiga

sisi = 9

# 1. Menggunakan for

# dummy variable

print("awal for")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

print("akhir dari for")

# 2. Menggunakan while

print("awal while")
count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

print ("akhir dari while")

# 3. hanya ganjil saja

print("awal while")
count = 1
while True:
   # print jika ganjil
    if (count%2):
        print("*"*count)
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break

print ("akhir dari while")

# 4. hanya ganjil saja

print("awal while")
count = 1
spasi = int(sisi/2)

while True:
    if (count%2):
        # print jika ganjil
        print(" "*spasi, "+"*count)
        spasi -= 1
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break

print ("akhir dari while")

# 5. belah ketupat

print("awal belah ketupat")
count = 1
spasi = int(sisi/2)

while True:
    if (count%2):
        # print jika ganjil
        print(" "*spasi, "+"*count)
        spasi -= 1
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break

while True:
    if (count%2):
        spasi += 1
        # print jika ganjil
        print(" "*spasi, "+"*count)
        count -= 1
    else:
        # akan kembali ke atas jika ganjil
        count -= 1

    # akan break jika count melebihi sisi
    if count == 0:
        break


print ("akhir dari belah ketupat")



