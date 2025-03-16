arr = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    arr.append([score, name])
arr.sort()
b = -1
for i in range(len(arr)):
    if arr[i][0] != arr[0][0] and b == -1:
        b = arr[i][0]
        print(arr[i][1])
    elif arr[i][0] == arr[0][0]:
        continue
    elif b == arr[i][0]:
        print(arr[i][1])
    else:
        break