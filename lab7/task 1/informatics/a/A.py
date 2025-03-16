import math

def hypot(a, b):
    return math.sqrt(pow(a,2) + pow(b,2))

a = int(input())
b = int(input())

print(hypot(a,b))