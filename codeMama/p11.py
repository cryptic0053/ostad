a = int(input())
if a%4==0 and a%100!=0 or a%400==0:
    print(f"{a} is a leap year.")
else:
    print(f"{a} is not a leap year.")