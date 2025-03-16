def  has22(a):
    b = 0
    for i in a:
        if i == 2:
            b += 1
            if b == 2:
                return True
        else:
            b = 0
    return False
print( has22(list(map(int, input().split()))))