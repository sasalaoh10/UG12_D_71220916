
# # susu = 20.000
# permen = 500
# roti = 15000
# indomie = 3000
# vitamin = 50000


uang= int(input('Masukan jumlah uang:'))
iStart = input('Masukkan START: ')

susu = 20000
permen = 500
roti = 15000
indomie = 3000
vitamin = 50000

if start.UPPER() == 'START':
    while True:
        beli = input('beli? ')
        if beli.upper() =='SUSU':
            if Duid >= susu:
                Duid -= susu
                print('sisa',uangAwal)
            else:
                print('tdk cukup')
        elif beli.upper() =='ROTI':
            if Duid >= roti:
                Duid -= roti
                print('sisa',uangAwal)
            else:
                print('tdk cukup')
        elif beli.upper() =='PERMEN':
            if Duid >= permen:
                Duid -= permen
                print('sisa',uangAwal)
            else:
                print('tdk cukup')
        elif beli.upper() =='VITAMIN':
            if Duid >= vitamin:
                Duid -= vitamin
                print('sisa',uangAwal)
            else:
                print('tdk cukup')
        elif beli.upper() =='INDOMIE':
            if Duid >= indomie:
                Duid -= indomie
                print('sisa',uangAwal)
            else:
                print('tdk cukup')
        elif beli.lower() == 'sudah':
            break
        else:
            print('barang tdk ada')