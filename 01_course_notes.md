# Haftalık Ders Notları
---
## 1. Hafta
### Veri Yapılarına Giriş
Bilgisayar = Bilgi + Sayar
Bu ders bilginin (temel yapıtaşı veri) organizasyonu ile ilgilenmektedir. Ayrıca bu ders kapsamında algoritma ve programlama kısmına da değinilmektedir.

**Veri**: bellekte yer kaplayan her türlü nesne

* basit: içerisinde tek bir veri barındırır
  * int, char, float
* karmaşık (çoklu):içerisinde birden fazla veri barındırır
  * lineer: bellekte ard arda, tüm veriler aynı türden
    * array, string
  * non-lineer: bellekte ard arda bulunmayan ve birden fazla veri barındıran yapılar
    * struct, class
    * veri yapısı (bu ders kapsamında görülen konular)
      * stack, queue, dequeue
      * list, linked-list
      * tree
      * graph
      * map (dictionary): key:value
      * hash tables

**Veri Yapısı Neden Önemlidir?**

Sıradan kod yazan kişiler ile iyi bir bilgisayar (yazılım) mühendisi arasındaki fark, veri yapılarının kullanmasıyla anlaşlaşılır. 

Her yazılım içeren sistem temelde 
* giriş olarak veri alır
* bu veriyi işler
* işlenen veri çıkış olarak verilir

Bu sürecin verimli olması için işlenen verinin iyi organize edilmesi gerekir. Bu da veri yapılarını bilmek ve uygulamakla mümkün olur. Verinin iyi organize edilmesi, verinin giriş olarak alınması, işlenmesi ve çıkış olarak verilmesi süreçlerini verimli hale getirir.

*Örnek*: 00_gpa.py python kodunu ve veri yapısı kullanarak yazılan versiyonunu inceleyiniz.

---

### Python Programlamaya Giriş
1. Python ekosisteminin kurulumu (Python3), anaconda, spyder, repl.it, colab
1. *.py uzantılı betik dosyalar, interaktif python
1. Ekrana bir şeyler yazılması, print()
1. Temel kurallar
1. Objects in Python
   * değişkenler, sabitler, atama işlemleri, 
     * dinamik tipli değişkenler, 
     * değişken isimleri referans (adres)
   * int, bool, str (char veri tipi yok, 1 boyutlu str var)
   * list, tuple
   * set, frozenset
   * dict (key:value organization) (*örn.*:gpa kaynak kodu)
1. operatörler
   * aritmetik: +, -, *, /, %, 
     * // : tam sayı bölme, 
     * ** : üs alma
   * karşılaştırma: 
     * <, >, <=, >=
   * eşitlik:
     * ==, !=, : içerik karşılaştırır
     * is, is not : objenin aynı obje olup olmadığını karşılaştırır
   * logical:
     * and, or, not
   * Sequence operators
      * s[j] element at index j
      * s[start:stop] slice including indices [start,stop)
      * s[start:stop:step] slice including indices start, start + step, start + 2 step, . . . , up to but not equalling or stop
      * s + t : concatenation of sequences 
      * k * s : shorthand for s + s + s + ... (k times)
      * val in s      : containment check
      * val not in s  : non-containment check

