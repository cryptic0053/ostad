class MyClass:
    x = 10
    y = 30
    z = 40

    def addTwo(self,a,b):
        sum=self.x+self.y+self.z+a+b
        print(sum)

obj1=MyClass()
obj1.addTwo(40,50)
