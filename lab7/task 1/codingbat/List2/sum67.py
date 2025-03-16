def  sum67(a):
    b = 0
    c = 0
    for i in a:
        if i  == 6:
            c = 1
        if c == 0:
            b += i
        if i == 7:
            c = 0

    return b
print( sum67(list(map(int, input().split()))))