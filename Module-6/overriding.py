class Father:
    x=10
    y=30

    def add(self):
        print(self.x+self.y)

class Son(Father):

    def add(self):
        print(self.x+self.y+20)

obj=Son()
obj.add()