# latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# ++++++3----------10++++++

inputUser = float(input('masukkan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n:'))

# +++++++++3---------------------
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =", isKurangDari)

# ------------------10++++++++
# Memeriksa angka lebih dari 10

isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)

isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan: ", isCorrect)

# --------3+++++++++++++++10---------
# kasus irisan
print("\n",10*"=","\n")
inputUser = float(input('masukkan angka yang bernilai\nlebih dari 3\ndan\nkurang dari 10\n:'))

# -------3+++++++++
# lebih dari 3

isLebihDari = (inputUser > 3)
print("Lebih dari 3 =", isLebihDari)

# ++++++++++++++++10-----------

isKurangDari = (inputUser < 10)
print("Kurang dari 10 =", isKurangDari)

isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukkan: ", isCorrect)

# --------0+++++++++++++++5---------8++++++++11---------

print("\n",10*"=","\n")
inputUser = float(input('masukkan angka yang bernilai\nlebih dari 0,\nkurang dari 5\ndan lebih dari 8,\nkurang dari 11\n:'))

# -------0+++++++++
# lebih dari 0

isLebihDari1 = (inputUser > 0)
print("Lebih dari 0 =", isLebihDari1)

# ++++++++++++++++5-----------

isKurangDari1 = (inputUser < 5)
print("Kurang dari 5 =", isKurangDari1)

# -------8+++++++++
# lebih dari 8

isLebihDari2 = (inputUser > 8)
print("Lebih dari 8 =", isLebihDari2)

# ++++++++++++++++11-----------

isKurangDari2 = (inputUser < 11)
print("Kurang dari 11 =", isKurangDari2)

isCorrect1 = (isKurangDari1 and isLebihDari1)
print("angka yang anda masukkan(1): ", isCorrect1)

isCorrect2 = (isKurangDari2 and isLebihDari2)
print("angka yang anda masukkan(2): ", isCorrect2)

isCorrect = (isCorrect1 or isCorrect2)
print("angka yang anda masukkan: ", isCorrect)

# ++++++0--------5+++++++8--------11++++++++

print("\n",10*"=","\n")
inputUser = float(input('masukkan angka yang bernilai\nkurang dari 0,\nlebih dari 5\ndan kurang dari 8,\nlebih dari 11\n:'))

# +++++++0-----------
# kurang dari 0

isKurangDari1 = (inputUser < 0)
print("Kurang dari 0 =", isKurangDari1)

# ----------5+++++++++

isLebihDari1 = (inputUser > 5)
print("Lebih dari 5 =", isLebihDari1)

# +++++++++++8------
# kurang dari 8

isKurangDari2 = (inputUser < 8)
print("Kurang dari 8 =", isKurangDari2)

# ---------11++++++++

isLebihDari2 = (inputUser > 11)
print("Lebih dari 11 =", isLebihDari2)

isCorrect1 = (isKurangDari1 or isLebihDari1)
print("angka yang anda masukkan(1): ", isCorrect1)

isCorrect2 = (isKurangDari2 or isLebihDari2)
print("angka yang anda masukkan(2): ", isCorrect2)

isCorrect = (isCorrect1 and isCorrect2)
print("angka yang anda masukkan: ", isCorrect)