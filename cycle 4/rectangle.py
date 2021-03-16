class Rectangle:
    def __init__(self ,breadth, length):
        self.breadth = breadth
        self.length = length
    def area(self):
        return self.breadth * self.length
    def perimeter(self):
        return 2 * (self.breadth + self.length)
print("Rectangle 1")
a=int(input("Enter the length:"))
b= int(input("Enter the breadth:"))
ob1=Rectangle(a,b)

print("Area 1 = ",ob1.area())
print("Perimeter = ",ob1.perimeter())

print("Rectangle 2")
a=int(input("enter the length:"))
b= int(input("enter the breadth:"))
ob2=Rectangle(a,b)

print("Area 2= ",ob2.area())
print("Perimeter=",ob2.perimeter())
if ob1.area() == ob2.area():
    print("The area's are equal")
else:
    print("not equal")