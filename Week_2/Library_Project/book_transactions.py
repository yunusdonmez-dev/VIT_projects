import json
import os

BOOKS_FILE = "book.json"

def kitap_ekle():

    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as f:
            kitaplar = json.load(f)

        barkod = int(input("Barkod numarası: ")) # Aynı barkodlu kitap var mı kontrol ettim
        for kitap in kitaplar:
            if kitap["Barkod"] == barkod:
                print("Bu barkodla kayıtlı bir kitap zaten var!")
                return

        dil = input("Dil: ")
        kitap_adi = input("Kitap Adı: ")
        yazar = input("Yazar: ")
        yayinevi = input("Yayınevi: ")
        fiyat = float(input("Fiyat: "))

        yeni_kitap = {
            "Barkod": barkod,
            "Dil": dil,
            "Fiyat": fiyat,
            "Kitap_Adi": kitap_adi,
            "Yayinevi": yayinevi, 
            "Yazar": yazar       
        }

        kitaplar.append(yeni_kitap)

        with open(BOOKS_FILE, "w", encoding="utf-8") as f:
            json.dump(kitaplar, f, ensure_ascii=False, indent=4)

        print(f"""
----------Kitap Başarıyla Eklendi-----------                      
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

def kitap_sil():
    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as f:
            kitaplar = json.load(f)
        
        barkod = int(input("Silmek istediğiniz kitabın barkod numarası: "))
        for kitap in kitaplar:
            if kitap["Barkod"] == barkod:
                print(f"""
---------Silmek İstediğiniz Kitap----------                      
    - Barkod    : {kitap["Barkod"]}
    - Kitap Adı : {kitap["Kitap_Adi"]}
    - Dil       : {kitap["Dil"]}
    - Fiyat     : {kitap["Fiyat"]}
    - Yayınevi  : {kitap["Yayinevi"]}
    - Yazar     : {kitap["Yazar"]}
--------------------------------------------
""")
                girdi = input("Silmek istediğinizden emin misiniz? (Y/N): ").lower()
                while True:
                    if girdi == "y":
                        kitaplar.remove(kitap)
                        with open(BOOKS_FILE, "w", encoding="utf-8") as f:
                            json.dump(kitaplar, f, ensure_ascii=False, indent=4)
                        print("Kitap başarıyla silindi.")
                        return
                    elif girdi == "n":
                        print("Ana Menüye Dönülüyor...")
                        return
                    else:
                        girdi = input("Geçersiz giriş yaptınız. Lütfen tekrar deneyiniz. (Y/N): ").lower()
        
        print("Bu barkoda sahip bir kitap bulunamadı. Lütfen geçerli bir barkod numarası giriniz.")
        return kitap_sil()
    
    except Exception as e:
        print("Bir hata oluştu:", e)

def kitap_ara():
    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as f:
            kitaplar = json.load(f)
        
        barkod = int(input("Aradığınız kitabın barkod numarası: "))
        for kitap in kitaplar:
            if kitap["Barkod"] == barkod:
                print(f"""
-------------Aradiginiz Kitap--------------                      
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

def kitap_guncelle():
    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as f:
            kitaplar = json.load(f)
        
        barkod = int(input("Güncellemek istediğiniz kitabın barkod numarasını giriniz: "))
        for kitap in kitaplar:
            if kitap["Barkod"] == barkod:
                print(f"""
------------Güncellenecek Kitap-------------                      
(1) - Barkod    : {kitap["Barkod"]}
(2) - Kitap Adı : {kitap["Kitap_Adi"]}
(3) - Dil       : {kitap["Dil"]}
(4) - Fiyat     : {kitap["Fiyat"]}
(5) - Yayınevi  : {kitap["Yayinevi"]}
(6) - Yazar     : {kitap["Yazar"]}
(0) - Çıkış     
--------------------------------------------
""")   
                secim= input("Seçiminizi Girin (0-6): ")
                while True:
                    if secim == "1":
                        degis=int(input("Yeni barkodu giriniz: "))
                        kitap["Barkod"]=degis
                        with open(BOOKS_FILE, "w", encoding="utf-8") as f:
                            json.dump(kitaplar, f, ensure_ascii=False, indent=4)
                        print("Barkod başarıyla değiştirildi.")
                        return
                    elif secim == "2":
                        degis=input("Yeni adı giriniz: ")
                        kitap["Kitap_Adi"]=degis
                        with open(BOOKS_FILE, "w", encoding="utf-8") as f:
                            json.dump(kitaplar, f, ensure_ascii=False, indent=4)
                        print("Ad başarıyla değiştirildi.")
                        return
                    elif secim == "3":
                        degis=input("Yeni dili giriniz: ")
                        kitap["Dil"]=degis
                        with open(BOOKS_FILE, "w", encoding="utf-8") as f:
                            json.dump(kitaplar, f, ensure_ascii=False, indent=4)
                        print("Dil başarıyla değiştirildi.")
                        return
                    elif secim == "4":
                        degis=float(input("Yeni fiyatı giriniz: "))
                        kitap["Fiyat"]=degis
                        with open(BOOKS_FILE, "w", encoding="utf-8") as f:
                            json.dump(kitaplar, f, ensure_ascii=False, indent=4)
                        print("Fiyat başarıyla değiştirildi.")
                        return
                    elif secim == "5":
                        degis=input("Yeni yayın evini giriniz: ")
                        kitap["Yayinevi"]=degis
                        with open(BOOKS_FILE, "w", encoding="utf-8") as f:
                            json.dump(kitaplar, f, ensure_ascii=False, indent=4)
                        print("Yayın evi başarıyla değiştirildi.")
                        return
                    elif secim == "6":
                        degis=input("Yeni yazarı giriniz: ")
                        kitap["Yazar"]=degis
                        with open(BOOKS_FILE, "w", encoding="utf-8") as f:
                            json.dump(kitaplar, f, ensure_ascii=False, indent=4)
                        print("Yazar başarıyla değiştirildi.")
                        return
                    elif secim == "0":
                        return
                    else:
                        secim=input("Hatalı giriş, Lütfen seçiminizi girin (0-6): ")
            
    
    except Exception as e:
        print("Bir hata oluştu:", e)