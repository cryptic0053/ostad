class MyClass:
    x = 10
    y = 20

    def __init__(self, zValue, xValue):
        self.z=zValue
        self.x=xValue

    def addTwo(self):
        print(self.x+self.y+self.z)

obj = MyClass(900, 600)

obj.addTwo()