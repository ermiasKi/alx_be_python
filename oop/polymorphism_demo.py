class Shape:
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def area(self, length:int, width:int):
        return length*width


class Circle(Shape):
    def area(self, radius:int):
        return 3.14*radius*radius
    
