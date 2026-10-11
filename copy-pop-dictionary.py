# copy dictionary

teman_teman = {
    "dea": "Afrizal",
    "math": "Ajar",
    "mth": "Thoriq",
    "arif": "Muluk Rahman",
    "ihwan": "Riadi"
}

friends = teman_teman.copy()

print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

teman_teman["arif"] = "Muluk"
print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

# pop dictionary (berdasarkan key)
dataDea = friends.pop("dea")
print(f"data Dea: {dataDea}")
print(f"friends: {friends}\n")

# pop item dictionary (yang terakhir aja)
dataTerakhir = friends.popitem()
print(f"data terakhir: {dataTerakhir}\n")
print(f"friends: {friends}\n")