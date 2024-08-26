fruits=["Apple","Banana","Orange","Mango"]
for fruit in fruits:
    print(fruit)

for i in range(4):
    print(i,".",fruits[i])

for i in range(3,8,2):
    print(i)

for i in range(1,11):
    print(i*i)

num=int(input("Enter a number:"))

def multiplication_table(n):
    for i in range(1,11):
        print("{}*{}={}".format(n,i,n*i))

multiplication_table(num)