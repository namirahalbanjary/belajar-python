# operator dictionary

data_dict = {
    "ac": "amicia",
    "hg": "hugo",
    "sp": "sophia",
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# mengecek key exist atau tidak
KEY = "ac"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

# mengakses value (read) dengan get
print(data_dict["ac"])
print(data_dict.get("ac"))
print(data_dict.get("ys", "key tidak ditemukan"))  # jika key tidak ada, akan mengembalikan default value

# mengupdate data
data_dict["ac"] = "amicia keren"
print(data_dict)
data_dict["bc"] = "Beatrice"
print(data_dict)

data_dict.update({"lc":"Lucas"})
print(data_dict)

# menghapus data pada dictionary
del data_dict["lc"]
print(data_dict)