def  array_front9(a):
    for i in range(4):
        if a[i] == "9": return True
    return False
print(array_front9(input().split()))