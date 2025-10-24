class Shape():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
class Rectangle(Shape):
    def calculate_area(self):
        return self.width * self.height
    
        
class Square(Shape):
    def calculate_area(self):
        return self.width * self.width
        
rectangle = Rectangle(4, 8)
square = Square(6,6)
        
print("Rectange Area:", rectangle.calculate_area())
print("Square Area:", square.calculate_area())
        
    
        
        
        
        
        
   
    