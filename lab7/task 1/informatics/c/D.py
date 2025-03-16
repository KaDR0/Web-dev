x = int(input())

d = int(input())


cnt = 0

while(True):
    if(x == 0):
        break
    a = x%10
    if(a == d):
        cnt += 1
    x = a
    
    
print(cnt)