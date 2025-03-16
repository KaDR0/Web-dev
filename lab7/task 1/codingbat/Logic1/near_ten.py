def  near_ten(a):
    if a % 10 <= 2 or a % 10 >= 8:
        return True
    return False
print(near_ten(int(input())))
