class Person:
    def __init__(self,n):
        self.name= n
    def hello(self):
        print("Hiiiiii" ,self.name)

t = Person("Taki")
t.hello()
    