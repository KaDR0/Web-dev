def  make_bricks(a, b, c):
    if b*5 > c:
        if c % 5 <= a:
            return True
        return False
    elif b*5 == c:
        return True
    else:
        if c - b*5 <= a:
            return True
        return False
print(make_bricks(int(input()), int(input()), int(input())))
