# function overriding
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self,radius):
        return 3.14 * radius * radius

class Rectangle(Shape):
    def area(self,length,width):
        return length * width

class Triangle(Shape):
    def area(self,base,height):
        return 1/2 * base * height

circle = Circle()
print(circle.area(10))

rectangle = Rectangle()
print(rectangle.area(5,10))

triangle = Triangle()
print(triangle.area(5,10))

    