
import json
import os

#JSON dosyasının adı
DOSYA_ADI = os.path.join(os.path.dirname(__file__), "books.json")

#JSON dosyasını oku
def dosya_oku():
    if not os.path.exists(DOSYA_ADI):
        print(" kitap.json bulunamadı, yeni dosya oluşturuluyor...")
        with open(DOSYA_ADI, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
        return []

    try:
        with open(DOSYA_ADI, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                print("JSON formatı beklenenden farklı. Boş listeyle başlatılıyor.")
                return []
    except json.JSONDecodeError:
        print("JSON dosyası okunamadı. Boş listeyle devam ediliyor.")
        return []

#JSON dosyasına yaz
def dosya_yaz(veri):
    with open(DOSYA_ADI, "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=4)

#Kitapları listele
def kitaplari_listele():
    kitaplar = dosya_oku()
    if not kitaplar:
        print(" Henüz kayıtlı kitap bulunmuyor.")
        return
    print(f"\n Toplam {len(kitaplar)} kitap listelendi:\n")
    for k in kitaplar:
        print(f"{k.get('Barkod')} | {k.get('Kitap_Adi')} | {k.get('Yazar')} | {k.get('Fiyat')}₺ | {k.get('Yayinevi')}")
    input("Press enter to continue")
#Kitap ekle
def kitap_ekle(barkod, ad, yazar, fiyat, yayinevi, dil="Türkçe"):
    kitaplar = dosya_oku()
    if any(str(k.get("Barkod")) == str(barkod) for k in kitaplar):
        print("Bu barkodla kayıtlı kitap zaten var!")
        return
    if not ad or not yazar or not yayinevi:
        print(" Eksik bilgi! Lütfen kitap adı, yazar ve yayınevi giriniz.")
        return

    yeni_kitap = {
        "Barkod": str(barkod),
        "Kitap_Adi": ad,
        "Yazar": yazar,
        "Fiyat": float(fiyat),
        "Yayinevi": yayinevi,
        "Dil": dil
    }
    kitaplar.append(yeni_kitap)
    dosya_yaz(kitaplar)
    print(f"'{ad}' adlı kitap başarıyla eklendi.")

#Kitap ara
def kitap_ara(aranan):
    kitaplar = dosya_oku()
    bulunanlar = [
        k for k in kitaplar
        if aranan.lower() in str(k.get('Kitap_Adi', '')).lower() or
           aranan.lower() in str(k.get('Yazar', '')).lower()
    ]
    if bulunanlar:
        print(f"\n {len(bulunanlar)} kitap bulundu:\n")
        for k in bulunanlar:
            print(f"{k.get('Barkod')} | {k.get('Kitap_Adi')} | {k.get('Yazar')} | {k.get('Fiyat')}₺ | {k.get('Yayinevi')}")
    else:
        print(" Aradığınız kriterlere uygun kitap bulunamadı.")

#Kitap sil
def kitap_sil(barkod):
    barkod = str(barkod)
    kitaplar = dosya_oku()
    yeni_liste = [k for k in kitaplar if str(k.get("Barkod")) != barkod]
    if len(kitaplar) == len(yeni_liste):
        print(" Bu barkodla kayıtlı bir kitap bulunamadı.")
    else:
        dosya_yaz(yeni_liste)
        print(f" Barkod {barkod} olan kitap başarıyla silindi.")

#Menü
def menu():
    while True:
        print("""
=======  KİTAP YÖNETİM SİSTEMİ =======
1 - Kitapları Listele
2 - Kitap Ara
3 - Kitap Ekle
4 - Kitap Sil
5 - Çıkış
========================================
""")
        secim = input("İşlem seçiniz (1-5): ").strip()
        if secim == "1":
            kitaplari_listele()
        elif secim == "2":
            aranan = input("Aranacak kelime (kitap adı veya yazar): ").strip()
            kitap_ara(aranan)
        elif secim == "3":
            try:
                barkod = input("Barkod: ").strip()
                ad = input("Kitap Adı: ").strip()
                yazar = input("Yazar: ").strip()
                fiyat = float(input("Fiyat: ").strip())
                yayinevi = input("Yayınevi: ").strip()
                dil = input("Dil (varsayılan Türkçe): ").strip() or "Türkçe"
                kitap_ekle(barkod, ad, yazar, fiyat, yayinevi, dil)
            except ValueError:
                print( "Geçersiz giriş! Barkod sayı, fiyat ondalıklı sayı olmalıdır.")
        elif secim == "4":
            barkod = input("Silinecek kitabın barkodu: ").strip()
            kitap_sil(barkod)
        elif secim == "5":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen 1-5 arasında bir değer giriniz.")

# Programı çalıştır
if __name__ == "__main__":
    menu()
