import datetime

current_temp = 31
reference_temp = 20

result = current_temp < reference_temp
print(result)
print(type(result))

result = current_temp % 2 == 0
print(result)
print(type(result))

if result:
    print(current_temp, "is even number")
else:
    print(current_temp, "is odd number")

today = input("Enter a day:")
public_holiday = input("Is it public holiday?(yes/no)")
public_holiday = public_holiday.lower()
is_sick_today = input("Are you sick today?(yes/no)")
is_sick_today = is_sick_today.lower()
if today == "Sunday":
    print("No office day")
elif today == "Saturday":
    print("No office day")
elif public_holiday == "ÿes":
    print("No office day")
elif is_sick_today == "yes":
    print("No office day")
else:
    print("Office day")



def meets_requirement(price, brand, color, milege):
    budget = 19000
    my_brand = "BMW"
    my_color = "Silver"
    maximum_milege = 20000

    if price <= budget and brand == my_brand and milege <= maximum_milege and my_color == color:
        return True
    else:
        return False

p=int(input("Price:"))
brand = input("Which one:")
color = input("Color:")
milege = int(input("Milege:"))

if meets_requirement(p,brand,color,milege):
    print("Consider it")
else:
    print("Dont")