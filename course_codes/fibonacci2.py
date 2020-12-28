def fibonacci(sinir):
    if sinir < 2:
        return sinir
    else:
        return (fibonacci(sinir-1) + fibonacci(sinir-2))


sinir = int(input("Lütfen sınır degerini giriniz:"))
while sinir:
    if(sinir > 0):
        print("Fibonacci Dizisi:")
        for i in range(sinir):
            print(fibonacci(i))

        break
    else:
        sinir = int(input("Sınır değeri pozitif olmalı!:"))