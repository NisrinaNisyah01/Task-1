# membuat set baru
set_saya = {1,2,3}
print(set_saya)

# bila kita hilangkan tanda # dari baris 9 akan muncul error TypeError
#set_saya[0]

# menambah satu anggota
# output: {1,2,3,4}
set_saya.add(4)
print_(set_saya)

# menambah beberapa anggota
# set akan menghilangkan duplikasi
# output: {1,2,3,4,5,6}
set_saya.update([3,4,5,6])
print(set_saya)