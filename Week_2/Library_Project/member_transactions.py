import json
import os

MEM_FILE = "members.json"
BOOKS_FILE = "book.json"

def uye_guncelle():

    try:
        with open(MEM_FILE, "r", encoding="utf-8") as f:
            uyeler = json.load(f)
        
        id = int(input("ID numarası: "))
        for uye in uyeler:
            if uye["id"] == id:
                print(f"""
-------------Güncellenecek Üye--------------                      
(1)- Uye ID                : {uye["id"]}
(2)- Ad                    : {uye["uyeadi"]}
(3)- Telefon               : {uye["tel"]}
(4)- Adres                 : {uye["adres"]}
(0)- ÇIKIŞ 
--------------------------------------------

""")    
                secim= input("Seçiminizi Girin (0-4): ")
                while True:
                    if secim == "1":
                        degis=int(input("Yeni ID/'yi giriniz: "))
                        uye["id"]=degis
                        with open(MEM_FILE, "w", encoding="utf-8") as f:
                            json.dump(uyeler, f, ensure_ascii=False, indent=4)
                        print("ID başarıyla değiştirildi.")
                        return
                    elif secim == "2":
                        degis=input("Yeni adı giriniz: ")
                        uye["uyeadi"]=degis
                        with open(MEM_FILE, "w", encoding="utf-8") as f:
                            json.dump(uyeler, f, ensure_ascii=False, indent=4)
                        print("Ad başarıyla değiştirildi.")
                        return
                    elif secim == "3":
                        degis=input("Yeni telefon numarasını giriniz: ")
                        uye["tel"]=degis
                        with open(MEM_FILE, "w", encoding="utf-8") as f:
                            json.dump(uyeler, f, ensure_ascii=False, indent=4)
                        print("Telefon numarası başarıyla değiştirildi.")
                        return
                    elif secim == "4":
                        degis=input("Yeni adresi giriniz: ")
                        uye["adres"]=degis
                        with open(MEM_FILE, "w", encoding="utf-8") as f:
                            json.dump(uyeler, f, ensure_ascii=False, indent=4)
                        print("Adres başarıyla değiştirildi.")
                        return
                    elif secim == "0":
                        return
                    else:
                        secim=input("Hatalı giriş, Lütfen seçiminizi girin (0-4): ")
            
    
    except Exception as e:
        print("Bir hata oluştu:", e)

def uye_ekle():

    try:
        with open(MEM_FILE, "r", encoding="utf-8") as f:
            uyeler = json.load(f)
        
        id = int(input("Eklemek için bir ID numarası giriniz: "))
        for uye in uyeler:
            if uye["id"] == id:
                print("Bu ID ile kayıtlı bir üye zaten var.")
                return

        uye_adi = input("Üye Adı: ")
        tel = input("Telefon Numarası: ")
        adres = input("Adres: ")

        yeni_uye = {
            "id": id,
            "uyeadi": uye_adi,
            "tel": tel,
            "adres": adres,
            "kitaplar": []
        }

        uyeler.append(yeni_uye)

        with open(MEM_FILE, "w", encoding="utf-8") as f:
            json.dump(uyeler, f, ensure_ascii=False, indent=4)

        print(f"Yeni üye başarıyla eklendi: {uye_adi}")
    
    except Exception as e:
        print("Bir hata oluştu:", e)

def uye_ara():
    try:
        with open(MEM_FILE, "r", encoding="utf-8") as f:
            uyeler = json.load(f)
        
        id = int(input("Üyenin ID numarası: "))
        for uye in uyeler:
            if uye["id"] == id:
                print(f"""
---------------Aradiginiz Üye---------------                      
- Uye ID                : {uye["id"]}
- Ad                    : {uye["uyeadi"]}
- Telefon               : {uye["tel"]}
- Adres                 : {uye["adres"]}
- Ödünç Aldığı Kitaplar : {uye["kitaplar"]}
--------------------------------------------
""")
        girdi=input("Ana menuye donmek icin enter'a basınız:")
    except Exception as e:
        print("Bir hata oluştu:", e)

def uye_sil():
    try:
        with open(MEM_FILE, "r", encoding="utf-8") as f:
            uyeler = json.load(f)
        
        id = int(input("Silmek istediğiniz üyenin ID numarası: "))
        for uye in uyeler:
            if uye["id"] == id:
                print(f"""
-----------Silmek İstediğiniz Üye-----------                      
- Uye ID                : {uye["id"]}
- Ad                    : {uye["uyeadi"]}
- Telefon               : {uye["tel"]}
- Adres                 : {uye["adres"]}
- Ödünç Aldığı Kitaplar : {uye["kitaplar"]}
--------------------------------------------
""")
                girdi = input("Silmek istediğinizden emin misiniz? (Y/N): ").lower()
                while True:
                    if girdi == "y":
                        uyeler.remove(uye)
                        with open(MEM_FILE, "w", encoding="utf-8") as f:
                            json.dump(uyeler, f, ensure_ascii=False, indent=4)
                        print("Üye başarıyla silindi.")
                        return
                    elif girdi == "n":
                        return
                    else:
                        girdi = input("Geçersiz giriş yaptınız. Lütfen tekrar deneyiniz. (Y/N): ").lower()
        
        print("Bu ID numarasına sahip bir üye bulunamadı.")
        return uye_sil()
    
    except Exception as e:
        print("Bir hata oluştu:", e)

def kitap_odunc_verme():
    try:
        with open(MEM_FILE, "r", encoding="utf-8") as f:
            uyeler = json.load(f)
        with open(BOOKS_FILE, "r", encoding="utf-8") as f:
            kitaplar = json.load(f)
        
        id = int(input("ID numarası: "))
        for uye in uyeler:
            if uye["id"] == id:
                print(f"""
---------------Üye Bilgileri----------------                      
- Uye ID                : {uye["id"]}
- Ad                    : {uye["uyeadi"]}
- Telefon               : {uye["tel"]}
- Adres                 : {uye["adres"]}
- Ödünç Aldığı Kitaplar : {uye["kitaplar"]}
--------------------------------------------
""")

        barkod = int(input("Barkod numarası: "))
        for kitap in kitaplar:
            if kitap["Barkod"] == barkod:
                print(f"""
------------Ödünç Alınacak Kitap------------                      
- Barkod    : {kitap["Barkod"]}
- Kitap Adı : {kitap["Kitap_Adi"]}
- Dil       : {kitap["Dil"]}
- Fiyat     : {kitap["Fiyat"]}
- Yayınevi  : {kitap["Yayinevi"]}
- Yazar     : {kitap["Yazar"]}
--------------------------------------------
""")
        

    except Exception as e:
        print("Bir hata oluştu:", e)

if __name__ == "__main__":
    print("işlem")
