a = list(map(int, input().split()))
swap = a[0]
a[0] = a[1]
a[1] = swap
print(f"Before swapping: num1 = {a[1]}, num2 = {a[0]}")
print(f"After swapping: num1 = {a[0]}, num2 = {a[1]}")