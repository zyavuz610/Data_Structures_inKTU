#İTERATİF
from time import time   #koşma süresini hesaplamak için sınıf oluşturuldu
start_time = time( )    #koşma süresinin başlangıcı 

def binary_search(list_,min,max, target_):  #Fonksiyon ve parametreler tanımlandı
    while min <= max:   #liste boş olmadığı sürece
    
        mid = (min + max)//2   #orta eleman hesaplandı
        
        if target_ == list_[mid]: #orta eleman, hedefe eşit ise
            print("\nAranan eleman:\n",target, "Elemaninin bulundugu indeks:",mid)
            return -1     
        elif target_ < list_[mid]:  #orta eleman, hedeften büyükse
            max = mid - 1     #sol taraftan devam etmek için mid bir azaltıldı
        elif target_ > list_[mid]:  #orta eleman, hedeften küçükse
            min = mid + 1   #sağ taraftan devam etmek için mid bir artırıldı 
    print("\nAranan sayi bulunamadi")
    return -1    
   
list = []  #boş liste oluşturuldu
len = int(input("Liste boyutunu giriniz: "))  
list = input('Liste elemanlarini giriniz: ')
list = list.split()  #yan yana girilen sayıları birbirinden ayıran metod
list = [int(x) for x in list]
list.sort() #listeyi küçükten büyüğe sıralayan metod
print('\nListe kucukten buyuge siralandi:', list)
 
target = int(input("\nAranan sayiyi giriniz: "))
binary_search(list,0, len-1, target) #fonksiyon çağrısı

end_time = time( ) #koşma süresi bitişi
elapsed = end_time - start_time #çalışma zamanı hesaplandı
print(elapsed)

#REKÜRSİF
from time import time   #koşma süresini hesaplamak için sınıf oluşturuldu
start_time = time( )    #koşma süresinin başlangıcı 

def binary_search(list, min, max, target):   #Fonksiyon ve parametreler tanımlandı
    if max >= min:  #Liste boş değilse
  
        mid = (max + min) // 2 #orta eleman hesaplandı
        
        if list[mid] == target:  #orta eleman, hedefe eşit ise
            print("Aranan eleman:\n",target, "Elemaninin bulundugu indeks: ",mid)
            return -1
        elif list[mid] > target: #orta eleman, hedeften büyükse
            return binary_search(list, min, mid - 1, target) #fonksiyon çağrılarak sol taraftan işlem yapılır
  
        elif list[mid]<target: #orta eleman, hedeften küçükse
            return binary_search(list, mid + 1, max, target)  #fonksiyon çağrılarak sağ taraftan işlem yapılır
    else: 
         print("Aranan eleman bulunamadi")
         return -1

list = []  #boş liste oluşturuldu
len = int(input("Liste boyutunu giriniz: "))  
list = input('Liste elemanlarini giriniz: ')
list = list.split()  #yan yana girilen sayıları birbirinden ayıran metod
list = [int(x) for x in list]
list.sort() #listeyi küçükten büyüğe sıralayan metod
print('\nListe kucukten buyuge siralandi:', list)
target = int(input("\nAradiginiz sayiyi giriniz: ")) 
binary_search(list, 0, len-1, target) #fonksiyon çağrısı 

end_time = time( ) #koşma süresi bitişi
elapsed = end_time - start_time #çalışma zamanı hesaplandı
print(elapsed)