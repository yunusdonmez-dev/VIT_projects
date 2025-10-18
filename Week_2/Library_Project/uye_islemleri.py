#uyeler
#uye ekleme
#uye ara
#uye sil
#kitap alma
#kitap iade
#kitap takibi



#import kitap_islemleri
import json
import os


#uye ekleme

def uye_ekle():
    #uyeler.json Dosyasi yoksa olusturur ve uyeleri ekler.Bilgileri kullanicidan alir.
    if os.path.exists("uyeler.json") == False:           #dosya yok ve olusturacak.
        with open("uyeler.json", "w") as a:
            json.dump([],a)           #bos liste olarak olustur.

            
    with open("uyeler.json", "r", encoding = "utf-8") as f:
        uyeler_liste = json.load(f)
        
        isim = input("Uye adi: ")
        telefon = input("Telefon numarasi: ")
        adres = input("Adres: ")
        
    if uyeler_liste != []:        #uye listesi bos degilse id yi otomatik olusturur.
        yeni_id = max([uye["UyeID"] for uye in uyeler_liste]) + 1
    else:
        yeni_id = 1
        
    yeni_uye = {
        "UyeID": yeni_id, 
        "Isim":isim,
        "Telefon": telefon,
        "Adres": adres
        }
    uyeler_liste.append(yeni_uye)
    
    with open("uyeler.json", "w", encoding = "utf-8") as f:
        json.dump(uyeler_liste, f)
        

#uye listesi id ve isim ile

def uyeleri_goster():          
    #bu fonksiyon tum uyeleri gosterir
    with open("uyeler.json", "r", encoding = "utf-8") as f:
        uyeler_liste = json.load(f)
        isim_id_listesi = [(uye["Isim"], uye["UyeID"]) for uye in uyeler_liste]         #isim ve id ile liste
    
        for isim_id in isim_id_listesi:
            print(f"{isim_id[1]}-{isim_id[0]}")

#uye ara
#arama bilgisi al.

def uye_ara():
    
    if not os.path.exists("uyeler.json"):               #Dosyanin olup olmadigini kontrol eder
        print("Henüz hiç üye eklenmemiş.")
        return

    arama = input("Aramak istediginiz uye adi veya id girin: ").strip()

    with open("uyeler.json", "r", encoding = "utf-8") as f:
        uyeler_liste = json.load(f)
    
    bulunan_uyeler = []
    for uye in uyeler_liste:
        if arama.lower() in uye["Isim"].lower() or str(uye["UyeID"]) == arama:      #isim ve id icin buyuk kucuk harfe duyarsiz yapar
         bulunan_uyeler.append(uye)
        
    if bulunan_uyeler:
        print("\nBulunan Uyeler:")
        for uye in bulunan_uyeler:
            print(f"ID: {uye['UyeID']}")
            print(f"Isim: {uye['Isim']}")
            print(f"Telefon: {uye['Telefon']}")
            print(f"Adres: {uye['Adres']}")
        else:
            print("Eslesen uye bulunamadi.")
        
   
        
    
#uye silme

def uye_sil():
    with open("uyeler.json","r+", encoding = "utf-8") as f:
        uyeler_liste = json.load(f)
        
        uye_id = int(input("Silmek istediginiz uyenin ID'si:"))
        
        yeni_liste = [] 
        for i in uyeler_liste:
            if i["UyeID"] != uye_id:
                yeni_liste.append(i)
        uyeler_liste = yeni_liste

    with open("uyeler.json", "w", encoding = "utf-8") as f:
        json.dump(yeni_liste, f)   
        
    print(f"ID {uye_id} numarali uye silindi.")    
    
    
    
#kitap alma

def kitap_alma():
    with open ("kitap.json", "r", encoding = "utf-8") as f:
        kitaplar = json.load(f)
        
    uye_id = int(input("Kitap almak isteyen üyenin ID'si: "))
    kitap_barkod = int(input("Almak istediginiz kitabin barkodu: "))

    kitap_bulundu = False

    for kitap in kitaplar:
        if kitap["Barkod"] == kitap_barkod:
            kitap_bulundu = True
            if kitap.get("Durum") == "Odunc":
                print("Bu kitap zaten ödünçte.")
            else:
                kitap["Durum"] = "Odunc"
                kitap["UyeID"] = uye_id
                print(f"{kitap['Kitap_Adi']} kitabı, üye ID {uye_id} tarafından alındı.")
            break

    if not kitap_bulundu:
        print("Kitap bulunamadı.")
        
    with open("kitap.json", "w", encoding = "utf-8") as f:
        json.dump(kitaplar,f)
        
    
            
#kitap iade

def kitap_iade():
    with open ("kitap.json", "r", encoding = "utf-8") as f:
        kitaplar = json.load(f)
        
    uye_id = int(input("Kitabi iade edecek uyenin ID'si: "))
    kitap_barkod = input("Iade edilecek kitabin barkodu: ")
    
    kitap_bulundu = False

    for kitap in kitaplar:
        if kitap["Barkod"] == kitap_barkod and kitap.get("UyeID") == uye_id:
            kitap["Durum"] = "Mevcut"
            kitap.pop("UyeID", None)
            kitap_bulundu = True
            print(f"📚 {kitap['Kitap_Adi']} kitabı iade edildi.")
            break

    if not kitap_bulundu:
        print("Bu kitap bu üye tarafından alınmamış.")
           
    with open("kitaplar.json", "w", encoding="utf-8") as f:
        json.dump(kitaplar, f)
              
    
# kitap takibi

def kitap_takibi():
    with open ("kitap.json", "r", encoding = "utf-8") as f:
        kitaplar = json.load(f)
        
    print("\nKİTAP TAKİP LİSTESİ")
    print("-" * 40)
    for kitap in kitaplar:
        durum = kitap.get("Durum", "Mevcut")
        if durum == "Odunc":
            print(f"{kitap['Kitap_Adi']} → Ödünçte (Üye ID: {kitap.get('UyeID')})")
        else:
            print(f"{kitap['Kitap_Adi']} → Mevcut")
    print("-" * 40)
        
        
    
        
            
      
    
                
                
                
            
            
        
    
    




            




    
    


        
        
        

