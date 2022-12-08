print("Pilihan model Matematika\n========================")
print('\n1. Perkalian')
print('2. Pembagian\n========================')

menu = int(input("Masukkan model matematika yang diinginkan (1/2) : "))
table = int(input('Menampilkan table matematika dari angka:'))

if menu == 1:
    for i in range(1,11):
        print(f'{table} x {i} = {table*i}')
elif menu == 2:
    for i in range(50,66):
        print(f'{i} : {table} = {i/table}')
else:
    print('Tidak tersedia')
