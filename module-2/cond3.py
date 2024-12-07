a=3
print(a<2)
print(type(a<2))

n=input()
n=int(n)

# if n>=0:print("positive")
# else:print("negative")


if n%2==0 and n>=0:
    print("positive & even")
elif n%2!=0 and n>=0:
    print("positive & odd")
elif n%2==0 and n<0:
    print("negative & even")
else:
    print("negative & odd")            