def  alarm_clock(a, b):
    if b == True or a == 0 or a == 6:
        return "10:00"
    return "7:00"
print(alarm_clock(int(input()), input() == "True"))
