height, weight = map(float, input().split())
bmi=weight/(height**2)

if bmi<18.5:
    print (f"BMI: {bmi:.2f}\nUnderweight")
elif 18.5<=bmi<25.0:
    print(f"BMI: {bmi:.2f}\nNormal weight")
elif 25.0<=bmi<30.0:
    print(f"BMI: {bmi:.2f}\nOverweight")
else:
    print(f"BMI: {bmi:.2f}\nObese")