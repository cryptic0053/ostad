class Father:
    x=10
    y=30

    def __init__(self):
        print("Father constructor")

    def add(self):
        print(self.x+self.y)

class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son constructor")


obj=Son()
obj=Father()