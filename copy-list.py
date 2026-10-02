## Teknik menduplikat list

a = ["Amicia", "Hugo", "Lucas"]
print(f"a = {a}")

b = a
print(f"b = {b}")

# kita akan merubah member dari a

# ini akan merubah kedua list
a[1]= "Beatrice"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list a dan b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# menduplikat list dengan copy

print("membuat list c dengan a,copy()")
c = a.copy()

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 0")
c[0] = "Arnaud"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 1")
c[1] = "Hugo"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
