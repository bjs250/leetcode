def uniqueString(s):
    if not s:
        return True
    d = dict()
    for c in s:
        try:
            d[c] += 1
            return False
        except:
            d[c] = 0
    return True

s = ""
print(uniqueString(s))
s = "a"
print(uniqueString(s))
s = "abc"
print(uniqueString(s))
s = "aab"
print(uniqueString(s))
