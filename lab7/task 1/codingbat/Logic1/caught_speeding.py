def  caught_speeding(a, b):
    if b == True:
        a -= 5
    if a <= 60:
        return 0
    elif a >= 61 and a <= 80:
        return 1
    return 2
print( caught_speeding(int(input()), input() == "True"))
