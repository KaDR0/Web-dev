def  sum13(a):
    b = 0
    for i in a:
        if i  == 13:
            break
        b += i
    return b
print( sum13(list(map(int, input().split()))))