a = int(input())
b = int(input())

for i in range(a, b+1):
    for j in range(a, i):
        if(j*j == i):
            print(i)
            break