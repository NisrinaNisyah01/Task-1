# membuat dictionary baru
dict_saya = {1:1, 2:4, 3:9, 4:16, 5:25}

# menghapus anggota tertentu
# output: 9
print(dict_saya.pop(3))

# menghapus anggota secara acak
# output: (5, 25)
print(dict_saya.popitem())

# yang tersisa adalah {1:1, 2:4, 4:16}
print(dict_saya)

# delete 5
del dict_saya[2]

# output: {2:4, 4:16}
print(dict_saya)

# menghapus semua anggota
dict_saya.clear()

# menghapus dictionary dict_saya
del dict_saya

# Error karena dict_saya sudah dihapus
#print(dict_saya)