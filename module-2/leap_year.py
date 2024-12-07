year=input("year:")
year=int(year)
#Type-1:
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"is leap year")
        else:
            print(year,"is not leap year")    
else:
    print(year,"is not leap year")
#Type-2:
if year%4==0:
    if year%100==0 and year%400==0:
        print(year,"is a leap year")
    else:
        print(year,"is not leap year")
else:
    print(year,"is not leap year")        
