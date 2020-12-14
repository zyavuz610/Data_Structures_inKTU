# Haftalık Ders Notları
---
## 9 ve 10. Hafta

### Listelerle ilgili örnek uygulama


### Listeyi Yığın ve Kuyruk olarak kullanmak

yığın, LIFO
- liste sonuna eleman ekle
- liste sonundan eleman çıkar


kuyruk, FIFO
- liste sonuna elaman ekle
- liste başından elaman çıkar

---

### Ödev 3

Ödevde iki polinom toplamı gerçeklenecek,
p1 = w1_0*x^0 + w_23*x^23 + w_46*x^46 + w_1001*x^1001

p2 = W2_0*x^0 + w_55*x^55 + w_1002*x^1002

p1+p2 = (w1_0+w2_0)*x^0 + w_23*x^23 + w_46*x^46 + w_55*x^55 + w_1001*x^1001 + w_1002*x^1002
     
p1=[w1_0,0,0,0, ..... w_23, 0, 0,.... w_46,0,0,.....,w_1001]
p2=.....

bu listelerin içerisinde boşuna çok fazla 0 değeri var

o halde polinomları liste veri yapısında tutalım.

h1-->(w1_0,0)-->(w_23,23)-->(w_46,46)-->(w_1001,1001)-->0
h2-->(w2_0,0)-->(w_55,55)-->(w_1002,1002)-->
h1+h2
