# latihan konversi satuan temperature.

# program konversi celcius ke satuan lain.

print ("\nPROGRAM KONVERSI TEMPERATURE\n")

celcius = float(input('Masukkan suhu dalam celcius :'))
print("suhu adalah",celcius, "Celcius")

#reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah",reamur, "Reamur")

#Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah",fahrenheit, "Fahrenheit")

#Kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah",kelvin, "Kelvin")


print("\nFAHRENHEIT KE KELVIN\n")

fahrenheit = float(input('Masukkan suhu dalam fahrenheit : '))
print("suhu adalah", fahrenheit, "Fahrenheit")

celcius = (fahrenheit - 32) * 5/9
print("suhu dalam celcius adalah",celcius, "Celcius")

kelvin = celcius + 273
print("suhu dalam kelvin adalah",kelvin, "Kelvin")


print("\nKELVIN KE FAHRENHEIT\n")

kelvin = float(input('Masukkan suhu dalam kelvin : '))
print("suhu adalah", kelvin, "Kelvin")

celcius = kelvin - 273
print("suhu dalam celcius adalah",celcius, "Celcius")

fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah",fahrenheit, "Fahrenheit")