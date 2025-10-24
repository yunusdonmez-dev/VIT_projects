class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
class OffRoadVehicle(Vehicle):
    def __init__(self, make, model, year, four_wheel_drive):
        super().__init__(make, model, year)
        self.four_wheel_drive = four_wheel_drive
        
        
    
class SportsCar(Vehicle): 
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.max_speed = max_speed
        
suv = OffRoadVehicle("Toyota", "Land Cruiser", 2022, True)
sportscar = SportsCar("Ferrari", "F8 Tributo", 2023, 340)

print("Off-Road Vehicle:")
print(f"Make: {suv.make}, Model: {suv.model}, Year: {suv.year}, 4x4: {suv.four_wheel_drive}")

print("\nSports Car:")
print(f"Make: {sportscar.make}, Model: {sportscar.model}, Year: {sportscar.year}, Max Speed: {sportscar.max_speed} km/h")       