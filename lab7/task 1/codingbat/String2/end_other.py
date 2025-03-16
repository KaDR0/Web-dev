def  end_other(a, b):
    if len(a) >= len(b):
        if a[len(a)-len(b):len(a)].lower() == b.lower():
            return True
    else:
        if b[len(b)-len(a):len(b)].lower() == a.lower():
            return True
    return False
print( end_other(input(), input()))