def    string_match(a, b):
    c = 0
    for i in range(1, min(len(a), len(b))):
        if a[i-1] + a[i] == b[i-1] + b[i]: c +=1
    return c
print(string_match(input(), input()))