n = int(input())

arr = list(map(int, input().split()))

target = int(input())

found = False
for i in range(len(arr) - 2):
    for j in range(i + 1, len(arr) - 1):
        for k in range(j + 1, len(arr)):
            if arr[i] + arr[j] + arr[k] == target:
                print(*sorted([arr[i],arr[j],arr[k]]))
                found = True
                break
        if found:
            break
    if found:
        break
