def  in1to10(a, b):
    if b == True and (a <= 1 or a >= 10):
        return True
    elif b == False and a >=1 and a <= 10:
        return True
    return False
print(in1to10(int(input()), input() == "True"))
