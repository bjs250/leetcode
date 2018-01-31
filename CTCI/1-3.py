def removeDuplicates(s):
    if not s:
        return s
    ans = s[0]
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            continue
        else:
            ans = ans + s[i]
    return ans


s = "alligator"
print(removeDuplicates(s))

s = "apple"
print(removeDuplicates(s))
