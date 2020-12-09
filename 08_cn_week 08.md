# Haftalık Ders Notları
---
## 8. Hafta

### Listeler (Lists)

* Ardışıl olarak birbirine bağlanan nesnelerden oluşan veri yapısıdır.
* Farklı türleri vardır:
  * Singly Linked List, Tek Bağlı Liste
  * Circularly Linked List, Dairesel Bağlı Liste
  * Double Linked List, Çift Yönlü Bağlı Liste
  * Circularly Double Linked List, Dairesel Çift Yönlü Bağlı Liste
* Araya eleman ekleme, silme, listeyi sıralı bir şekilde tutmak için işlerde çok kullanışlıdır.
* Gerçek Hayattan örnekler:
  * değerlerin sıralı liste şeklinde tutulması gereken tüm problemler. (Aslında bilgisayar diye icat edilen ve görevi bilgi saymak olan makinelerin icat edilmesinin nedeni verileri sıralı turmaktır)
  * web tarayıcı geçmişinin tutulması
  * dosyaların sektörler şeklinde disk üzerinde yazılması
  * blok zinciri (BitCoin sanal paranın temelinde olan teknoloji) benzeri uygulamalar (blok zinciri özel tasarlanmış bazı kısıtlamaları olan bir bağlı listedir)

**Singly Linked List (Tek Yönlü Bağlı Liste)**
* [Görsel olarak inceleyelim.](https://miro.medium.com/max/970/1*f2oDQ0cdY54olxCFOIMIdQ.png)
* Listede her eleman **Node** olarak isimlendirilir.
* Her Node element (value) ve pointer içermektedir.
  * **element (value)**, düğümdeki elemanın değerini, 
  * **pointer** ise bir sonraki düğümü gösteren pointer olarak isimlendirilir.
* Listede ilk eleman head, son eleman tail olarak isimlendirilir.
* Listede baştan sonraya kadar tüm düğümleri ziyaret etmek **gezinme (traversing)** olarak isimlendirilir.
* Listenin eleman sayısı listenin **size** değeri olarak adlandırılır.
* Tek yönlü bağlı listede 2 türlü işlem yapılabilir
  * Yeni bir düğüm ekleme
    * En başa, araya, sona
  * Mevcut bir düğümü silme
    * Düğüm En başta ise
    * Düğüm ortada ise
    * Düğüm en sonda ise