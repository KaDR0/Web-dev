def  rotate_left3(a):
    return [a[1], a[2], a[0]]
print( rotate_left3(list(map(int, input().split()))))