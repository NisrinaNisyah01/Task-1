dict_saya = {'nama' : 'Budi', 'usia':27}

# output: Budi
print(dict_saya['nama'])

# output 27
print(dict_saya.get('usia'))

# output None
print(dict_saya.get('alamat'))

# Mengakses kunci yang tidak tersedia menyebabkan KeyError
#dict_saya['alamat]