import os
import shutil
from pathlib import Path

# --- AYARLAR ---
# Mevcut karışık dosyaların bulunduğu ana dizin (Görseldeki yapıya göre)
# Eğer veri_ayirici.py dosyası ana dizindeyse bu yol doğru çalışacaktır.
BASE_DIR = Path("dataset/kidney")
SOURCE_DIR = BASE_DIR / "images_txt_mask"

# Yeni oluşturulacak hedef klasörler
IMAGES_DIR = BASE_DIR / "images"
MASKS_DIR = BASE_DIR / "masks"
LABELS_DIR = BASE_DIR / "labels"

def dosyalari_ayir():
    # 1. Hedef klasörleri oluştur (eğer yoksalarsa)
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    MASKS_DIR.mkdir(parents=True, exist_ok=True)
    LABELS_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Kaynak klasör taranıyor: {SOURCE_DIR}")
    
    # Klasörün var olup olmadığını kontrol et
    if not SOURCE_DIR.exists():
        print("Hata: Kaynak klasör bulunamadı. Lütfen dosya yollarını kontrol edin.")
        return

    tasinan_resim = 0
    tasinan_maske = 0
    tasinan_txt = 0

    # 2. Kaynak klasördeki tüm dosyaları dön
    for filename in os.listdir(SOURCE_DIR):
        file_path = SOURCE_DIR / filename

        # Sadece dosyaları işle, alt klasör varsa atla
        if not file_path.is_file():
            continue

        # 3. Dosya isimlerine/uzantılarına göre ayırma işlemi
        if filename.endswith("_mask.png"):
            # Maske dosyalarını taşı
            shutil.move(str(file_path), str(MASKS_DIR / filename))
            tasinan_maske += 1
            
        elif filename.endswith(".txt"):
            # Text dosyalarını taşı
            shutil.move(str(file_path), str(LABELS_DIR / filename))
            tasinan_txt += 1
            
        elif filename.endswith(".jpg"):
            # Orijinal JPG resimlerini taşı
            shutil.move(str(file_path), str(IMAGES_DIR / filename))
            tasinan_resim += 1
            
        else:
            print(f"Atlandı (Bilinmeyen format): {filename}")

    # Sonuç raporu
    print("\n--- İşlem Tamamlandı ---")
    print(f"Taşınan Orijinal Resim (.jpg): {tasinan_resim}")
    print(f"Taşınan Maske Resim (_mask.png): {tasinan_maske}")
    print(f"Taşınan Text Dosyası (.txt): {tasinan_txt}")

if __name__ == "__main__":
    dosyalari_ayir()