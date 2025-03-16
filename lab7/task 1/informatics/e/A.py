a,b,c,d = input().split()

def minn(a, b):
    return a if a < b else b

def min(a, b, c, d):
    return minn(a,b) if minn(a, b) < minn(c, d) else minn(c, d)

print(min(a, b, c, d))