def  squirrel_play(a, b):
    if a >= 60 and a <= 90 and b == False:
        return True
    elif a >= 60 and a <= 100 and b == True:
        return True
    return False
print( squirrel_play(int(input()), input() == "True"))