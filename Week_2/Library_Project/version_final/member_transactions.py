import json
import os
import datetime
import time_module



current_dir = os.path.dirname(os.path.abspath(__file__))

MEM_FILE = os.path.join(current_dir, 'members.json')
BOOKS_FILE = os.path.join(current_dir, 'kitap.json')
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

def transaction_log(id, barcode):
    # This function hold the record of every transaction as log in json file.
    # This function takes many parameters. Which boek, who takes it, when , when due, boek info, user info
    # Or book barcode(unique) user id(unique) 
    current_dir = os.path.dirname(os.path.abspath(__file__))
    users_json_path = os.path.join(current_dir, 'members.json')
    books_json_path = os.path.join(current_dir, 'kitap.json')

    with open(users_json_path, 'r',encoding='utf-8') as f:
        users_data = json.load(f)
        user_data = list(filter(lambda x: x['id'] == id, users_data)) # the user is filtered
    
    with open(books_json_path, 'r',encoding='utf-8') as f:
        books_data = json.load(f) 
        book_data = list(filter(lambda x: x['Barkod'] == barcode, books_data)) # the book is filtered

    transactions_json_path = os.path.join(current_dir, 'transactions.json')
    
    # Make a transactions.json file if it is not already there
    if os.path.exists(transactions_json_path) == False:
        with open(transactions_json_path, 'w',encoding='utf-8') as f: 
            json.dump([], f)

    with open(transactions_json_path, 'r',encoding='utf-8') as f:
        transactions_data = json.load(f)
        new_transaction = {
        'Id' : id,
        'User_name' : user_data[0]['uyeadi'],
        'Tel' : user_data[0]['tel'],
        'Adres' : user_data[0]['adres'],
        'barcode' : barcode,
        'Language' : book_data[0]['Dil'],
        'Price' : book_data[0]['Fiyat'],
        'Book_name' : book_data[0]['Kitap_Adi'],
        'publisher' : book_data[0]['Yayinevi'],
        'Author' : book_data[0]['Yazar'],
        'Start_date' : str(datetime.date.today()),
        'Due_date' : str(time_module.two_weeks_ahead())
         }
        transactions_data.append(new_transaction) # Add new transaction to the list
    with open(transactions_json_path ,'w',encoding='utf-8') as f:
        json.dump(transactions_data,f, ensure_ascii=False, indent=4)

def lent_book():

    # Lent a boek
    barcode = int(input("Enter the barcode of the book : "))

    current_dir = os.path.dirname(os.path.abspath(__file__))
    books_json_path = os.path.join(current_dir, 'kitap.json')

    with open(books_json_path, 'r',encoding='utf-8') as f:
        books_data = json.load(f) 
        book_data = list(filter(lambda x: x['Barkod'] == barcode, books_data)) # the book is filtered    
        if book_data[0]['Kitap_Adi'] != None:
            print(book_data[0]['Kitap_Adi'])
        else:
            print('Book is not available')
            # selection = int(input("Select : "))
            lent_book() # Call the function but how to exit ???
    
    user_id = int(input('Enter your user Id : '))

    users_json_path = os.path.join(current_dir, 'members.json')
    with open(users_json_path, 'r',encoding='utf-8') as f:
        users_data = json.load(f)
        user_data = list(filter(lambda x: x['id'] == user_id, users_data)) # the user is filtered
        if user_data[0]['uyeadi'] != None:
            print(user_data[0]['uyeadi'])
        else:
            print('User is unknown. Try to be member')
            # lent_book() # Call the function but how to exit ???    

    transaction_log(user_id,barcode)
    # delete the book from the list
    print(f"Book is succesfully lended, due date is {str(time_module.two_weeks_ahead())}. Enjoy! ")

def return_book():

    barcode = int(input("Enter the barcode : "))

    current_dir = os.path.dirname(os.path.abspath(__file__))
    books_json_path = os.path.join(current_dir, 'kitap.json')

    with open(books_json_path, 'r', encoding='utf-8') as f:
        books = json.load(f)

        book = list(filter(lambda x:x['Barkod'] == barcode, books))[0]['Kitap_Adi']

    id = int(input("Enter the user id : "))

    users_json_path = os.path.join(current_dir, 'members.json')

    with open(users_json_path, 'r', encoding='utf-8') as f:
        users = json.load(f)

        user = list(filter(lambda x:x['id'] == id, users))[0]['User_name']    



   
    # Add the book again to the list

if __name__ == "__main__":
    print("işlem")
