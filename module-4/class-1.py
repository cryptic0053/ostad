import random
numbers=[1,6,3,2,6,2,10,1,5,9]

max_number=max(numbers)
print(max_number)

max_number=float('-inf')#linear search

for n in numbers:
    if n>max_number:
        max_number=n

print(max_number)

nums=[]
for _ in range(10):
    nums.append(random.randint(1,100))

print(nums)
print(max(nums))

print(dir(random))

import matplotlib.pyplot as plt

days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
tempa=[]

for i in range (7):
    temp=int(input(f"{days[i]}:"))
    tempa.append(temp)

plt.plot(days,tempa,marker='o')

plt.title('Average Temparature over a week')
plt.xlabel('Days')
plt.ylabel('Temparature(c)')

plt.show()