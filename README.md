# Python-Arduino-Serial-Control
# Python ile Arduino LED Kontrolü (Seri Haberleşme Protokolü)

Bu proje, bilgisayar (Python) ile mikrodenetleyici (Arduino Uno) arasında **Seri Haberleşme (Serial Communication)** protokolünü kullanarak donanım kontrolü gerçekleştirmek amacıyla geliştirilmiştir. 

Projede, Python üzerinden kullanıcının girdiği komutlar (klavye girdileri) bayt formatına dönüştürülerek USB portu üzerinden Arduino'ya iletilmekte ve Arduino tarafında çalışan karar mekanizması ile bir LED entegrasyonu kontrol edilmektedir.

## 🛠️ Kullanılan Teknolojiler ve Donanımlar
* **Mikrodenetleyici:** Arduino Uno
* **Programlama Dilleri:** Python 3.x, C++ (Arduino Sketch)
* **Kütüphaneler:** `pySerial`, `time`
* **Donanım Bileşenleri:** 1x LED, 1x 220 Ohm Direnç, Jumper Kablolar, Breadboard

## 💻 Kod Yapısı ve Mantığı

### 1. Arduino (C++) Tarafı
Arduino, bilgisayardan gelen verileri `9600 baud rate` hızında sürekli dinler (`Serial.available()`). Gelen veriyi `char` tipindeki bir değişkene atayarak kontrol eder:
* Kullanıcıdan `'a'` karakteri gelirse, dijital pin `HIGH` konumuna getirilerek LED yakılır.
* Kullanıcıdan `'b'` karakteri gelirse, dijital pin `LOW` konumuna getirilerek LED söndürülür.

### 2. Python Tarafı
Python tarafında `serial.Serial` nesnesi ile ilgili COM portu kilitlenir. `while True` sonsuz döngüsü ile kullanıcıdan `input()` alınır. Alınan string verisi `b'a'` veya `b'b'` şeklinde **byte** formatında porta yazılır (`write()`).

## ⚠️ Karşılaşılan Zorluklar ve Çözümleri (Mühendislik Notları)
* **Port Kilitlenmesi (SerialException / Permission Error):** Python kodu kapatılmadan portun serbest kalmadığı ve Arduino'ya yeni kod yüklenirken *Erişim Engellendi* hatası alındığı gözlemlenmiştir. Bu problem, Python tarafında `arduino.close()` fonksiyonunun doğru konumlandırılması ve Spyder konsolunun tamamen sıfırlanması ile çözülmüştür.
* **Zamanlama Senkronizasyonu (Reset Problemi):** Arduino portu açıldığında kartın otomatik reset atması nedeniyle Python'a `time.sleep(3)` eklenerek donanımın ayağa kalkması için gerekli süre tanınmıştır.
