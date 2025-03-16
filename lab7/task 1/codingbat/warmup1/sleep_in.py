def sleep_in(weekday, vacation):
    if weekday == False or vacation == True:
        return True
    return False
print(sleep_in(bool(input()), bool(input())))