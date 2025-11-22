# 🕵️ USB Exfiltrator v2.0 (Persistent & Auto-Zip)

![Python](https://img.shields.io/badge/Language-Python_3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

> **YASAL UYARI / DISCLAIMER:** > Bu yazılım **tamamen eğitim ve adli bilişim (forensics) öğrenimi** amacıyla geliştirilmiştir. İzinsiz olarak başkalarının cihazlarında veri toplamak için kullanılması yasadışıdır. Geliştirici (egnake), bu aracın kötüye kullanımından sorumlu tutulamaz.

## 📖 Proje Hakkında

**USB Exfiltrator**, Python kullanılarak geliştirilmiş, sistem arka planında çalışan gelişmiş bir otomasyon aracıdır. Sisteme bağlanan harici depolama birimlerini (USB Bellek, SD Kart vb.) algılar ve belirlenen dosya formatlarını otomatik olarak analiz edip güvenli bir şekilde yedekler.

Bu proje; **Sistem Programlama**, **Dosya Sistemi Manipülasyonu** ve **Kalıcılık (Persistence)** tekniklerini göstermek amacıyla oluşturulmuştur.

## 🚀 Özellikler

* **Otomatik USB Algılama:** `Watchdog` benzeri bir yapı ile sisteme yeni bir sürücü eklendiği anda tetiklenir.
* **Filtreli Veri Çekme:** Sadece belirlenen kritik uzantıları (PDF, DOCX, JPG, vb.) hedefler. Gereksiz dosyalarla zaman kaybetmez.
* **Otomatik Sıkıştırma (Auto-Zip):** Toplanan verileri dağınık bırakmaz; anlık olarak `.zip` formatında paketler.
* **Kalıcılık (Persistence):** Script ilk çalıştırıldığında kendini Windows Başlangıç (Startup) klasörüne kopyalar. Bilgisayar yeniden başlatılsa bile çalışmaya devam eder.
* **İz Temizleme:** Geçici kopyalama klasörlerini işlem bitince otomatik olarak siler.

## 🛠️ Kurulum ve Kullanım

Bu proje herhangi bir harici kütüphane (pip install) gerektirmez. Python'un standart kütüphaneleri (`os`, `shutil`, `time`, `sys`) ile çalışır.

1.  Repoyu klonlayın veya indirin:
    ```bash
    git clone [https://github.com/egnake/usb-exfiltrator.git](https://github.com/egnake/usb-exfiltrator.git)
    cd usb_spoofer
    ```

2.  Scripti çalıştırın:
    ```bash
    python usb_ajan.py
    ```
    *(Arka planda tamamen gizli çalışması için dosya uzantısını `.pyw` olarak değiştirebilirsiniz.)*

## ⚙️ Konfigürasyon

`usb_ajan.py` dosyası içerisindeki şu değişkenleri ihtiyacınıza göre düzenleyebilirsiniz:

          ```python
          # Hedef dosya türleri
          HEDEF_UZANTILAR = [".jpg", ".jpeg", ".png", ".pdf", ".docx", ".txt", ".xlsx"]

          # Verilerin kaydedileceği ana dizin
          ANA_KLASOR = os.path.join(os.path.expanduser("~"), "Desktop", "Toplanan_Veriler")
## 🧠 Çalışma Mantığı (Algoritma)

Başlangıç: Program çalışır çalışmaz APPDATA içerisindeki Startup klasörüne kendini kopyalar.

    ```python


       İzleme: Sonsuz döngüde (while True) sistemdeki sürücü harflerini (E:/, F:/ vb.) tarar.

       Tespit: Mevcut sürücü listesinde bir değişiklik (Fark kümesi) olduğunda tetiklenir.

       Aksiyon: * USB içeriğini tarar (os.walk).

       Hedef uzantıları geçici bir klasöre kopyalar.

       Klasörü shutil ile ZIP haline getirir.

       Geçici dosyaları siler.

##  🗺️ Yol Haritası (To-Do)
     ```python
        [x] Temel USB algılama

        [x] Dosya filtreleme

        [x] Kalıcılık (Persistence) ekleme

        [x] Verileri ZIP ile paketleme

        [ ] Discord Webhook ile anlık bildirim gönderme

        [ ] Verileri AES-256 ile şifreleme

        [ ] FTP sunucusuna otomatik upload

##👤 İletişim
```python
Geliştirici: egnake GitHub: github.com/egnake

Eğitim amaçlı kodlanmıştır.
