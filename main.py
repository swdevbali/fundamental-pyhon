from modularization import hitung_segitiga, hitung_harga_diskon
from modularization import *

luas_segitiga = 10
print('MAIN', luas_segitiga)
exit(0)
print('Main', hitung_segitiga(10, 3))
print('Main', hitung_harga_diskon(1000000, .1))
"""
Ini komentar panjaang
"""
print("Hello world!")

# variables type
gedung = "BPK"
tinggi = 8
pi = 3.14
PI = "Private Investigation"
is_alive = True
is_alive = "HAI"
# tinggi = True # tipe variable bs berubah2
print(gedung)
print(tinggi)
print(pi)
print(PI, is_alive, pi)

#list
hari = []
hari = ['ahad', 'senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu']
print(hari)
print(hari[len(hari)-1])

#dictionary
antonim = {}
antonim['tinggi'] = "pendek"
antonim['gelap'] = 'terang'
antonim['jauh'] = 'dekat'
print('Antonim dari jauh adalah', antonim['jauh'])

#SEQUENTIAL FLOW

#CONTROL FLOW/IF
if is_alive == True:
    print('HIDUP!')
    print('yes!')
elif is_alive == False:
    print('MATI')
else:
    print('GA jelas')

if is_alive and tinggi > 7:
    print('HIDUP, tapi ketinggian, jadi mati')

#LOOP
# MENGULANGI KODE BEBERAPA KALI, SAMPAI KONDISI TERTNTU
# FOR untuk perulangan yang pasti
for i in range(0, 3):
    print(i)

#WHILE
#Digunakan untuk perulangan yang jumlahnya tidak pasti,
#namun kondisi berhentinya pasti
i = 0
while is_alive:
    print(i, 'hidup!')
    i = i + 1
    if i == 10:
        is_alive = False
#FOR UNTUK LIST
for h in hari:
    print(h)

#SAMA dengan di atas
for h in range(0, len(hari)-1):
    print(hari[h])
