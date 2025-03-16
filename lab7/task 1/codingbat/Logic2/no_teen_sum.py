def  fix_teen(a):
    if a >= 13 and a <= 19 and a != 15 and a != 16:
        return 0
    return a
def  no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

print(no_teen_sum(int(input()), int(input()), int(input())))
