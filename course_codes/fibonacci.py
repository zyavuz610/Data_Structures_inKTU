def fibonacci(sinir):
    sayi1 = 0
    sayi2 = 1
    print(sayi1)
    print(sayi2)
    for _ in range(sinir-2):
        sayi3 = sayi1 + sayi2
        print(sayi3)
        sayi1 = sayi2
        sayi2 = sayi3


sinir = int(input("Lütfen sınır degerini giriniz:"))
if(sinir > 0):
    fibonacci(sinir)
else:
    sinir = int(input("Sınır değeri pozitif olmalı!:"))
    fibonacci(sinir)