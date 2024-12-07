#single & multiple inheritance
class Father:
    x=10
    y=30

    def add(self):
        print(self.x+self.y)

    def mul(self):
        print(self.x*self.y)

class Mother:
    a=700
    b=500

    def sub(self):
        print(self.a-self.b)

    def div(self):
        print(self.a/self.b)

class Son(Father,Mother):
    pass

obj=Son()
obj.sub()
obj.mul()
print(obj.x)
print(obj.y)
print(obj.a)
print(obj.b)
obj.add()
obj.div()

#multilevel inheritance
class Grandfather:
    x=10
    y=30

    def add(self):
        print(self.x+self.y)

    def mul(self):
        print(self.x*self.y)

class Father(Grandfather):
    pass

class Son(Father):
    pass

obj=Grandfather()
print(obj.x)
print(obj.y)
obj.add()
obj.mul()

obj=Father()
print(obj.x)
print(obj.y)
obj.add()
obj.mul()

obj=Son()
print(obj.x)
print(obj.y)
obj.add()
obj.mul()
