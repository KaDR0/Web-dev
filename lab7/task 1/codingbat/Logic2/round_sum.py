def  round10(a):
    if a%10 >= 5:
        return (a//10 + 1) * 10
    return (a//10) * 10
def  round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

print(round_sum(int(input()), int(input()), int(input())))
