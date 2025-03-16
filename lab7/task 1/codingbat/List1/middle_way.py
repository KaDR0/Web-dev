def  middle_way(a, b):
    return [a[1], b[1]]
print( middle_way(list(map(int, input().split())), list(map(int, input().split()))))