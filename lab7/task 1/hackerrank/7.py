def full_str(a):
    leap = ""
    for i in range(1, a + 1):
        leap += str(i)
    return leap

a = int(input())
print(full_str(a))