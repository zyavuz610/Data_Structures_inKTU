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
* Yığın veri yapısının OOP ile kodlanması
    * array_stack.py
* **Örnek Projeler**
    * String ters çevirme
    * decimal2binary
    * reverse file
    * match paratheses
    * match html

---

### Kuyruk (Queue)

* İlk giren ilk çıkar (first in first out - FIFO) mantığına göre çalışan veri yapısıdır.
* Aslında kuyruk, FIFO özellikleri sunan bir dizidir. Şöyleki:
    * diziye eleman eklerken en sona eklenir (push)
    * diziden elaman çıkarılırken ilk eklenen eleman (front) çıkarılır (pull, pop)
    * kuyrukta ilk eklenen elemanın indisini tutmak için front, en son eklenen elemanın indisini tutmak için rear indisi kullanılabilir.
        * front==rear ise kuyruk boştur
        * rear indisi maksimum kapasite ise kuyruk doludur


### Çift-Sonlu Kuyruk (De-Queue)

* Hem baştan, hem de sondan eleman eklenebilen veya çıkarılabilen bir kuyruk veriyapısı çeşididir.

---

**Not:** Daha ayrıntılı konu içerikleri için ders kitabındaki "Bölüm 6"'yı inceleyiniz.