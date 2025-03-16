def  common_end(a, b):
    if a[len(a)-1] == b[len(a)-1] or a[0] == b[0]:
        return True
    return False
print( common_end(list(map(int, input().split())), list(map(int, input().split()))))