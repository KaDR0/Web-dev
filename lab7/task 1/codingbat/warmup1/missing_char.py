def missing_char(a, b):
    return a[0 : b] + a[b+1 : len(a)]
print(missing_char(input(), int(input())))