import book_transactions
import member_transactions
import os

def ana_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') # Clear terminal
        print("""
    --------------------------------------------------------------------------
    -                    HALK KÜTÜPHANEMİZE HOŞ GELDİNİZ                     -
    --------------------------------------------------------------------------
    -   1- ÜYELİK İŞLEMLERİ = 1                                              -
    -   2- KİTAP İŞLEMLERİ  = 2                                              -
    -   3- ÇIKIŞ            = 0                                              -
    --------------------------------------------------------------------------
        """)
        secim = input("Lütfen yapmak istediğiniz seçimin kodunu girin : ")

        if secim == "1":
            uyelik_menu()
        elif secim == "2":
            kitap_menu()
        elif secim == "0":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")

def uyelik_menu():
    while True:
        print("""
    --------------------------------------------------------------------------
    -                           ÜYELİK İŞLEMLERİ                             -
    --------------------------------------------------------------------------
    -       ÜYE GÜNCELLEME    = 1              KİTAP ÖDÜNÇ VERME = 5         -
    -       ÜYE EKLEME        = 2              KİTAP İADE        = 6         -
    -       ÜYE ARA           = 3              KİTAP TAKİBİ      = 7         -
    -       ÜYE SİL           = 4              ÇIKIŞ             = 0         -
    --------------------------------------------------------------------------
        """)
        secim = input("Islem seciniz : ")

        if secim == "1":
            member_transactions.uye_guncelle()
        elif secim == "2":
            member_transactions.uye_ekle()
        elif secim == "3":
            member_transactions.uye_ara()
        elif secim == "4":
            member_transactions.uye_sil()
        elif secim == "5":
            member_transactions.kitap_odunc_verme()
        elif secim == "6":
            member_transactions.kitap_iade()
        elif secim == "7":
            member_transactions.kitap_takibi()
        elif secim == "0":
            break
        else:
            print("Geçersiz işlem. Lütfen tekrar deneyin.")

def kitap_menu():
    while True:
        print("""
    --------------------------------------------------------------------------
    -                            KİTAP İŞLEMLERİ                             -
    --------------------------------------------------------------------------
    -       KİTAP GÜNCELLE = 1                                               -
    -       KİTAP EKLE     = 2                                               -
    -       KİTAP ARA      = 3                                               -
    -       KİTAP SİL      = 4                               ÇIKIŞ = 0       -
    --------------------------------------------------------------------------
        """)
        secim = input("Islem seciniz : ")

        if secim == "1":
            book_transactions.kitap_guncelle()
        elif secim == "2":
            book_transactions.kitap_ekle()
        elif secim == "3":
            book_transactions.kitap_ara()
        elif secim == "4":
            book_transactions.kitap_sil()
        elif secim == "0":
            break
        else:
            print("Geçersiz işlem. Lütfen tekrar deneyin.")

# Programı başlat
if __name__ == "__main__":
    ana_menu()
