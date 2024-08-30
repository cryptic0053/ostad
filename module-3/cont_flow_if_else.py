mark=int(input("Enter your mark:"))
if mark<=100 and mark>=80:
    print("A+")
elif mark<80 and mark>=70:
    print("A")
elif mark<70 and mark>60:
    print("A-")
else:
    print("F")