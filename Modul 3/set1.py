# set integer
set_saya = {1,2,3}
print(set_saya)

# set dengan menggunakan fungsi set()
set_saya = set([1,2,3])
print(set_saya)

# set data campuran
set_saya = {1, 2.0, "python", (3,4,5)}
print(set_saya)

# bila kita mengisi duplikasi, set akan menghilangkan salah satu
# output: {1,2,3}
set_saya = {1,2,2,3,3,3}
print(set_saya)

# set tidak bisa berisi anggota list
# contoh berikut akan muncul error TypeError
set_saya = {1,2,[3,4,5]}