def pos_neg(a, b, c):
    if c == False and ((a < 0 and b > 0) or (a > 0 and b < 0)):
        return True
    elif c == True and a < 0 and b < 0:
        return True
    return False
print(pos_neg(int(input()), int(input()), input() == "True"))