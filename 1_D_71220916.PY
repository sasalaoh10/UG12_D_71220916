start = input("Ketik 'START' untuk memulai: ")

Susu = 20000
Permen = 500
Roti = 15000
indomie = 3000
Vitamin = 50000

Uang = int(input('Masukan Jumlah uang:'))
if start.upper() == 'START':
    while True:
        beli = input("Apa barang yang akan beli?")
        if beli.upper() =='SUSU':
            if Uang >= Susu:
                Uang -= Susu
                print('sisa',Uang)
            else:
                print('tdk cukup')
        elif beli.upper() =='PERMEN':
            if Uang >= Permen:
                Uang -= Permen
                print('sisa',Uang)
            else:
                print('tdk cukup')
        elif beli.lower() =='roti':
            if Uang >= Roti:
                Uang -= Roti
                print('sisa',Uang)
            else:
                print('tdk cukup')
        elif beli.upper() =='VITAMIN':
            if Uang >= Vitamin:
                Uang -= Vitamin
                print('sisa',Uang)
            else:
                print('tdk cukup')
        elif beli.lower() =='indomie':
            if Uang >= indomie:
                Uang -= indomie
                print('sisa',Uang)
            else:
                print('tdk cukup')
        elif beli.lower() == 'sudah':
            break
        else:
            print('barang tdk ada')