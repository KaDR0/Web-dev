def  double_char(a):
    b = ""
    for i in range(len(a)):
        b += a[i] * 2
    return b
print( double_char(input()))