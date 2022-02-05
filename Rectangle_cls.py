class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)

len = int(input("Enter the length of rectangle"))
bre = int(input("Enter the breadth of rectangle"))
rect1 = Rectangle(len, bre)
print(f"Area: {rect1.area()}")
print(f"Perimeter: {rect1.perimeter()}")