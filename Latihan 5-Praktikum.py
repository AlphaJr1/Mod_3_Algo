#Adrian Alfajri - 064002200009

print('Mari kita cek apa jenis segitiga mu')

x = float(input('Masukkan panjang sisi tegak segitiga :'))
y = float(input('Masukkan panjang sisi bawah segitiga :'))
z = float(input('Masukkan panjang sisi miring segitiga :'))

if x == z or z == x :
    print('Segitiga kamu adalah segitiga sama kaki')
elif z == (x**2 + y**2)**0.5 :
    print('Segitiga kamu adalah segitiga siku-siku')
else :
     print('Segitiga kamu adalah segitiga sembarang')
           