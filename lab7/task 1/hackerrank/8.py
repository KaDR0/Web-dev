x = int(input())
y = int(input())
z = int(input())
n = int(input())
m = []
for i in range(x+1):
    for j in range(y + 1):
        for k in range(x + 1):
            if i + j + k != n:
                m.append([i, j, k])
print(m)