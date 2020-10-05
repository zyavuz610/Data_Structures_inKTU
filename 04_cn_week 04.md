# Haftalık Ders Notları
---
## 4. Hafta

### Diziler (Sequences)

* Diziler birden çok aynı türden elemanları bir arada tutan en basit veri yapısıdır.
* Dizi elemanlarını indexlemek için [] operatörü kullanılmaktadır.
   * Sequence operators
      * s[j] element at index j
      * s[start:stop] slice including indices [start,stop)
      * s[start:stop:step] slice including indices start, start + step, start + 2 step, . . . , up to but not equalling or stop
      * s + t : concatenation of sequences 
      * k * s : shorthand for s + s + s + ... (k times)
      * val in s      : containment check
      * val not in s  : non-containment check
* Örn; ch05/list_expand.py

---

### Object-Oriented in Python
* Bu bölümde Nesne Yönelimli Programlama ile ilgili temel kavramlara değinilecektir. 
* Daha ayrıntılı bilgi "Nesne Yönelimli Programlama" dersinde C++ dili ile anlatılmaktadır. 
  * Python dili çok sıkı bir Nesne Yönelimli dil olmamasına rağmen bir çok temel özellikleri desteklemektedir.
  * C++ dili de böyledir.
  * Java dili daha sıkı bir Nesne Yönelimli Programlama dilidir.
* Nesne Yönelimli Programlamaya neden ihtiyaç duyulur?
  * Robustness: Yazılan kod hatalara karşı daha dayanıklıdır.
  * Adaptability: yazılan kod farklı projelere daha kolay adapte edilebilmektedir.
  * Reusability: Yazılan kodun yeniden kullanılabilirliği sağlanmaktadır.
* Nesne bellekte yer kaplayan ve tanımlı bir sınıfın sureti (örneğidir).
* class(sınıf) ise nesnenin (object) tanımıdır.
* Her nesnenin 2 önemli bileşeni vardır:
  * Durum bilgilerinin tutulduğu değişkenler (status, variable)
  * Nesnenin davranışını ifade eden fonksiyonlar (method)
* ---
* Bir sınıfı tanımlarken <code>class ClassName</code> şeklinde bir tanım kullanılır.
* Örn; ch02/CreditCard.py
