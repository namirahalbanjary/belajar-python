'''Type hints untuk fungsi'''

# bentuk standar fungsi yang udah kita pelajari

'''srudi kasus
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)


fungsi(1)fungsi("Musashi")
fungsi(True)
'''

# penggunaan type hints

import string


def sepuluh_pangkat(argument:int) -> int:
    '''Fungsi dengan Hints'''
    output = 10**argument
    return output

HASIL = sepuluh_pangkat(2)
print(HASIL)

def display(argument:string):
    print(argument)

display("Musashi")