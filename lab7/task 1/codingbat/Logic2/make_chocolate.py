def  make_bricks(a, b, c):
    if b*5 > c:
        if c % 5 <= a:
            return c % 5
        return -1
    elif b*5 == c:
        return 0
    else:
        if c - b*5 <= a:
            return c-(b * 5)
        return -1
print(make_bricks(int(input()), int(input()), int(input())))
