def  first_last6(a):
    if a[len(a)-1] == 6 or a[0] == 6:
        return True
    return False
print( first_last6(list(map(int, input().split()))))