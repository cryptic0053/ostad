def msg():
    print("hello world")

msg()

def addTwo(a,b):
    return a+b

x=addTwo(30,40)
print(x)

def add(*numbers):
    for number in numbers:
        print(number)

add(10,20,30,40)

def person(**per):
    for key,value in per.items():
        print(f'{key}:{value}')


person(
    name="Argha",
    age=22,
    city="Rajshahi"
)
