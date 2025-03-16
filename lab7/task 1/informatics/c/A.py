a = int(input())
b = int(input())

list = []

for i in range(a,b+1):
    if(i %2 == 0):
        list.append(i)
        
print(list)