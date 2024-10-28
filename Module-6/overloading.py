class Myclass:
    x=10
    y=20

    def addtwo(self,a=0,b=0):
        print(self.x+self.y+a+b)

    

obj=Myclass()
obj.addtwo()