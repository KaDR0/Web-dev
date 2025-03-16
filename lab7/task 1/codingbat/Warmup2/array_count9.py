def    array_count9(a):
    b = 0
    for i in range(len(a)):
        if a[i] == "9": b +=1
    return b
print(array_count9(input().split()))