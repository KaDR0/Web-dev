def monkey_trouble(a_smile, b_smile):
    if a_smile == b_smile:
        return True
    return False
print(monkey_trouble(bool(input()), bool(input())))