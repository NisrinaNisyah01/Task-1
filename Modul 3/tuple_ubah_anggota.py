tuple1 =  (2, 3, 4, [5, 6])
# kita tidak bisa mengubah anggota tuple
# bila kita hilangkan tanda komentar # pada baris ke 6
# akan muncul error: # TypeError: 'tuple' objects does not support item assigment

# tuple1[1] = 8

# tapi list di dalam tuple bisa diubah
# output: (2, 3, 4, [7, 6])
tuple[3][0] = 7
print(tuple1)

# tuple bisa diganti secara keseluruhan dengan penugasan kembali
# output: ('p','y',t','h','o','n')
tuple1 = ('p','y','t','h','o','n')
print(tuple1)

# anggota tuple juga tidak bisa dihapus menggunakan del
# perintah berikut akan menghasilkan error TypeError
# kalau Anda menghilangkan tanda komentar #

#del tuple1[0]
# kita bisa menghapus tuple keseluruhan
del tuple1