def  same_first_last(a):
    if len(a) > 0 and a[0] == a[len(a)-1]:
        return True
    return False
print( same_first_last(input().split()))