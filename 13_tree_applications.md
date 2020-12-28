# Haftalık Ders Notları
---
## 13. Hafta

### Tree (Ağaç) Uygulamaları

* Ağacın düğümüne parent işaretçisi ekleme, DEBUG etme
* ağaç üzerinde gezinme - TEKRAR
  * inorder
  * preorder
  * postorder
* yeni bir ağaç oluştur, 25,36,20,10,5,22,40,48,38,30,22,12,28
  * ağaç üzerindeki bağlantıları incele
* derinlik ve eleman sayısı kavramı
* **ağaçtan düğüm silme**
  * 12 nin silinmesi (yaprak düğüm ise direk sil)
  * 30 un silinmesi (sağ ya da sol kol boş ise düğüm silinir, dolu kol yerine gelir)
  * 36 nın silinmesi (ara düğüm silinecekse)
    * __Yöntem 1__: sol koldaki en büyük düğüm ya da sağ koldaki en küçük düğüm
    * __Yöntem 2__: sağ veya sol kol dengeli olsun diye derinlik (veya eleman sayısı) fazla olan koldaki düğüm silinen düğüm yerine getirilir
* BFS - Breadth First Search, enine arama
* DFS - Depth First Search, derinine arama

