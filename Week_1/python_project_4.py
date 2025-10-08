

products_2 = {"apple" : {"unit" : "kg", "price" : 3} , "banana" : {"unit" : "kg", "price" : 5},"bread" : {"unit" : "piece", "price" : 2},"milk" : {"unit" : "liter", "price" : 4}}

total_price = 0
total_item = 3
print(20*"=" + " Welcome to our team-2 mini market " + 20*"=")

for product in products_2: # Show the list of products to user

    print(f"{product} is {products_2[product]['price']}$ per {products_2[product]['unit']}")

count = 0
while count < total_item:

    basket = input("Please enter the products you want to buy : ").strip().lower()
    
    if basket in products_2:

        # Get the product info after selection
        unit = products_2[basket]["unit"]
        price = products_2[basket]["price"]
        while True:
            amount = input(f"How many {unit} {basket} do you want to buy ? ") 
            try :    # Validate user input 
                amount = int(amount)
                if amount <= 0:
                    print("Amount must be positive")
                    continue
                break
            except Exception :
                print("Please enter a valid number")


        total_price += amount*price
        count += 1
    else :
        print("Please enter a valid product")
        continue

print(f"Total price would be {total_price} $. Do you want to pay cash or by card ? ")