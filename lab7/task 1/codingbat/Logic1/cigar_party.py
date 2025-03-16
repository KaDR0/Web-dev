def  cigar_party(a, b):
    if a >= 30 and a <= 60 and b ==False:
        return True
    elif a >= 30 and b == True:
        return True
    return False
print( cigar_party(int(input()), input() == "True"))