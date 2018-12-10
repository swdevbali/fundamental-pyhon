tinggi = 10
alas = 5
#SATU SEGITIGA
luas_segitiga = alas * tinggi / 2
print(luas_segitiga)

#SEGITIGA KEDUA
tinggi2 = 7
alas2 = 8
luas_segitiga_2 = alas2 * tinggi2 / 2
print(luas_segitiga_2)

def hitung_segitiga(alas, tinggi):
    return alas * tinggi / 2

segitiga1 = hitung_segitiga(10, 5)
segitiga2 = hitung_segitiga(7, 8)

print(segitiga1, segitiga2)
#TUGAS: FUNGSI PENGHITUNG DISKON.
#Parameter: total harga dan nilai diskon.
#Hasil fungsi: mengembalikan harga yang sudah didiskon
#Cetak hasilnya.

#discount in 0.x
def hitung_harga_diskon(price, discount):
    return price - (price * discount)

result = hitung_harga_diskon(100000, 0.3)
print('Hasilnya adalah', result)