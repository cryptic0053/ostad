import math

my_list=[1,2,3]
print(type(my_list))

my_list.append(4)
print(my_list)

class MyClass:
    total=6

    def say_hello():
        print("Hello")

print(MyClass.total)   
MyClass.say_hello() 

class A:
    pass

obj1=A()
print(obj1)

class Fraction:

    def __init__(self,num,denom):
        self.numerator=num
        self.denominator=denom

    def __str__(self):
        return "{}/{}".format(self.numerator,self.denominator)
    
    def simplify(self):
        g=math.gcd(self.numerator,self.denominator)
        self.numerator=self.numerator//g
        self.denominator=self.denominator//g

f1=Fraction(20,40)
print(f1.numerator,f1.denominator)
print(f1)
f1.simplify()
print(f1)