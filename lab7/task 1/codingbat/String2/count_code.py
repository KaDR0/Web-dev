import re
def  count_code(a):
    if a.count("code") == 0:
        pattern = r'co\we'
        matches = re.findall(pattern, a)
        return len(matches)
    return a.count("code")
print( count_code(input()))