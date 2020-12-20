# Haftalık Ders Notları
---
## 3. Hafta
### Algorithm Analysis
* Algoritma analizi neden gerekli?
  * Her algoritmanın farklı davranışları vardır. Algoritmaları birbirleri ile karşılaştırmak ve hangisinin daha iyi olduğuna karar vermek için algoritma analizi yapılmaktadır.
  * Yaygın olarak kullanılan 2 türlü analiz yöntemi vardır. 1) deneysel (zamansal) analiz, 2) karmaşıklık analizi. Karmaşıklık analizinin de en yaygın olanı büyük O notasyonudur.
  * n, problemin boyutu olarak alınır.

**Deneysel Analiz (zaman analizi):**
  * Algoritmanın koşma (çalışma) zamanına göre değerlendirilmesidir. t, çalışma zamanı olursa (n,t) olarak ifade edilir.
  * Bu analiz yönteminin bazı dezavantajları vardır.
    * Algoritmaları karşılaştırmak için her algoritmanın aynı donanım ve yazılım kombinasyonunda çalıştırılması gerekir.
    * Büyük boyutlar söz konusu olduğunda çalışma zamanı elde edilemeyebilir.
    * Çalışma zamanını değerlendirmek için algoritma tamamen kodlanmalıdır.
  * Aşağıdakine benzer bir Python kodu ile çalışma zamanı elde edilebilir.

<code>

from time import time

start time = time( )                # record the starting time

 run algorithm

end time = time( )                  # record the ending time

elapsed = end time − start time     # compute the elapsed time

</code>

**Karmaşıklık Analizi (algorithm complexty) - bigO**
* bigO (büyük O notasyonu olarak da isimlendirilir)
* O derece anlamında Order kelimesinin ilk harfidir.
* Algoritmanın problem boyutu n olarak düşünüldüğünde f(n) = O(c*g(n)) olarak ifade edilir.
    * f(n), problemin gerçek derecesini ifade eden fonksiyon,
    * c*g(n) ise f(n) fonksiyonunun asimptotik üst sınırını ifade eden fonksiyon.
* Örn; n² + 3n + 4 --> O(n²), çünkü n² + 3n + 4 < 2n² (n > 10 durumunda)

**Çok Kullanılan 7 Temel Fonksiyon**
1. sabit (constant) --> f(n) = c
1. logaritmik(logarithm) --> f(n) = log(n)
1. lineer --> f(n) = n
1. N-log-N --> f(n) = n*log(n)
1. quadratic --> n^2
1. cubic --> n^3
1. exponational --> a^n

* Algoritmik karmaşıklık sırası küçükten büyüğe şu şekildedir:
  * O(c) < O(log(n)) < O(n) < O(n*log(n)) < O(n^2) < O(n^3) < O(a^n)

### Öz Yinelemeli Fonksiyonlar (Recursion)
* Kendi kendini çağıran fonksiyonlara öz yinelemeli (recursive) fonksiyonlar denir. Mühendislik problemlerinin çözümlerini kolaylaştırdığı için oldukça yaygın olarak kullanılmaktadır. 
* Öz yineli fonksiyonlarda durma noktası çok önemlidir. Aksi durumda program durmadan sürekli çalışarak bilgisayar belleğini doldurarak çöker.
* Aşağıda örnek rekürsif fonk. problemlerine örnekler verilmektedir.
  * faktöryel,fibonacci, ruler, binary search, a^n, sum(1...n)
* recursion trace (özyineleme izi) yaparak rekürsif fonksiyonları verilen örnek değerlerle gösteriniz.
* Dallanma sayısına göre 3 türlü recursive fonksiyon vardır. 1) lineer recursion (kendini bir kere çağırarak problemin durma noktasına kadar lineer olarak ilerler), 2) binary recursion (kendini iki kez çağırarak 2 kollu bir ağaç şeklinde problemin durm noktalarına kadar ilerler, binary tree), 3) multiple recursion (kendini ikiden fazla kez çağırarak m kollu bir ağaç şeklinde problemin durm noktalarına kadar ilerler, multiway tree)
* Yineleme şekline göre 2 türlü recursive fonksiyon vardır. 1) doğrudan (direct recursion, A fonksiyonu sürekli kendini çağırır), 2) dolaylı (indirect recursion, A fonksiyonu B fonksiyonunu çağırır, B fonksiyonu da A'yı çağırır)
* [Daha fazlası için bkz.](https://www.geeksforgeeks.org/types-of-recursions/#:~:text=Thus%2C%20the%20two%20types%20of,the%20recursive%20function%20performs%20nothing.)
