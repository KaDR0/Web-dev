n = int(input())

list = input().split()


res = 0
for i in range(1,n):
    if(int(list[i+1]) < int(list[i]) > int(list[i-1])):
        res += 1

print(res)