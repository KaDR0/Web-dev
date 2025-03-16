def array123(a):
    for i in range(3, len(a) + 1):
        if a[i-3:i] == ["1", "2", "3"]: return True
    return False
print(array123(input().split()))