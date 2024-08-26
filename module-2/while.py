i=1

while i<=10:
    print(i)
    i=i+1

num=int(input("Enter a number:"))

def multiplication_table(n):
    for i in range(1,11):
        print("{}*{}={}".format(n,i,n*i))

multiplication_table(num)