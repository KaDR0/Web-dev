def  make_ends(a):
    if len(a) > 1:
        return [a[0], a[len(a)-1]]
    return a[0]
print( make_ends(list(map(int, input().split()))))