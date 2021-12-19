import sys                    # sistem modülü  
from PyQt5.QtCore import *    # Temel pencere kütüphaneleri
from PyQt5.QtWidgets import *  # görsel kütüphane 

def window():                                           # pencere oluşturma fonksiyonu
    app = QApplication(sys.argv)                        # ana uygulamayı oluştur
    w = QMainWindow()                                   # pencere oluştur
    
    groupBox = QGroupBox(w)                             # groupBox oluştur
    groupBox.setGeometry(10,10,200,130)                 # konum ve boyutu ayarla
    groupBox.setTitle("Eğitim İşlemleri")               # groupBox başlığı
    button1 = QPushButton("Eğitim Verisi Yükle")        # 3 adet buton
    button2 = QPushButton("Eğitim Parametreleri")       
    button3 = QPushButton("Sistem Eğitimi")
    
    vbox = QVBoxLayout()                                # dikey kutu dizilimi
    vbox.addWidget(button1)                             # butonları dikey olarak ekle
    vbox.addWidget(button2)
    vbox.addWidget(button3)                             # groupBox dizilimini ayarla
    vbox.addStretch(1)                                  # butonları yayarak yerleştir
    groupBox.setLayout(vbox)

    groupBox2 = QGroupBox(w)                            # groupBox oluştur
    groupBox2.setGeometry(10,150,200,160)               # konum ve boyutu ayarla
    groupBox2.setTitle("Tahmin İşlemleri")              # groupBox başlığı
    button21 = QPushButton("1.Takım Verisi Yükle")      # 4 adet buton
    button22 = QPushButton("2.Takım Verisi Yükle")
    button23 = QPushButton("Tahmin Çalıştır")
    button24 = QPushButton("Tahmin Sonucu")
    
    vbox2 = QVBoxLayout()                               # dikey kutu dizilimi
    vbox2.addWidget(button21)                           # butonları dikey olarak ekle    
    vbox2.addWidget(button22)
    vbox2.addWidget(button23)   
    vbox2.addWidget(button24)    
    vbox2.addStretch(1)                                 # butonları yayarak yerleştir.
    groupBox2.setLayout(vbox2)                          # groupBox dizilimini ayarla
    
    groupBox3=QGroupBox(w)                              # groupBox oluştur.
    groupBox3.setGeometry(10, 320, 200, 90)             # konum ve boyutu ayarla
    groupBox3.setTitle("Seçenekler")                    # groupBox başlığı
    button31 = QPushButton("İstatistikler")             # 2 adet buton
    button32 = QPushButton("Genel Ayarlar")
    
    vbox3    = QVBoxLayout()                            # dikey kutu dizilimi
    vbox3.addWidget(button31)                           # butonları dikey olarak ekle
    vbox3.addWidget(button32)
    vbox3.addStretch(1)                                 # butonları yayarak yerleştir.
    groupBox3.setLayout(vbox3)                          # groupBox dizilimini ayarla
    
    w.setGeometry(100,100,800,500)                      # pencere konumu
    w.setWindowTitle("Futbol Tahmin Uygulaması")        # pencere başlığı
    w.show()                                            # pencereyi göster
    sys.exit(app.exec_())                               # uygulamayı çalıştır
   
if __name__ == '__main__':                              # bu kod direk çalıştırılırsa
   window()                                             # pencere fonk. çağır