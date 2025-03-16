n = int(input())

list = input().split()

res = 0

for i in range(n):
    if(int(list[i]) > 0):
        res += 1
        
print(res)

