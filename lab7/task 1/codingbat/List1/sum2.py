def  sum2(a):
    if len(a) > 1:
        return a[0] + a[1]
    elif len(a) == 1:
        return a[0]
    return 0
print( sum2(list(map(int, input().split()))))