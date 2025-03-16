def   string_splosion(a):
    b = ""
    for i in range(len(a)):
        b += a[0:i+1]

    return b
print(string_splosion(input()))