# Haftalık Ders Notları
---
## 5. Hafta

### Yığın (Stack)

* Yığın, son giren ilk çıkar (last in first out - LIFO) mantığına göre çalışan veri yapısıdır.
* En çok kullanılan, çok önemli ve en basit veri yapısıdır.
* Aslında yığın, LIFO özellikleri sunan bir dizidir. Şöyleki:
    * diziye eleman eklerken en sona eklenir (push)
    * diziden elaman çıkarılırken en son eklenen eleman (top) çıkarılır (pull, pop)
    * yığında en son eklenen elemanın indisini tutmak için top indisi kullanılabilir.
        * top indisi 0 ise yığın boştur
        * top indisi maksimum kapasite ise yığın doludur
* Example 6.1 ve 6.2 : yığın kullanım örnekleri.
* **Abstract Data Type (ADT) of Stack**
    * **S.push(e)**: Add element e to the top of stack S.
    * **S.pop()**: Remove and return the top element from the stack S; an error occurs if the stack is empty. Additionally, let us deﬁne the following accessor methods for convenience:
    * **S.top()**: Return a reference to the top element of stack S, without removing it; an error occurs if the stack is empty.
    * **S.is empty()**: Return True if stack S does not contain any elements.
    * **len(S)**: Return the number of elements in stack S; in Python, we implement this with the special method len .
    * Example 6.3 : örnek bir yığın uygulaması

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
    * public
      * class içerinde doğrudan kullanılırlar, class dışından ve içerisinden erişilebilirler.
      * kodlama stili olarak başına _ eklenebilir. (zorunlu değildir ancak method isimleri ile karışmasınlar diye boyle bir kodlama stili geliştirilebilir).
    * private
      * class dışından erişilemeyen, sadece class içerisindeki metodlar tarafından erişilebilen değişkenlerdir.
      * bir değişkeninin başına çift alt çizgi (__, double underscore) eklendiğinden o değişken private olur.
      * bu değişkenlere erişim için **getter** ve **setter** methodlar tanımlanabilir.
  * Nesnenin davranışını ifade eden fonksiyonlar (method)
    * Nesne oluşturulurken otomatik çağrılan metod, constructor, : **\__init(self)__**
    * Nesne bellekten silinirken otomatik çağrılan fonksiyon, : **\__del(self)__**
    * sıradan methodlar
    * Tüm methodlar ilk parametre olarak nesnenin kendisini alırlar (self)
* ---
* Bir sınıfı tanımlarken <code>class ClassName</code> şeklinde bir tanım kullanılır.
* \__init__(): constructor

```python
class ClassName:
  def __init__(self):   # constructor
    ....

  def func1(self):      # parametresiz method
    .... 
  
  def func2(self,a,b):  # 2 parametreli method
    .... 
  
  def __del__(self):    # destructor
    ....

  self._var1  = ...     # public variables
  self.var2   = ...
  var3        = ...

  self.__var4 = ...     # private variables
  __var5      = ... 
```

* Örn; ch02/CreditCard.py
