n = int(input())

list = input().split()


res = 0
for i in range(1,n):
    if(list[i] > list[i - 1]):
        res += 1

print(res)