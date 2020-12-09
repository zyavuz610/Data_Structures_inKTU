# Haftalık Ders Notları
---
## 6. Hafta

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