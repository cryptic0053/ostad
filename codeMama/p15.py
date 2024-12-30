import statistics

n = int(input())
a = list(map(int, input().split()))

med = statistics.median(a)

sum = 0
for num in a:
    if num<med:
        sum += num	
print(sum)
