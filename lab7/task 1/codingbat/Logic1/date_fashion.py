def  date_fashion(a, b):
    if a >= 8 or b >= 8:
        return 2
    elif a <= 2 or b <= 2:
        return 0
    return 1
print( date_fashion(int(input()), int(input())))