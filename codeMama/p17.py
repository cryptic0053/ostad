def factorial(self):
    if self == 0:
        return 1
    else:
        return self * factorial(self - 1)
    
x = int(input())
print(factorial(x))