class MyClass:
    x = 10
    y = 30
    z = 40

    def addTwo(self,a,b):
        sum=self.x+self.y+self.z+a+b
        print(sum)

    def addNew(self):
        sum2=self.x+self.y+self.z
        print(sum2)

obj1=MyClass()
obj1.addTwo(40,50)
obj1.addNew()

obj=MyClass()
obj.addTwo(100,200)

obj2=MyClass()
obj2.addNew()
