def  lone_sum(a, b, c):
    if a == b and b == c:
            return 0
    elif a == b:
        return c
    elif c == b:
        return a
    elif c == a:
        return b
    else:
        return a + b + c
print(lone_sum(int(input()), int(input()), int(input())))
