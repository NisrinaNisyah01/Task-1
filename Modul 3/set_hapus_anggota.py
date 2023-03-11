# membuat set baru
set_saya = {1,2,3,4,5,}
print(set_saya)

# menghapus 4 dengan discard
# output: {1,2,3,5}
set_saya.discard(4)
print(set_saya)

# menghapus 5 dengan remove
# output : {1,2,3}
set_saya.remove(5)
print(set_saya)

# anggota yang mau dihapus tidak ada dalam set
# discard tidak akan memunculkan error
# output: {1, 2, 3}
set_saya.discard(6)