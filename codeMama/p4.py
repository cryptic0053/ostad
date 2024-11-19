a=input()
b=0
for i in range(len(a)):
    if a[i]=='0':
        if (i==0 or a[i-1]!='0') and (i==len(a)-1 or a[i+1]!='0'):
            b=b+1

print(b)
