class Myclass:
    x=10
    y=20

    def addtwo(self,a=0,b=0):
        print(self.x+self.y+a+b)

    def myMethod(self,*a):
        print(a)

obj=Myclass()
obj.addtwo()
obj.addtwo(10)
obj.addtwo(10,10)

obj.myMethod(10,20,30)
obj.myMethod(10)
obj.myMethod(10,20)
obj.myMethod(10,20,30,40)
