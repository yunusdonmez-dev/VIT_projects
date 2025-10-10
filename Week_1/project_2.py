#Age Checker

age = int(input("Enter your age:"))

if age < 18:
    print("You are not an adult.")
elif age == 18:
    print("You just became an adult.")
else:
    print("You are an adult.")
   
    BirthYear = int(input("Enter your birth year:"))
    CurrentYear = 2025
    CalculatedAge = CurrentYear - BirthYear
    print("Your calculated age is:", CalculatedAge)
