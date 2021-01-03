# Haftalık Ders Notları
---
## 14. Hafta

### Tree (Ağaç) Uygulamaları

* **ağaçtan düğüm silme**
  * 12 nin silinmesi (yaprak düğüm ise direk sil)
  * 30 un silinmesi (sağ ya da sol kol boş ise düğüm silinir, dolu kol yerine gelir)
  * 36 nın silinmesi (ara düğüm silinecekse)
    * __Yöntem 1__: sol koldaki en büyük düğüm ya da sağ koldaki en küçük düğüm
    * __Yöntem 2__: sağ veya sol kol dengeli olsun diye derinlik (veya eleman sayısı) fazla olan koldaki düğüm silinen düğüm yerine getirilir
* **Ağaç Üzerinde Gezinme**
    * BFS - Breadth First Search, enine arama
    * DFS - Depth First Search, derinine arama
* Euler Tour
    * Ağacın etrafında dolaşmak, ağacı dıştan dolaşmak
        * kök düğümü ilk ziyaret et, pre-visit
        * sol düğüm için euler tour
        * sağ düğüm için euler tour
        * kök düğümü son ziyaret et, post-visit
* Örnek Uygulama (Ödev 4)
    * Ağaç üzerine eleman ekleme (kodu derste yazıldı)
    * Ağaç üzerinde gezinme
        * DFS, BFS
        * inorder, preorder, postorder (derste kodu yazıldı)
        * Euler tour
    * Ağacın ekrana yazılması, (linux tree command) veya görsel grafik (sf. 347)
* Örnek Uygulama (Ödev 5)
    * Ağaçtan düğüm silen program (Yöntem 1 ve 2'nin ikisi de kodlanacak)
* Örnek Uygulama (Ödev 6)
    * Ağacın ekrana yazılması, (linux tree command) veya görsel grafik (sf. 347)

### Priority Queue (Öncelikli Kuyruk)

* (key,value) şeklinde ikililer şeklinde tutuluyor
* key değeri öncelik değerini gösteriyor ve kuyruğun key değerine göre sıralı olması sağlanır.

### Heap (Öbek)
