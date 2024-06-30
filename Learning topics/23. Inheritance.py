class Shape:
    def __init__(self):
        self.color = (0,0,0)
class Rectangle(Shape):
    def __init__(self, w,h):
        Shape.__init__(self)
        self.width = w
        self.height = h
    
    def area(self):
        return self.width*self.height
rect1 = Rectangle(20,10)
print(rect1.height)
print(rect1.area())