n = int(input())
arr = list(map(int, input().split()))
a =  -101
b =  -101
for i in range(n):
    if arr[i] > a:
        b = a
        a = arr[i]
    elif arr[i] != a and b < arr[i]:
        b = arr[i]
print(b)