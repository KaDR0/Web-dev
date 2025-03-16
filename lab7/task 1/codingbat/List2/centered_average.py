def  centered_average(a):
    return (sum(a) - max(a) - min(a)) // (len(a) - 2)
print( centered_average(list(map(int, input().split()))))