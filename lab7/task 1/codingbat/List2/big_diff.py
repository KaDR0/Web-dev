def  big_diff(a):
    return max(a) - min(a)
print( big_diff(list(map(int, input().split()))))