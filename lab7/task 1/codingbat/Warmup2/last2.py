def   last2(a):
    b = 0
    for i in range(1, len(a) - 2):
        if a[-2] + a[-1] == a[i-1] + a[i]: b +=1
    return b
print(last2(input()))