n = int(input())

list = input().split()

res = []

for i in range(n):
    res[n-i-1] = list[i]
    
print(res)