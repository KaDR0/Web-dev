def power(a:float, b:int):
    res = 1
    for i in range(b):
        res *= a
    return res
        
a = float(input())
b = int(input())

print(power(a, b))