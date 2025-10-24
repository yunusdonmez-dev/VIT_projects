class Customer():
    def __init__(self, name, surname, tc_identification, phone):
        self.name = name
        self.surname = surname
        self.tc_identification = tc_identification
        self.phone = phone

    def display_information(self):
        print(f"Name: {self.name} {self.surname}")
        print(f"TC ID: {self.tc_identification}")
        print(f"Phone: {self.phone}")
    
    
class Account(Customer):
    def __init__(self, customer, account_number, balance):
        self.customer = customer
        self.account_number = account_number
        self.balance = balance
        
    def display_information(self):                   #bilgi gosterme metodu
        print(f"Name; {self.customer.name} {self.customer.surname}")
        print(f"TC ID: {self.customer.tc_identification}")
        print(f"Phone: {self.customer.phone}")
        
    def deposit(self, amount):                      #para yatirma metodu(deposit)
        self.balance += amount                      #şu anki bakiye üzerine yeni yatırılan parayı ekler.
        print(f"{amount} TL deposited. New balance: {self.balance}. TL")
        
    def money_check(self, amount):               #para cekme metodu
        if amount <= self.balance:       
            self.balance -= amount               #cekilmek istenen para cikariliyor sonuc guncel para
            print(f"{amount} TL withdrawn. Remaining balance: {self.balance} TL")
        else:
            print("Insufficient balance! Transaction cancelled.")
            
    def display_balance(self):                      #bakiye gosterme metodu
        print(f"Current balance: {self.balance}")
        
customer1 = Customer("Yasemin", "Kalemli", "3452347689","05324562398" )             #musteri olustur
account1 = Account(customer1, "TR12345", 1300)                                      #hesap olustur
account1.display_information()                      #musteri bilgilerini gosterir
customer1.display_information()



            
           
        
           
        
        